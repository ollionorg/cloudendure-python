#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check the status of an AWS EC2 instance."""
from __future__ import annotations

import json
from typing import Any, Dict

import boto3
from migrationstate import MigrationStateHandler

print("Loading function get_instance_status")

ec2_client = boto3.client("ec2")

# {
#   "instance_id": "i-identifier",
#   "kms_id": "KMS ID",
#   "account": "account_number",
#   "instance_status": "should be there if in loop"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: " + json.dumps(event, indent=2))

    instance_id: str = event.get("instance_id")
    instance_name: str = event.get("name", "")
    state: str = "unknown"

    resp = ec2_client.describe_instances(InstanceIds=[instance_id])
    reservations = resp.get("Reservations", [])
    for reservation in reservations:
        for instance in reservation.get("Instances", []):
            state = instance.get("State", {}).get("Name")

            # check if running
            if state == "running":
                resp = ec2_client.describe_instance_status(InstanceIds=[instance_id])
                status = resp.get("InstanceStatuses", [])[0]

                # check instance
                if status["InstanceStatus"].get("Status", "") != "ok":
                    state = "instance_failed"

                # check system
                if status["SystemStatus"].get("Status", "") != "ok":
                    state = "system_failed"

    if state == "running":
        MigrationStateHandler().update_state(state="INSTANCE_READY", machine_name=instance_name)

    return state
