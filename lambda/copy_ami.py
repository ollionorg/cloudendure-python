# -*- coding: utf-8 -*-
"""Define the CloudEndure lambda function.

Attributes:
    LOG_LEVEL (str):
    REGION_OVERRIDE (str): If provided, this value will override the default AWS region.
    logger (logging.Logger):

"""
import logging
import os

import boto3

logger = logging.getLogger(__name__)

SRC_ACCOUNT_ID = os.environ.get('CLOUDENDURE_SRC_ACCOUNT', '')
DEST_ACCOUNT_ID = os.environ.get('CLOUDENDURE_DEST_ACCOUNT', '')
IMAGE_ID = os.environ.get('CLOUDENDURE_IMAGE_ID', '')
SRC_REGION = os.environ.get('CLOUDENDURE_SRC_REGION', 'us-east-1')
DEST_REGION = os.environ.get('CLOUDENDURE_DEST_REGION', 'us-west-1')
SRC_ROLE_ARN = os.environ.get('CLOUDENDURE_SRC_ROLE_ARN', '')
DEST_ROLE_ARN = os.environ.get('CLOUDENDURE_DEST_ROLE_ARN', '')
SESSION_NAME = os.environ.get('CLOUDENDURE_SESSION_NAME', 'CloudEndureMigration')


def assume_role(sts_role_arn='', session_name=SESSION_NAME):
    sts = boto3.client('sts')

    try:
        credentials = sts.assume_role(RoleArn=sts_role_arn, RoleSessionName=session_name).get('Credentials', {})
    except Exception as e:
        logger.error(
            '%s encountered while attempting to assume the Role ARN: (%s) during (%s)', e, sts_role_arn, session_name
        )

    if not credentials:
        logger.error('Unable to assume role via STS! Please check permissions and try again.')

    return credentials


def get_ec2(credentials, region=''):
    ec2 = None

    # Copy image to failover regions
    try:
        ec2 = boto3.client(
            'ec2',
            region,
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken'],
        )
    except Exception as e:
        logger.error(e)

    return ec2


def share_image(image_name='CloudEndureImage'):
    src_credentials = assume_role(SRC_ROLE_ARN)
    src_ec2 = get_ec2(src_credentials, region=SRC_REGION)

    # Access the image that needs to be copied
    image = src_ec2.Image(IMAGE_ID)

    # Share the image with the destination account
    image.modify_attribute(
        ImageId=image.id,
        Attribute='launchPermission',
        OperationType='add',
        LaunchPermission={'Add': [{
            'UserId': DEST_ACCOUNT_ID
        }]}
    )

    # We have to now share the snapshots associated with the AMI so it can be copied
    devices = image.block_device_mappings
    for device in devices:
        if 'Ebs' in device:
            snapshot_id = device['Ebs']['SnapshotId']
            snapshot = src_ec2.Snapshot(snapshot_id)
            snapshot.modify_attribute(
                Attribute='createVolumePermission',
                CreateVolumePermission={'Add': [{'UserId': DEST_ACCOUNT_ID}]},
                OperationType='add',
            )

    # Access destination account so we can now copy the image
    dest_credentials = assume_role(DEST_ROLE_ARN)
    # Copy image to failover regions
    dest_ec2 = get_ec2(dest_credentials, region=DEST_REGION)

    # Copy the shared AMI to dest region
    try:
        dest_ec2.copy_image(Name=image_name, SourceImageId=image.id, SourceRegion=SRC_REGION)
    except Exception as e:
        logger.error(e)
