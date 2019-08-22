#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict, List
import json
import boto3
import os

print("Loading function share_image")

ec2_res = boto3.resource("ec2")

# {
#     "ami_id" : "ami-123456",
#     "kms_id"   : "GUID",
#     "wait_time": 60
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> bool:
    print("Received event: " + json.dumps(event, indent=2))

    migrated_ami_id: str = event["migrated_ami_id"]
    account: str = event["account"]

    # Access the image that needs to be copied
    image = ec2_res.Image(migrated_ami_id)

    try:
        # Share the image with the destination account
        image.modify_attribute(
            ImageId=image.id,
            Attribute="launchPermission",
            OperationType="add",
            LaunchPermission={"Add": [{"UserId": account}]},
        )
    except Exception as e:
        print(e)
        return False

    # We have to now share the snapshots associated with the AMI so it can be copied
    devices = image.block_device_mappings
    for device in devices:
        if "Ebs" in device:
            snapshot_id: str = device["Ebs"]["SnapshotId"]
            snapshot = ec2_res.Snapshot(snapshot_id)
            try:
                snapshot.modify_attribute(
                    Attribute="createVolumePermission",
                    CreateVolumePermission={"Add": [{"UserId": account}]},
                    OperationType="add",
                )
            except Exception as e:
                print(e)
                return False
    return True
