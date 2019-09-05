#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AWS Lambda to create an AWS image."""
from __future__ import annotations

import datetime
import json
from typing import Any, Dict

import boto3

print("Loading function create_image")

ec2_resource = boto3.resource("ec2")

# {
#   "instance_id": "i-identifier",
#   "kms_id": "KMS ID",
#   "account": "account_number",
#   "instance_status": "should be there if in loop"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: " + json.dumps(event, indent=2))

    instance_id: str = event["instance_id"]

    image_creation_time: str = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

    instance = ec2_resource.Instance(instance_id)

    ec2_image = instance.create_image(
        Name=f"{instance_id}-{image_creation_time}",
        Description=f"Created image for {instance_id}",
    )

    for tag in instance.tags:
        ec2_image.create_tags(Tags=[{"Key": tag["Key"], "Value": tag["Value"]}])

    instance.create_tags(Tags=[{"Key": "CloneStatus", "Value": "IMAGE_CREATED"}])

    return ec2_image.image_id
