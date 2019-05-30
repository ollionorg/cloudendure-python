# -*- coding: utf-8 -*-
"""Define the CloudEndure lambda function.

Attributes:
    LOG_LEVEL (str):
    REGION_OVERRIDE (str): If provided, this value will override the default AWS region.
    logger (logging.Logger):

"""
import datetime
import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

LOG_LEVEL = getattr(logging, os.environ.get('CLOUDENDURE_LOGLEVEL', 'INFO'))
REGION_OVERRIDE = os.environ.get('CLOUDENDURE_REGION_OVERRIDE', '')

logger = logging.getLogger()

logger.setLevel(LOG_LEVEL)


def send_sqs_message(imageinfo):
    """Sends a SQS message with the AMI information
    that was created from the migrated instance
    that passed testing post migration in CloudEndure
    """
    try:
        message = json.dumps(imageinfo)
        sqsclient = boto3.client('sqs')
        sqsclient.send_message(QueueUrl=os.environ['QueueURL'], MessageBody=message)

    except ClientError as err:
        logger.error(err.response)


def create_ami(project_id, instance_id):
    """Create an AMI from the specified instance.

    """
    try:
        _ec2_client = boto3.client('ec2')

        # Create an AMI from the migrated instance
        image_creation_time = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
        ec2_image = _ec2_client.create_image(
            InstanceId=instance_id,
            Name=f"{image_creation_time}",
            Description=f"{project_id} {image_creation_time}",
            NoReboot=True,
        )
        logger.info('AMI Id: %s', ec2_image)
        _filters = [{'Name': 'resource-id', 'Values': [instance_id]}]

        # Tag the newly created AMI by getting the tags of the migrated instance to copy to the AMI.
        ec2_tags = _ec2_client.describe_tags(Filters=_filters)

        logger.info(ec2_tags)
        for tag in ec2_tags['Tags']:
            _ec2_client.create_tags(Resources=[ec2_image['ImageId']], Tags=[{'Key': tag['Key'], 'Value': tag['Value']}])

        send_sqs_message(ec2_image)

    except ClientError as err:
        logger.error(err.response)


def lambda_handler(event, context):
    """Lambda entry point"""
    logger.info(event)

    try:
        json_sns_message = json.loads(event['Records'][0]['Sns']['Message'])

        if json_sns_message['Pass'] != "True":
            logger.error(
                "%s did not pass post migration testing! Not creating an AMI." % (json_sns_message['instanceId'])
            )

        else:
            logger.info("%s passed post migration testing. Creating an AMI." % (json_sns_message['instanceId']))
            create_ami('', json_sns_message['instanceId'])
    except ClientError as err:
        logger.error(err.response)
