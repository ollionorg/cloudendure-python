#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict, List
import json
import boto3
import os

print("Loading function image_cleanup")

ec2_client = boto3.client("ec2")

# {
#   "ami_id": "original AMI",
#   "kms_id": "KMS GUID used for copy and split AMI",
#   "wait_time": wait time in seconds,
#   "copy_ami": "copied AMI",
#   "split_ami_id": split AMI if it passed"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> bool:
    print("Received event: " + json.dumps(event, indent=2))

    copy_ami: str = event.get("copy_ami")
    if not copy_ami:
        return ""

    ec2_client.deregister_image(ImageId=copy_ami)

    return True
