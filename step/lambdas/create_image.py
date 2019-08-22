#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict, List
import json
import boto3
import os
import datetime

print("Loading function create_image")

ec2_client = boto3.client("ec2")

# {
#   "original_id": "original id",
#   "account": "account number",
#   "instance_id": "i-aaaaaaa",
#   "instance_status": "running"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    print("Received event: " + json.dumps(event, indent=2))

    instance_id: str = event["instance_id"]

    image_creation_time: str = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

    ec2_image: Dict[str, Any] = ec2_client.create_image(
        InstanceId=instance_id,
        Name=f"{instance_id}-{image_creation_time}",
        Description=f"Created image for {instance_id}",
    )
    _filters: List[Any] = [{"Name": "resource-id", "Values": [instance_id]}]

    # Tag the newly created AMI by getting the tags of the migrated instance to copy to the AMI.
    ec2_tags: Dict[str, Any] = ec2_client.describe_tags(Filters=_filters)

    name: str = instance_id
    for tag in ec2_tags["Tags"]:
        if tag["Key"] == "Name":
            name = tag["Value"]

        ec2_client.create_tags(
            Resources=[ec2_image["ImageId"]],
            Tags=[{"Key": tag["Key"], "Value": tag["Value"]}],
        )

    ec2_client.create_tags(
        Resources=[instance_id], Tags=[{"Key": "CloneStatus", "Value": "IMAGE_CREATED"}]
    )
    ec2_client.delete_tags(
        Resources=[ec2_image["ImageId"]], Tags=[{"Key": "CloneStatus"}]
    )

    return ec2_image["ImageId"]
