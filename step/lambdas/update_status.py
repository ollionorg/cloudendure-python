#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AWS Lambda to read from a SQS queue and pass the information to service now."""
from __future__ import annotations

import json
import os
from typing import Any, Dict

import boto3

print("Loading function update_status")


def lambda_handler(event: Dict[str, Any], context: Any) -> bool:
    """Handle signaling and entry into the AWS Lambda."""
    print("Received event: ", json.dumps(event, indent=2))

    for record in event["Records"]:
        payload = record["body"]
        print(str(payload))

    return True
