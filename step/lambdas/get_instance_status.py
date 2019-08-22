#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict, List
import json
import boto3
import os

print("Loading function get_instance_status")

ec2_client = boto3.client("ec2")

# {
#     "instance_id" : "id of project"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    print("Received event: " + json.dumps(event, indent=2))

    instance_id: str = event["instance_id"]

    resp = ec2_client.describe_instance_status(InstanceIds=[instance_id])

    print(resp)

    return "available"
