#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict, List
import json
import boto3

print("Loading function find_instance")

ec2_client = boto3.client("ec2")

# {
#     "original_id" : "GUID from cloudendure that identifies the target machine",
#     "account"     : "Account to share the image to"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    print("Received event: " + json.dumps(event, indent=2))

    original_id: str = event["original_id"]
    instance_id: str = ""

    resp = ec2_client.describe_instances(
        Filters=[{"Name": "tag:Original id", "Values": [f"{original_id}"]}]
    )
    for reservation in resp.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            if instance["State"].get("Name") == "running":
                instance_id = instance.get("InstanceId", "")

    return instance_id
