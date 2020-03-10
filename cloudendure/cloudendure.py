#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Define the CloudEndure main entry logic."""
from __future__ import annotations

import base64
import datetime
import json
import os
from typing import Any, Dict, List

import boto3
import fire
from botocore import client as boto_client
from botocore.exceptions import ClientError
from requests.models import Response

from .api import CloudEndureAPI
from .config import CloudEndureConfig
from .constants import get_aws_regions
from .events import Event, EventHandler
from .exceptions import CloudEndureHTTPException, CloudEndureMisconfigured
from .templates import TerraformTemplate

HOST: str = "https://console.cloudendure.com"
headers: Dict[str, str] = {"Content-Type": "application/json"}
session: Dict[str, str] = {}
AWS_REGION: str = os.environ.get("AWS_REGION", "")


class CloudEndure:
    """Define the CloudEndure general object."""

    def __init__(
        self,
        project_name: str = "",
        dry_run: bool = False,
        username: str = "",
        password: str = "",
        token: str = "",
    ) -> None:
        """Initialize the CloudEndure object.

        This entrypoint is primarily for use with the CLI.

        """
        self.config: CloudEndureConfig = CloudEndureConfig(
            username=username, password=password, token=token
        )
        self.api: CloudEndureAPI = CloudEndureAPI(self.config)
        self.is_authenticated = self.api.login()

        # Determine the active project ID.
        self.project_id = self.config.active_config.get("project_id", "")

        # Determine the active project name.
        self.project_name: str = self.config.active_config.get("project_name", "")
        if project_name and project_name != self.project_name:
            self.project_name = project_name

        if not self.project_id or (project_name and project_name != self.project_name):
            self.project_id: str = self.get_project_id(project_name=self.project_name)

        self.dry_run = dry_run
        self.event_handler: EventHandler = EventHandler()
        self.destination_account: str = self.config.active_config.get(
            "destination_account", ""
        )
        self.destination_kms: str = self.config.active_config.get("destination_kms", "")
        self.destination_role: str = self.config.active_config.get(
            "destination_role", ""
        )
        self.subnet_id: str = self.config.active_config.get("subnet_id", "")
        self.private_ip_action: str = self.config.active_config.get(
            "private_ip_action", ""
        )
        if self.subnet_id and not self.private_ip_action:
            self.private_ip_action = "CREATE_NEW"
        self.security_group_id: str = self.config.active_config.get(
            "security_group_id", ""
        )
        self.target_machines: List[str] = self.config.active_config.get(
            "machines", ""
        ).split(",")
        self.target_instance_types: List[str] = self.config.active_config.get(
            "instance_types", ""
        ).split(",")
        if len(self.target_machines) == len(self.target_instance_types):
            self.target_instances: Dict[str, str] = dict(
                zip(self.target_machines, self.target_instance_types)
            )
        else:
            print(
                "WARNING: Misconfiguration of CLOUDENDURE_INSTANCE_TYPES and CLOUDENDURE_MACHINES.  These should be the same length!"
            )
            self.target_instances = {}

        self.lagging_machines: List[str] = []
        self.ready_machines: List[str] = []
        self.nonexistent_machines: List[str] = []
        self.launched_machines: List[str] = []
        self.migration_wave: str = self.config.active_config.get("migration_wave", "0")
        self.max_lag_ttl: int = self.config.active_config.get("max_lag_ttl", 90)

        if not self.is_authenticated:
            print(
                "Failed to authenticate with CloudEndure! Please check your credentials and try again!"
            )

    def _get_role_credentials(self, name: str, role: str) -> Dict[str, Any]:
        _sts_client: boto_client = boto3.client("sts")

        print(f"Assuming role: {role}")
        assumed_role: Dict[str, Any] = _sts_client.assume_role(
            RoleArn=self.destination_role, RoleSessionName=name
        )
        return assumed_role.get("Credentials", {})

    def get_project_id(self, project_name: str = "") -> str:
        """Get the associated CloudEndure project ID by project_name.

        Args:
            project_name (str): The name of the CloudEndure project.

        Exceptions:
            Exception: Currently catch all encountered exceptions while traversing
                the project list API call.

        Returns:
            str: The CloudEndure project UUID.

        """
        if not self.is_authenticated:
            return ""

        print(f"Active Project Name: {project_name}")
        if self.project_name and self.project_name == project_name:
            return self.project_id

        if not self.project_name and not project_name:
            print(
                "No project name provided! Please add a project_name to the configuration and re-run!"
            )
            raise CloudEndureMisconfigured()

        if not project_name:
            project_name: str = self.project_name

        print("No project ID for the provided project name!\nFetching project ID...\n")
        projects_result: Response = self.api.api_call("projects")
        if projects_result.status_code != 200:
            print("Failed to fetch the project!")
            return ""

        try:
            # Get Project ID
            projects: List[Any] = json.loads(projects_result.text).get("items", [])
            found_project: Dict[Any, Any] = next(
                (item for item in projects if item.get("name", "NONE") == project_name),
                {},
            )
            project_id: str = found_project.get("id", "")
        except Exception as e:
            print(f"Exception: {str(e)}")
            return ""
        return project_id

    def get_cloud(self, cloud_type: str = "") -> str:
        """Get the ID for the specified cloud type."""
        if not cloud_type:
            cloud_type = self.config.active_config.get("cloud_type", "AWS")

        clouds_result: Response = self.api.api_call("clouds")
        for cloud in json.loads(clouds_result.content)["items"]:
            if cloud.get("name", "") == cloud_type:
                return cloud.get("id", "")
        return ""

    def create_cloud_credentials(
        self, access_key: str = "", secret_key: str = ""
    ) -> str:
        """Create a new CloudEndure project.

        Args:
            project_name (str): The name of the CloudEndure project to be created.

        Returns:
            str: The newly created CloudEndure project ID.

        """
        _encoded_private_key = base64.b64encode(secret_key.encode())
        _project = {
            "accountIdentifier": "",
            "publicKey": access_key,
            "privateKey": _encoded_private_key,
            "cloudId": self.get_cloud(),
        }

        cloud_cred_result: Response = self.api.api_call(
            "cloudCredentials", method="post", data=_project
        )
        if cloud_cred_result.status_code != 201:
            print(
                f"Failed to create the new cloud credentials: ({access_key}): "
                f"{cloud_cred_result.status_code} {cloud_cred_result.content}"
            )
            return ""
        print(f"Cloud Credentials: ({access_key}) was created successfully!")
        return json.loads(cloud_cred_result.content).get("id", "")

    def create_repl_config(self, region: str = "", cloud_cred_id: str = ""):
        """Create a CloudEndure project replication configuration.

        Args:
            project_name (str): The name of the CloudEndure project to get replication configurations for.

        Returns:
            list of dict: The CloudEndure replication configuration dictionary mapping.

        """
        regions = get_aws_regions()
        payload = {
            # "archivingEnabled": False,
            "bandwidthThrottling": 0,
            # "cloudCredentials": "",
            # "id": "",
            # "objectStorageLocation": "",
            # "proxyUrl": "",
            # "region": "",
            "replicationServerType": "Default",
            "replicationTags": [],
            # "replicatorSecurityGroupIDs": [],
            # "subnetHostProject": "",
            # "subnetId": "",
            "useDedicatedServer": False,
            "useLowCostDisks": False,
            "usePrivateIp": True,
            "volumeEncryptionAllowed": False,
            # "volumeEncryptionKey": ""
        }

        credentials_response: Response = self.api.api_call(
            f"cloudCredentials/{cloud_cred_id}/regions"
        )
        for _region in json.loads(credentials_response.content).get("items", []):
            if _region["name"] == regions.get(region, "N/A"):
                payload["region"] = _region["id"]

        print(payload)
        repl_result: Response = self.api.api_call(
            f"projects/{self.project_id}/replicationConfigurations",
            method="post",
            data=payload,
        )
        if repl_result.status_code != 201:
            print(
                f"Failed to create replication configuration {repl_result.status_code} {repl_result.content}"
            )
            return ""
        print("Replication configuration was created successfully")
        return json.loads(repl_result.content).get("id", "")

    def get_repl_configs(self) -> List[Any]:
        """Get a CloudEndure project's replication configurations.

        Args:
            project_name (str): The name of the CloudEndure project to get replication configurations for.

        Returns:
            list of dict: The CloudEndure replication configuration dictionary mapping.

        """
        print(
            f"Fetching Replication Configuration - Project Name: ({self.project_name})"
        )
        repl_config_results: Response = self.api.api_call(
            f"projects/{self.project_id}/replicationConfigurations"
        )

        if repl_config_results.status_code != 200:
            print(
                f"Failed to fetch replication configurations for ({self.project_name}): "
                f"{repl_config_results.status_code} {repl_config_results.content}"
            )
            print(repl_config_results.text)
            return []

        repl_configs = json.loads(repl_config_results.content).get("items", [])
        print(
            f"Successfully fetched replication configurations for project: {self.project_name}"
        )
        return repl_configs

    def create_project(self, project_name: str) -> str:
        """Create a new CloudEndure project.

        Args:
            project_name (str): The name of the CloudEndure project to be created.

        Returns:
            str: The newly created CloudEndure project ID.

        """
        project = {
            "licensesIDs": [],
            "name": project_name,
            "targetCloudId": self.get_cloud(),
            "type": "MIGRATION",
        }
        licenses_result: Response = self.api.api_call("licenses")

        for license in json.loads(licenses_result.content).get("items", []):
            license_id = license.get("id", "")
            if license_id:
                print(license_id)
                project["licensesIDs"].append(license_id)

        projects_result: Response = self.api.api_call(
            "projects", method="post", data=project
        )
        if projects_result.status_code != 201:
            print(
                f"Failed to create the new project ({self.project_name}): "
                f"{projects_result.status_code} {projects_result.content}"
            )
            return ""
        print(f"Project: ({self.project_name}) was created successfully!")
        return json.loads(projects_result.content).get("id", "")

    def update_project(self, project_data: Dict[str, Any] = None) -> bool:
        """Update a CloudEndure project.

        Args:
            project_name (str): The name of the CloudEndure project to be updated.
            project_data (dict): The project payload to be used to update the project.
                Defaults to the current project state.

        Returns:
            bool: Whether or not the project has been updated.

        """
        print(f"Updating Project - Name: ({self.project_name})")
        projects_result: Response = self.api.api_call(
            f"projects/{self.project_id}", method="patch", data=project_data
        )

        if projects_result.status_code != 200:
            print(
                f"Failed to update the project ({self.project_name}): "
                f"{projects_result.status_code} {projects_result.content}"
            )
            print(projects_result.text)
            return False
        print("Project was updated successfully")
        return True

    def check(self) -> bool:
        """Check the status of machines in the provided project."""
        print(
            f"Checking Project - Name: ({self.project_name}) - Dry Run: ({self.dry_run})"
        )

        projects_response: Response = self.api.api_call("projects")

        if projects_response.status_code != 200:
            print("Failed to fetch the project!")
            raise CloudEndureHTTPException("Failed to fetch the CloudEndure Project!")

        machine_status: int = 0
        machines_response: Response = self.api.api_call(
            f"projects/{self.project_id}/machines"
        )

        for _machine in self.target_machines:
            machine_exist: bool = False
            for machine in json.loads(machines_response.text).get("items", []):
                source_props: Dict[str, Any] = machine.get("sourceProperties", {})
                ref_name: str = source_props.get("name") or source_props.get(
                    "machineCloudId", "NONE"
                )
                if _machine == source_props.get(
                    "name", "NONE"
                ) or _machine == source_props.get("machineCloudId", "NONE"):
                    machine_exist = True

                    if "lastConsistencyDateTime" not in machine["replicationInfo"]:
                        print(
                            f"{ref_name} replication into the migration account in progress!"
                        )
                    else:
                        replica: str = machine.get("replica")
                        if replica:
                            machine_status += 1
                            print(
                                f"{ref_name} has been launched in the migration account: {replica}"
                            )
                        else:
                            print(
                                f"{ref_name} has not been launched or is preparing launch in the migration account"
                            )

            if not machine_exist:
                print(f"ERROR: Machine: {_machine} does not exist!")

        if machine_status == len(self.target_machines):
            print(
                "All machines specified in CLOUDENDURE_MACHINES have been launched in the migration account"
            )
        else:
            print(
                "Some machines have not yet completed launching in the migration account"
            )
        return True

    def update_encryption_key(self, kms_id: str) -> bool:
        """Update encryption keys for replication.

        Warning: This will cause re-sync if key does not match!

        Args:
            kms_id (str): The AWS KMD ID to update the project to use.
            project_name (str): The name of the CloudEndure project to be updated.
            dry_run (bool): Whether or not this execution should be a dry run,
                making no actual changes to CloudEndure for validation purposes.

        Returns:
            bool: Whether or not the encryption key was updated.

        """
        print(
            f"Updating Encryption Key - Name: ({self.project_name}) - KMS ID: ({kms_id}) - Dry Run: ({self.dry_run})"
        )

        machines_response: Response = self.api.api_call(
            f"projects/{self.project_id}/machines"
        )
        for machine in json.loads(machines_response.text).get("items", []):
            source_props: Dict[str, Any] = machine.get("sourceProperties", {})
            name: str = source_props.get("name")
            machine_id: str = machine.get("id")
            replication_config: Dict[str, Any] = machine.get(
                "replicationConfiguration", {}
            )

            if replication_config.get("volumeEncryptionKey") == kms_id:
                print(f"Key matches {name}")
                continue

            if self.dry_run:
                print(f"DRY RUN - Not updating key for {name} - DRY RUN")
                continue

            replication_config["volumeEncryptionKey"] = kms_id
            endpoint: str = f"projects/{self.project_id}/machines/{machine_id}"
            print(f"sending to {endpoint}")
            result: Response = self.api.api_call(
                endpoint, method="patch", data=json.dumps(machine)
            )

            if result.status_code != 200:
                print(
                    f"Key update failure encountered for machine: {name} - {result.status_code}\n{result.json()}"
                )
            else:
                print(f"Key updated for or machine: {name}")

        return True

    def check_licenses(self) -> Dict[str, Any]:
        """Check licenses for all available instances in a given project."""
        response_dict: Dict[str, Any] = {}
        print(
            f"Checking CloudEndure Licenses - Name: ({self.project_name})"
        )

        now: datetime = datetime.datetime.now(datetime.timezone.utc)
        expirationday: timedelta = datetime.timedelta(days=90)
        expirationwarn: timedelta = datetime.timedelta(days=60)
        machine_data_dict: Dict[str, Any] = {}
        machines_response: Response = self.api.api_call(
            f"projects/{self.project_id}/machines"
        )
        for machine in json.loads(machines_response.text).get("items", []):
            source_props: Dict[str, Any] = machine.get("sourceProperties", {})
            machine_id: str = machine.get("id")
            machine_name: str = source_props.get("name")
            license_data: Dict[str, Any] = machine.get("license", {})
            license_use: str = license_data.get("startOfUseDateTime")
            license_date: datetime = datetime.datetime.strptime(license_use, '%Y-%m-%dT%H:%M:%S.%f%z')
            delta: timedelta = now - license_date
            if(expirationday < delta):
                response_dict[machine_name] = { "machine_id" : machine_id, "status" : "expired", "delta_days" : delta.days}
            elif(expirationwarn < delta):
                response_dict[machine_name] = { "machine_id" : machine_id, "status" : "warn", "delta_days" : delta.days}

        return response_dict
                
    def update_blueprint(self) -> bool:
        """Update the blueprint associated with the specified machines."""
        print(
            f"Updating CloudEndure Blueprints - Name: ({self.project_name}) - Dry Run: ({self.dry_run})"
        )

        machine_data_dict: Dict[str, Any] = {}
        machines_response: Response = self.api.api_call(
            f"projects/{self.project_id}/machines"
        )
        for machine in json.loads(machines_response.text).get("items", []):
            source_props: Dict[str, Any] = machine.get("sourceProperties", {})
            machine_id: str = machine.get("id")
            machine_name: str = source_props.get("name")
            if (
                machine_name in self.target_machines
                or machine_name.upper() in self.target_machines
            ):
                machine_data_dict[machine_id] = machine_name

        if not machine_data_dict:
            print("No Machines Found!")
            return False
        try:
            blueprints_response = self.api.api_call(
                f"projects/{self.project_id}/blueprints"
            )
            for blueprint in json.loads(blueprints_response.text).get("items", []):
                _machine_id: str = blueprint.get("machineId", "")
                _machine_name: str = machine_data_dict.get(_machine_id, "")
                if not _machine_name:
                    continue

                _blueprint_id: str = blueprint.get("id", "")
                _endpoint: str = f"projects/{self.project_id}/blueprints/{_blueprint_id}"
                # Handle disk blueprints since we don't want provisioned IOPS $$$$
                new_disks = []
                for disk in blueprint["disks"]:
                    new_disks.append(
                        {
                            "type": self.config.active_config.get("disk_type", "SSD"),
                            "name": disk.get("name", ""),
                        }
                    )
                blueprint["disks"] = new_disks

                if self.subnet_id:
                    # Update launch subnets and SG IDs
                    blueprint["subnetIDs"] = [self.subnet_id]
                if self.private_ip_action:
                    blueprint["privateIPAction"] = self.private_ip_action
                if self.security_group_id:
                    blueprint["securityGroupIDs"] = [self.security_group_id]

                instance_type = self.target_instances.get(_machine_name, "")
                if instance_type:
                    blueprint["instanceType"] = instance_type

                # Update machine tags
                blueprint["tags"] = [
                    {
                        "key": "CloneStatus",
                        "value": self.config.active_config.get(
                            "clone_status", "NOT_STARTED"
                        ),
                    },
                    {"key": "MigrationWave", "value": self.migration_wave},
                    {"key": "DestinationAccount", "value": self.destination_account},
                    {"key": "DestinationKMS", "value": self.destination_kms},
                    {"key": "DestinationRole", "value": self.destination_role},
                ]

                blueprint["publicIPAction"] = self.config.active_config.get(
                    "public_ip", "DONT_ALLOCATE"
                )
                if self.dry_run:
                    print("This is a dry run! Not updating blueprints!")
                    return True
                result: Response = self.api.api_call(
                    _endpoint, method="patch", data=json.dumps(blueprint)
                )

                if result.status_code != 200:
                    print(
                        "Blueprint update failure encountered for machine:",
                        f"({_machine_name}) - {result.status_code} fix blueprint settings!",
                    )
                    print(blueprint)
                else:
                    print("Blueprint for machine: " + _machine_name + " updated!")
        except Exception as e:
            print(f"Updating blueprint task failed! {e}")
            return False
        return True

    def launch(self) -> Dict[str, Any]:
        """Launch the test target instances."""
        response_dict: Dict[str, Any] = {}

        print(
            f"Launching Project - Name: ({self.project_name}) - Dry Run: ({self.dry_run})"
        )

        if self.dry_run:
            print("This is a dry run! Not launching any machines!")
            return response_dict

        machines_response: Response = self.api.api_call(
            f"projects/{self.project_id}/machines"
        )
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
                    machine_data = {
                        "items": [{"machineId": machine["id"]}],
                        "launchType": "TEST",
                    }

                if machine_data:
                    result: Response = self.api.api_call(
                        f"projects/{self.project_id}/launchMachines",
                        method="post",
                        data=json.dumps(machine_data),
                    )
                    if result.status_code == 202:
                        response_dict["original_id"] = source_props.get(
                            "machineCloudId", "NONE"
                        )
                        response_dict.update(json.loads(result.text))
                        print("Test Job created for machine ", _machine)
                        self.event_handler.add_event(
                            Event.EVENT_SUCCESSFULLY_LAUNCHED, machine_name=_machine
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
                    self.event_handler.add_event(
                        Event.EVENT_IGNORED, machine_name=_machine
                    )
        return response_dict

    def status(self) -> bool:
        """Get the status of machines in the current wave."""
        print(
            f"Getting Status of Project - Name: ({self.project_name}) - Dry Run: ({self.dry_run})"
        )

        machine_status: int = 0
        machines_response: Response = self.api.api_call(
            f"projects/{self.project_name}/machines"
        )
        for _machine in self.target_machines:
            machine_exist: bool = False
            for machine in json.loads(machines_response.text).get("items", []):
                source_props: Dict[str, Any] = machine.get("sourceProperties", {})
                ref_name: str = source_props.get("name") or source_props.get(
                    "machineCloudId", "NONE"
                )
                if ref_name == source_props.get("name", "NONE"):
                    machine_exist = True
                    # Check if replication is done
                    if "lastConsistencyDateTime" not in machine["replicationInfo"]:
                        print(f"ERROR: Machine: {ref_name} replication in progress")
                        return False
                    else:
                        # Check the replication lag between source and CE destination.
                        last_consistent_dt_1: int = int(
                            machine.get("replicationInfo", {}).get(
                                "lastConsistencyDateTime", ""
                            )[11:13]
                        )
                        last_consistent_dt_2: int = int(
                            machine.get("replicationInfo", {}).get(
                                "lastConsistencyDateTime", ""
                            )[14:16]
                        )
                        datetime_1: int = int(
                            datetime.datetime.utcnow().isoformat()[11:13]
                        )
                        datetime_2: int = int(
                            datetime.datetime.utcnow().isoformat()[14:16]
                        )
                        result: int = (datetime_1 - last_consistent_dt_1) * 60 + (
                            datetime_2 - last_consistent_dt_2
                        )
                        if result > self.max_lag_ttl:
                            print(
                                f"{ref_name} is currently lagging greater than {self.max_lag_ttl} minutes - ({result})"
                            )
                            return False
                        else:
                            if self.dry_run:
                                machine_status += 1
                            else:
                                # Check whether or not the target machine has already been tested.
                                _m_life_cycle: Dict[str, Any] = machine.get(
                                    "lifeCycle", {}
                                )
                                if (
                                    "lastTestLaunchDateTime" not in _m_life_cycle
                                    and "lastCutoverDateTime" not in _m_life_cycle
                                ):
                                    machine_status += 1
                                else:
                                    print(
                                        f"{ref_name} has already been tested - you can create AMIs now!"
                                    )
                                    return False
            if not machine_exist:
                print(f"ERROR: Machine: {_machine} does not exist!")
                self.nonexistent_machines.append(_machine)

        if machine_status == len(self.target_machines):
            print("All Machines in the targeted pool are ready!")
        else:
            print("ERROR: some machines in the targeted pool are not ready")
            return False
        return True

    def execute(self) -> bool:
        """Start the migration project my checking and launching the migration wave."""
        print(
            f"Executing Project - Name: ({self.project_name}) - Dry Run: ({self.dry_run})"
        )

        projects_result: Response = self.api.api_call("projects")
        if projects_result.status_code != 200:
            print("Failed to fetch the project!")
            return False

        try:
            # Get Machine List
            machines_response: Response = self.api.api_call(
                f"projects/{self.project_id}/machines"
            )
            if "sourceProperties" not in machines_response.text:
                print("Failed to fetch the machines!")
                return False

            machine_data_dict: Dict[str, Any] = {}
            for machine in json.loads(machines_response.text).get("items", []):
                source_props = machine.get("sourceProperties", {})
                if not source_props:
                    print("No source properties found!")
                    continue

                ref_name = source_props.get("name") or source_props.get(
                    "machineCloudId", "NONE"
                )
                _machine_id: str = source_props.get("id", "")
                print(f"Machine name: {ref_name}, Machine ID: {_machine_id}")
                machine_data_dict[machine["id"]] = ref_name

            # Check Target Machines
            print("Checking Target machines...")
            self.status()

            # Launch Target machines
            if not self.dry_run:
                print("Launching target machines...")
                self.launch()
        except Exception as e:
            print(str(e))
            return False

    def replication(self, action: str, machine_ids: str = "") -> bool:
        """Handle replication actions."""
        print(f"{action.title()} Machine Replication: ({machine_ids})")
        action: str = action.lower()
        _machines: List[str] = machine_ids.split(",")

        if not _machines:
            _machines = self.target_machines
            print(
                f"No machines provided.  Defaulting to project machines: ({_machines})"
            )

        replication_data: Dict[str, Any] = {"machineId": _machines}
        if action not in ["pause", "stop", "start"]:
            return False

        replication_results: Response = self.api.api_call(
            f"projects/{self.project_id}/{action}Replication",
            method="post",
            data=replication_data,
        )

        if replication_results.status_code != 200:
            print(
                f"Failed to update the machine(s) replication status to: ({action}) for ({machine_ids}): "
                f"{replication_results.status_code} {replication_results.content}"
            )
            print(replication_results.text)
            return False
        print("Project was updated successfully")
        return True

    def share_image(self, image_id: str, image_name: str = "CloudEndureImage") -> bool:
        """Share the generated AMIs to the provided destination account."""
        print("Loading EC2 client for region: ", AWS_REGION)
        _ec2_res = boto3.resource("ec2", AWS_REGION)

        # Access the image that needs to be copied
        image = _ec2_res.Image(image_id)

        try:
            # Share the image with the destination account
            image.modify_attribute(
                ImageId=image.id,
                Attribute="launchPermission",
                OperationType="add",
                LaunchPermission={"Add": [{"UserId": self.destination_account}]},
            )
        except Exception as e:
            print(e)
            return False

        # We have to now share the snapshots associated with the AMI so it can be copied
        devices = image.block_device_mappings
        for device in devices:
            if "Ebs" in device:
                snapshot_id: str = device["Ebs"]["SnapshotId"]
                snapshot = _ec2_res.Snapshot(snapshot_id)
                try:
                    snapshot.modify_attribute(
                        Attribute="createVolumePermission",
                        CreateVolumePermission={
                            "Add": [{"UserId": self.destination_account}]
                        },
                        OperationType="add",
                    )
                except Exception as e:
                    print(e)
                    return False
        print(f"AMI ID: ({image_id}) - Shared to: ({self.destination_account})")
        return True

    def create_ami(self) -> Dict[str, str]:
        """Create an AMI from the specified instances.

        Args:
            project_name (str): The name of the CloudEndure project.

        Returns:
            bool: Whether or not the AMI creation was successful.

        """
        amis = {}
        if not self.project_id:
            return amis

        try:
            print("Loading EC2 client for region: ", AWS_REGION)
            _ec2_client: boto_client = boto3.client("ec2", AWS_REGION)

            # Create an AMI from the migrated instance
            image_creation_time: str = datetime.datetime.utcnow().strftime(
                "%Y%m%d%H%M%S"
            )
            instances: Dict[str, Any] = _ec2_client.describe_instances(
                Filters=[
                    {"Name": "tag:MigrationWave", "Values": [self.migration_wave]},
                    {"Name": "tag:CloneStatus", "Values": ["NOT_STARTED"]},
                ]
            )

            if not instances or not instances.get("Reservations", []):
                print(
                    f"No instances or reservations found for migration wave: {self.migration_wave}"
                )
                return amis

            for reservation in instances.get("Reservations", []):
                for instance in reservation.get("Instances", []):
                    instance_id: str = instance.get("InstanceId", "")
                    ec2_image: Dict[str, Any] = _ec2_client.create_image(
                        InstanceId=instance_id,
                        Name=f"{instance_id}-{image_creation_time}",
                        Description=f"{self.project_name} - {self.project_id} - {instance_id} - {image_creation_time}",
                        NoReboot=True,
                    )
                    _filters: List[Any] = [
                        {"Name": "resource-id", "Values": [instance_id]}
                    ]

                    # Tag the newly created AMI by getting the tags of the migrated instance to copy to the AMI.
                    ec2_tags: Dict[str, Any] = _ec2_client.describe_tags(
                        Filters=_filters
                    )

                    name: str = instance_id
                    for tag in ec2_tags["Tags"]:
                        if tag["Key"] == "Name":
                            name = tag["Value"]

                        _ec2_client.create_tags(
                            Resources=[ec2_image["ImageId"]],
                            Tags=[{"Key": tag["Key"], "Value": tag["Value"]}],
                        )

                    _ec2_client.create_tags(
                        Resources=[instance_id],
                        Tags=[{"Key": "CloneStatus", "Value": "IMAGE_CREATED"}],
                    )
                    _ec2_client.delete_tags(
                        Resources=[ec2_image["ImageId"]], Tags=[{"Key": "CloneStatus"}]
                    )

                    amis[name] = ec2_image["ImageId"]
                    print(f"Instance ID: ({instance_id}) - AMI ID: ({ec2_image})")
        except ClientError as e:
            print(str(e))
            return amis
        return amis

    def copy_image(self, image_id: str) -> str:
        """Copy a shared image to an account.

        Args:
            image_id (str): The AWS AMI to be copied.

        Returns:
            str: The copied AWS AMI ID.

        """
        credentials = self._get_role_credentials("CopyImage", self.destination_role)

        _ec2_client: boto_client = boto3.client(
            "ec2",
            region_name=AWS_REGION,
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )

        print(f"Copying image {image_id} with KMS: {self.destination_kms}")
        new_image: Dict[str, Any] = _ec2_client.copy_image(
            SourceImageId=image_id,
            SourceRegion=AWS_REGION,
            Name=f"copied-{image_id}",
            Encrypted=True,
            KmsKeyId=self.destination_kms,
        )

        return new_image.get("ImageId", "")

    def split_image(self, image_id: str) -> Dict[str, Any]:
        """Split the image into a root drive only AMI and a collection of snapshots.

        Args:
            image_id (str): The AWS AMI to be copied.

        Returns:
            dict: The mapping of AWS EBS block devices.

        """
        print(
            f"Loading EC2 resource for region: {AWS_REGION} using role: {self.destination_role}"
        )
        credentials = self._get_role_credentials("SplitImage", self.destination_role)

        _ec2_res: boto_client = boto3.resource(
            "ec2",
            region_name=AWS_REGION,
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )

        # Access the image that needs to be split
        image = _ec2_res.Image(image_id)

        root_drive: Dict[str, Any] = {}
        drives: Dict[str, Any] = {}

        # separate the root drive from the other drives
        devices: List[Any] = image.block_device_mappings
        for device in devices:
            if "Ebs" in device:
                if device["DeviceName"] == image.root_device_name:
                    print(f"Found Root! {device}")
                    root_drive: Dict[str, Any] = device
                else:
                    drives[device["DeviceName"]] = device["Ebs"]

        # have to remove the encrypted flag
        del root_drive["Ebs"]["Encrypted"]

        # create a new AMI with only the root
        response = _ec2_res.register_image(
            Architecture=image.architecture,
            BlockDeviceMappings=[root_drive],
            Name=f"root-{image_id}",
            RootDeviceName=image.root_device_name,
            VirtualizationType=image.virtualization_type,
        )

        root_ami = response.id

        for drive in drives:
            print(drives[drive])
            _ec2_res.create_tags(
                Resources=[root_ami],
                Tags=[{"Key": f"Drive-{drive}", "Value": json.dumps(drives[drive])}],
            )

        # remove the old image
        image.deregister()

        return root_ami

    def gen_terraform(
        self,
        image_id: str,
        name: str = "INSTANCENAME",
        subnet_id: str = "SUBNET_ID",
        private_ip: str = "PRIVATE_IP",
        keypair: str = "KEYPAIR",
        security_group: str = "SECURITY_GROUP",
        tagging_module: str = "tagging_module",
    ) -> str:
        """Generate Terraform for a given split image.

        Args:
            image_id (str): The split AMI ID to be referenced.
            name (str): The name of the instance to be generated.
            subnet_id (str): The AWS VPC Subnet ID to be referenced.
            private_id (str): The internal IP address to associate with the AWS ENI.
            keypair (str): The AWS EC2 keypair name to be referenced.
            security_group (str): The AWS security group ID to be referenced.

        Returns:
            str: The raw Terraform with volume, ENI, and EC2 instance templates.

        """
        credentials = self._get_role_credentials("GenTerraform", self.destination_role)

        _ec2_res: boto_client = boto3.resource(
            "ec2",
            region_name=AWS_REGION,
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )

        # Access the image
        image: str = _ec2_res.Image(image_id)
        base_template_data = {
            "image_id": image_id,
            "name": name,
            "keypair": keypair,
            "uppercase_name": name.upper(),
            "subnet_id": subnet_id,
            "private_ip": private_ip,
            "security_group": security_group,
            "tagging_module": tagging_module,
            "region": AWS_REGION,
        }
        template: str = (
            TerraformTemplate.INSTANCE_TEMPLATE.format(**base_template_data)
            + TerraformTemplate.NETWORK_TEMPLATE.format(**base_template_data)
        )

        # If image.tags is empty, boto3 returns NoneType.
        if image.tags:
            for tag in image.tags:
                tag_key = tag.get("Key", "")
                if not tag_key.startswith("Drive-"):
                    continue

                drive = tag_key[6:]
                if not drive.startswith("/dev/sd"):
                    continue

                drive_info = json.loads(tag.get("Value", "{}"))
                drive_name = drive.split("/")[-1]

                drive_template_data = {
                    **base_template_data,
                    "drive": drive,
                    "drive_name": drive_name,
                    "snapshot_id": drive_info.get("SnapshotId", ""),
                    "volume_size": drive_info.get("VolumeSize", "2"),
                    "volume_type": drive_info.get("VolumeType", "gp2"),
                }

                drive_template = TerraformTemplate.VOLUME_TEMPLATE.format(
                    **drive_template_data
                )
                template = template + drive_template
        return template

    def terminate(self) -> bool:
        """Terminate the launched machine(s).

        Returns:
            bool: Whether cleanup was successful.

        """
        machines_response: Response = self.api.api_call(
            f"projects/{self.project_id}/machines"
        )
        success = True
        for _machine in self.target_machines:
            for machine in json.loads(machines_response.text).get("items", []):
                source_props: Dict[str, Any] = machine.get("sourceProperties", {})
                ref_name: str = source_props.get("name") or source_props.get(
                    "machineCloudId", "NONE"
                )
                if _machine == source_props.get(
                    "name", "NONE"
                ) or _machine == source_props.get("machineCloudId", "NONE"):
                    replica: str = machine.get("replica")
                    if replica:
                        print(
                            f"{ref_name} has a launched machine: {replica}.  Terminating."
                        )
                        data_dict: Dict[str, Any] = {}
                        data_dict["replicaIDs"] = [replica]

                        delete_response: Response = self.api.api_call(
                            path=f"projects/{self.project_id}/replicas",
                            method="delete",
                            data=json.dumps(data_dict),
                        )
                        if delete_response.status_code != 202:
                            print(
                                f"Response code: {delete_response.status_code}\n"
                                f"{ref_name} replica {replica} did not terminate.\n{delete_response.text}"
                            )
                            success = False
                        else:
                            print(
                                f"Terminated {ref_name}\n{json.loads(delete_response.text)}"
                            )
                    else:
                        print(f"{ref_name} does not have a launched machine")
                        success = False

        return success

    def delete_image(self, image_id: str) -> bool:
        """Remove the AMI and snapshots.

        Args:
            image_id (str): The AWS AMI to be deleted.

        Returns:
            bool: Whether the AMI deletion was requested successfully.

        """
        print("Loading EC2 resource for region: ", AWS_REGION)
        _ec2_res = boto3.resource("ec2", AWS_REGION)

        try:
            # Access the image that needs to be deleted
            image = _ec2_res.Image(image_id)

            # grab device mappings before deregistering
            devices: List[Any] = image.block_device_mappings
            image.deregister()
            for device in devices:
                if "Ebs" in device:
                    snap = _ec2_res.Snapshot(device["Ebs"].get("SnapshotId"))
                    snap.delete()
        except Exception as e:
            print(f"Failed.  AMI does not exist? {str(e)}")
            return False

        return True


def main() -> None:
    """Define the main entry method for the CLI."""
    # Run CloudEndure via the pipeline object for easy CLI access.
    fire.Fire(CloudEndure)


if __name__ == "__main__":
    main()
