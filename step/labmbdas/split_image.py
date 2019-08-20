#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Split a copied image"""
import json
import boto3

from __future__ import annotations
from typing import Any, Dict, List

print("Loading function split_image")

ec2_res = boto3.resource("ec2", AWS_REGION)

# {
#     "copy_ami" : "ami-123456",
#     "kms_id"   : "GUID",
#     "wait_time": 60
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    print("Received event: " + json.dumps(event, indent=2))

    copy_ami: str = event["copy_ami"]

    print("Loading EC2 resource for region: ", AWS_REGION)

    # Access the image that needs to be split
    image = ec2_res.Image(copy_ami)

    root_drive: Dict[str, Any] = {}
    drives: Dict[str, Any] = {}

    # separate the root drive from the other drives
    devices: List[Any] = image.block_device_mappings
    for device in devices:
        if "Ebs" in device:
            if device["DeviceName"] == image.root_device_name:
                print(f"Found Root! {device}")
                root_drive: Dict[str, Any] = device
            else:
                drives[device["DeviceName"]] = device["Ebs"]

    # have to remove the encrypted flag
    del root_drive["Ebs"]["Encrypted"]

    # create a new AMI with only the root
    response = ec2_res.register_image(
        Architecture=image.architecture,
        BlockDeviceMappings=[root_drive],
        Name=f"root-{copy_ami}",
        RootDeviceName=image.root_device_name,
        VirtualizationType=image.virtualization_type,
    )

    root_ami = response.id

    for drive in drives:
        print(drives[drive])
        ec2_res.create_tags(
            Resources=[root_ami],
            Tags=[{"Key": f"Drive-{drive}", "Value": json.dumps(drives[drive])}],
        )

    return root_ami
