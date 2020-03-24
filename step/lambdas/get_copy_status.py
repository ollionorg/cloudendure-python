#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check the status of an AWS AMI copy."""
from __future__ import annotations

import json
import os
from typing import Any, Dict

import boto3
from migrationstate import MigrationStateHandler

print("Loading function get_copy_status")

# {
#   "ami_id": "original AMI",
#   "kms_id": "KMS GUID",
#   "wait_time": timeout in seconds,
#   "copy_ami": "copied AMI",
#   "status": "pending if it came from the copy complete? choice"
#   "region": "different region"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: " + json.dumps(event, indent=2))

    copy_ami: str = event["copy_ami"]
    region: str = event.get("region", os.environ.get("AWS_REGION"))
    instance_name: str = event.get("name", "")
    role: str = event.get("role", "")

    sts_client = boto3.client("sts")

    print(f"Assuming role: {role}")
    assumed_role: Dict[str, Any] = sts_client.assume_role(RoleArn=role, RoleSessionName="GetCopyStatusLambda")

    credentials = assumed_role.get("Credentials")

    ec2_client = boto3.client(
        "ec2",
        region_name=region,
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )

    try:
        ami_state: Dict[str, Any] = ec2_client.describe_images(ImageIds=[copy_ami])
    except Exception as e:
        print(e)
        return "error"

    images = ami_state.get("Images")
    if not images:
        return "no-image-yet"

    state = images[0].get("State")
    if state and state == "available":
        MigrationStateHandler().update_state(state="IMAGE_COPIED", machine_name=instance_name)

    return state
