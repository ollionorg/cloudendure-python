# -*- coding: utf-8 -*-
"""Define Migration events."""
from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Any, Dict, List, Tuple

import boto3


class MigrationStateHandler:
    sqs = None

    def update_state(self, state: str, machine_name: str, **kwargs) -> bool:
        """Send a state update."""
        sqs = boto3.client("sqs")

        print("Event queue: " + os.environ.get("event_queue"))
        queue_url = os.environ.get("event_queue")
        state_obj = MigrationState(state, machine_name, **kwargs)
        print(sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(state_obj.state_dict)))


class MigrationException(Exception):
    """Define the structure of a Migration exception."""

    pass


class MigrationState:
    """Define the structure of a Migration state."""

    state_dict = {}

    # states
    STATE_ERRORED: str = "ERROR"
    STATE_INSTANCE_LAUNCHED: str = "INSTANCE_LAUNCHED"
    STATE_INSTANCE_READY: str = "INSTANCE_READY"
    STATE_IMAGE_CREATING: str = "IMAGE_CREATING"
    STATE_IMAGE_CREATED: str = "IMAGE_CREATED"
    STATE_IMAGE_SHARED: str = "IMAGE_SHARED"
    STATE_IMAGE_COPYING: str = "IMAGE_COPYING"
    STATE_IMAGE_COPIED: str = "IMAGE_COPIED"
    STATE_IMAGE_SPLIT: str = "IMAGE_SPLIT"
    STATE_IMAGE_READY: str = "IMAGE_READY"

    STATES: List[Tuple[str]] = [
        STATE_ERRORED,
        STATE_INSTANCE_LAUNCHED,
        STATE_INSTANCE_READY,
        STATE_IMAGE_CREATING,
        STATE_IMAGE_CREATED,
        STATE_IMAGE_SHARED,
        STATE_IMAGE_COPYING,
        STATE_IMAGE_COPIED,
        STATE_IMAGE_SPLIT,
        STATE_IMAGE_READY,
    ]

    def __init__(self, state: str, machine_name: str = "NA", **kwargs) -> None:
        """Initialize the State."""
        if state not in self.STATES:
            raise MigrationException(f"State: {state} is unrecognized!")

        self.machine_name: str = machine_name.upper()
        self.state: str = state

        self.state_dict: Dict[str, Any] = {
            "state": self.state,
            "machine_name": self.machine_name,
        }

        for k, v in kwargs.items():
            setattr(self, k, v)
            self.state_dict[k] = v
