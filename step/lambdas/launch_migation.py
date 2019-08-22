#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict, List
import json
import boto3
import os

from requests.models import Response
from .api import CloudEndureAPI
from .config import CloudEndureConfig
from .events import Event, EventHandler
from .exceptions import CloudEndureHTTPException

print("Loading function launch_migration")

ec2_client = boto3.client("ec2")

# {
#     "project_id" : "id of project"
#     "machine_id" : "id of the machine to migrate",
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """Launch the test target instances."""
    print("Received event: " + json.dumps(event, indent=2))

    project_id: str = event["project_id"]
    machine_id: str = event["machine_id"]

    api: CloudEndureAPI = CloudEndureAPI()
    api.login()
    event_handler: EventHandler = EventHandler()
    # if dry_run:
    #     print("This is a dry run! Not launching any machines!")
    #     return False

    machines_response: Response = self.api.api_call(
        f"projects/{project_id}/machines/{machine_id}"
    )
    if machine.get("replica"):
        print("Target machine already launched")
        event_handler.add_event(Event.EVENT_ALREADY_LAUNCHED, machine_name=_machine)

    for _machine in self.target_machines:
        for machine in json.loads(machines_response.text).get("items", []):
            source_props: Dict[str, Any] = machine.get("sourceProperties", {})
            machine_data: Dict[str, Any] = {}
            if _machine == source_props.get("name", "NONE"):
                if machine.get("replica"):
                    print("Target machine already launched")
                    self.event_handler.add_event(
                        Event.EVENT_ALREADY_LAUNCHED, machine_name=_machine
                    )
                    continue
                if launch_type == "test":
                    machine_data = {
                        "items": [{"machineId": machine["id"]}],
                        "launchType": "TEST",
                    }
                elif launch_type == "cutover":
                    machine_data = {
                        "items": [{"machineId": machine["id"]}],
                        "launchType": "CUTOVER",
                    }

            if machine_data:
                result: Response = self.api.api_call(
                    f"projects/{project_id}/launchMachines",
                    method="post",
                    data=json.dumps(machine_data),
                )
                if result.status_code == 202:
                    if launch_type == "test":
                        print("Test Job created for machine ", _machine)
                        self.event_handler.add_event(
                            Event.EVENT_SUCCESSFULLY_LAUNCHED, machine_name=_machine
                        )
                    elif launch_type == "cutover":
                        print("Cutover Job created for machine ", _machine)
                        self.event_handler.add_event(
                            Event.EVENT_SUCCESSFULLY_CUTOVER, machine_name=_machine
                        )
                elif result.status_code == 409:
                    print(f"ERROR: ({_machine}) is currently in progress!")
                    self.event_handler.add_event(
                        Event.EVENT_IN_PROGRESS, machine_name=_machine
                    )
                elif result.status_code == 402:
                    print("ERROR: Project license has expired!")
                    self.event_handler.add_event(
                        Event.EVENT_EXPIRED, machine_name=_machine
                    )
                else:
                    print("ERROR: Launch target machine failed!")
                    self.event_handler.add_event(
                        Event.EVENT_FAILED, machine_name=_machine
                    )
            else:
                print(
                    f"Machine: ({source_props['name']}) - Not a machine we want to launch..."
                )
                self.event_handler.add_event(Event.EVENT_IGNORED, machine_name=_machine)
    return True
