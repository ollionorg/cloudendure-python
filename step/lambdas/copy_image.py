#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict
import json
import boto3

print("Loading function copy_image")

ec2_client = boto3.client("ec2")

# {
#     "ami_id" : "ami-123456",
#     "kms_id"   : "GUID",
#     "wait_time": 60
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    print("Received event: " + json.dumps(event, indent=2))

    ami_id: str = event["ami_id"]
    kms_id: str = event["kms_id"]

    new_image: Dict[str, Any] = ec2_client.copy_image(
        SourceImageId=ami_id,
        SourceRegion=os.environ["AWS_REGION"],
        Name=f"copied-{ami_id}",
        Encrypted=True,
        KmsKeyId=kms_id,
    )

    return new_image["ImageId"]
