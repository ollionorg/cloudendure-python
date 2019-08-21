#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict, List
import json
import boto3
import os

print("Loading function image_cleanup")

ec2_res = boto3.resource("ec2")

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

    # Access the image that needs to be removed
    image = ec2_res.Image(copy_ami)
    devices: List[Any] = image.block_device_mappings
    image.deregister()

    for device in devices:
        if "Ebs" in device:
            ec2_res.delete_snapshot(SnapshotId=device["Ebs"]["SnapshotId"])

    return True
