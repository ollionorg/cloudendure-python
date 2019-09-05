#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AWS Lambda to cleanup AWS images."""
from __future__ import annotations

import json
import os
from typing import Any, Dict, List

import boto3

print("Loading function image_cleanup")

# {
#   "ami_id": "original AMI",
#   "kms_id": "KMS GUID used for copy and split AMI",
#   "wait_time": wait time in seconds,
#   "copy_ami": "copied AMI",
#   "split_ami_id": split AMI if it passed"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> bool:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: " + json.dumps(event, indent=2))

    migrated_ami: str = event.get("migrated_ami_id")
    if not migrated_ami:
        return False

    ec2_res = boto3.resource("ec2", os.environ.get("AWS_REGION"))
    try:
        # Access the image that needs to be deleted
        image = ec2_res.Image(migrated_ami)

        # grab device mappings before deregistering
        devices: List[Any] = image.block_device_mappings
        image.deregister()
        for device in devices:
            if "Ebs" in device:
                snap = ec2_res.Snapshot(device["Ebs"].get("SnapshotId"))
                snap.delete()
    except Exception as e:
        print(f"Failed.  AMI may not exist.\n{str(e)}")
        return False

    return True
