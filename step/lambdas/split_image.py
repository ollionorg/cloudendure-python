#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AWS Lambda to split a copied image."""
from __future__ import annotations

import json
import os
from typing import Any, Dict, List

import boto3

print("Loading function split_image")

# {
#     "copy_ami" : "ami-123456",
#     "kms_id"   : "GUID",
#     "wait_time": 60,
#     "region"   : optional region
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: " + json.dumps(event, indent=2))

    copy_ami: str = event["copy_ami"]
    region: str = event.get("region", os.environ.get("AWS_REGION"))
    role: str = event.get("role")

    sts_client = boto3.client("sts")

    print(f"Assuming role: {role}")
    assumed_role: Dict[str, Any] = sts_client.assume_role(
        RoleArn=role, RoleSessionName="SplitImageLambda"
    )

    credentials = assumed_role.get("Credentials")

    ec2_res = boto3.resource(
        "ec2",
        region_name=region,
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )

    try:
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

        # clean up original image
        image.deregister()
    except Exception as e:
        print(e)
        return ""

    return root_ami
