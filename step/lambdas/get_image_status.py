#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations

import json
from typing import Any, Dict

import boto3

print("Loading function get_image_status")

ec2_client = boto3.client("ec2")

# {
#   "original_id": "original id",
#   "account": "account id",
#   "instance_id": "i-aaaaaa",
#   "instance_status": "running",
#   "migrated_ami_id": "ami-123456"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: " + json.dumps(event, indent=2))

    migrated_ami_id: str = event["migrated_ami_id"]

    ami_state: Dict[str, Any] = ec2_client.describe_images(ImageIds=[migrated_ami_id])

    return ami_state["Images"][0]["State"]
