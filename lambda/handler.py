# -*- coding: utf-8 -*-
"""Define the CloudEndure lambda function.

Attributes:
    LOG_LEVEL (str):
    REGION_OVERRIDE (str): If provided, this value will override the default AWS region.
    logger (logging.Logger): The logger to be used throughout execution of the AWS Lambda.

"""
import datetime
import json
import logging
import os
from typing import Any, Dict, List

import boto3
from botocore.exceptions import ClientError

from .exceptions import ImproperlyConfigured, InvalidPayload

LOG_LEVEL = getattr(logging, os.environ.get("CLOUDENDURE_LOGLEVEL", "INFO"))
REGION_OVERRIDE = os.environ.get("CLOUDENDURE_REGION_OVERRIDE", "")

logger = logging.getLogger()

logger.setLevel(LOG_LEVEL)


def send_sqs_message(image_info: Dict) -> bool:
    """Send a SQS message.

    The message includes the AMI information that was created from the migrated
    instance that passed testing post migration in CloudEndure.

    Raises:
        ClientError: The exception is raised in the event of a boto3 client error.
        ImproperlyConfigured: The exception is raised in the event of missing or invalid
            environment configuration settings.

    Returns:
        bool:  Whether or not the message has been sent successfully.

    """
    queue_url = os.environ.get("QueueURL", "")
    if not queue_url:
        raise ImproperlyConfigured("Missing environment variable:  QueueURL")

    try:
        message = json.dumps(image_info)
        sqsclient = boto3.client("sqs")
        sqsclient.send_message(QueueUrl=queue_url, MessageBody=message)
    except ClientError as e:
        logger.error(e.response)
        return False
    except ImproperlyConfigured as e:
        logger.error(e)
        return False
    return True


def create_ami(project_id: str, instance_id: str) -> bool:
    """Create an AMI from the specified instance.

    Args:
        project_id (str): The ID associated with the Project.
        instance_id (str): The ID associated with the AWS instance.

    Raises:
        ClientError: The exception is raised in the event of a boto3 client error.

    Returns:
        bool: Whether or not the AMI has been created successfully.

    """
    try:
        _ec2_client = boto3.client("ec2")

        # Create an AMI from the migrated instance
        image_creation_time = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
        ec2_image = _ec2_client.create_image(
            InstanceId=instance_id,
            Name=f"{image_creation_time}",
            Description=f"{project_id} {image_creation_time}",
            NoReboot=True,
        )
        logger.info("AMI Id: %s", ec2_image)
        _filters: List[Dict] = [{"Name": "resource-id", "Values": [instance_id]}]

        # Tag the newly created AMI by getting the tags of the migrated instance to copy to the AMI.
        ec2_tags = _ec2_client.describe_tags(Filters=_filters)

        logger.info(ec2_tags)
        for tag in ec2_tags["Tags"]:
            _ec2_client.create_tags(
                Resources=[ec2_image["ImageId"]],
                Tags=[{"Key": tag["Key"], "Value": tag["Value"]}],
            )

        send_sqs_message(ec2_image)

    except ClientError as err:
        logger.error(err.response)
        return False
    return True


def lambda_handler(event: Dict[str, Any], context: Dict[str, Any]) -> bool:
    """Define the AWS Lambda entry point and handler.

    Args:
        event (str): The event performed against Lambda.
        context (dict): The context of the request performed against Lambda.

    Raises:
        ClientError: The exception is raised in the event of a boto3 client error.
        InvalidPayload: The exception is raised in the event of an invalid payload.

    Returns:
        bool: Whether or not the lambda function has executed successfully.

    """
    logger.debug(event)

    event_records = event.get("Records", [])
    if not event_records:
        return False

    try:
        event_message = event_records[0].get("Sns", {}).get("Message", "")
        json_sns_message = json.loads(event_message)
        instance_id: str = json_sns_message.get("instanceId", "")
        project_id: str = json_sns_message.get("projectId", "")

        if json_sns_message.get("Pass", "NA") != "True":
            raise InvalidPayload(
                f"{instance_id} did not pass post migration testing! Not creating an AMI."
            )
        else:
            logger.info(
                "%s passed post migration testing. Creating an AMI." % (instance_id)
            )
            create_ami(project_id, instance_id)
    except ClientError as e:
        logger.error(e.response)
        return False
    except InvalidPayload as e:
        logger.error(e)
        return False
    return True
