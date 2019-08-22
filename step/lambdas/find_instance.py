#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict, List
import json
import boto3
import os

print("Loading function find_instance")

ec2_client = boto3.client("ec2")

# {
#     "original_id" : "GUID from cloudendure that identifies the target machine",
#     "account"     : "Account to share the image to"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    print("Received event: " + json.dumps(event, indent=2))

    original_id: str = event["original_id"]

    resp = ec2_client.describe_instances(Filters=[{"Name": "tag:Original id", "Values": [f"{original_id}"]}])

    print(resp)

    return "i-1234"
