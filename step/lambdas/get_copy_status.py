#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Get status of a copy job"""
from __future__ import annotations

import json
from typing import Any, Dict

import boto3

print("Loading function get_copy_status")

ec2_client = boto3.client("ec2")

# {
#   "ami_id": "original AMI",
#   "kms_id": "KMS GUID",
#   "wait_time": timeout in seconds,
#   "copy_ami": "copied AMI",
#   "status": "pending if it came from the copy complete? choice"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: " + json.dumps(event, indent=2))

    copy_ami: str = event["copy_ami"]

    ami_state: Dict[str, Any] = ec2_client.describe_images(ImageIds=[copy_ami])

    return ami_state["Images"][0]["State"]
