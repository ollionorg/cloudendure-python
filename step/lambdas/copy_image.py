#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AWS Lambda to copy an AWS image."""
from __future__ import annotations

import json
import os
from typing import Any, Dict

import boto3

print("Loading function copy_image")

# {
#     "ami_id"    : "ami-123456",
#     "kms_id"    : "GUID",
#     "wait_time" : 60,
#     "region"    : "optional destination region"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: " + json.dumps(event, indent=2))

    migrated_ami_id: str = event["migrated_ami_id"]
    kms_id: str = event["kms_id"]
    region: str = event.get("region", os.environ.get("AWS_REGION"))
    ec2_client = boto3.client("ec2", region)

    try:
        new_image: Dict[str, Any] = ec2_client.copy_image(
            SourceImageId=migrated_ami_id,
            SourceRegion=region,
            Name=f"copied-{migrated_ami_id}",
            Encrypted=True,
            KmsKeyId=kms_id,
        )
    except Exception as e:
        print(e)
        return ""

    return new_image.get("ImageId", "")
