#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find the passed in instance id and see if it is a CE migration"""
from __future__ import annotations

import json
from typing import Any, Dict

import boto3

print("Loading function find_instance")

ec2_resource = boto3.resource("ec2")

# {
#   "version": "0",
#   "id": "7e979767-95bb-1972-0cab-a670ec5d5000",
#   "detail-type": "EC2 Instance State-change Notification",
#   "source": "aws.ec2",
#   "account": "460535642604",
#   "time": "2019-08-23T13:45:28Z",
#   "region": "us-east-1",
#   "resources": [
#     "arn:aws:ec2:us-east-1:460535642604:instance/i-00c758f34483a2ea2"
#   ],
#   "detail": {
#     "instance-id": "i-00c758f34483a2ea2",
#     "state": "running"
#   }
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: " + json.dumps(event, indent=2))

    detail: Dict[str, Any] = event.get("detail", {})
    event_dict: Dict[str, Any] = {}
    instance_id: str = detail.get("instance-id", "")

    if not instance_id:
        event_dict["instance_id"] = "not-found"
        return event_dict

    try:
        instance = ec2_resource.Instance(instance_id)

        # look for tags that show it is a CE migration that has not run yet
        for tag in instance.tags:
            if tag["Key"] == "CloneStatus":
                if tag["Value"] == "NOT_STARTED":
                    event_dict["instance_id"] = instance_id
                else:
                    event_dict["instance_id"] = "not-migration"

            if tag["Key"] == "DestinationAccount":
                event_dict["account"] = tag["Value"]

            if tag["Key"] == "DestinationKMS":
                event_dict["kms_id"] = tag["Value"]

            if tag["Key"] == "DestinationRole":
                event_dict["role"] = tag["Value"]

    except Exception as e:
        print(e)
        event_dict["instance_id"] = "not-found"

    return event_dict
