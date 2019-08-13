#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Define the CloudEndure main entry logic."""
import datetime
import json
import os
from typing import Any, Dict, List

import boto3
import fire
from botocore.exceptions import ClientError

from cloudendure.cloudendure_api.api_client import ApiClient

from .api import CloudEndureAPI
from .config import CloudEndureConfig
from .events import Event, EventHandler
from .exceptions import CloudEndureHTTPException

HOST: str = "https://console.cloudendure.com"
headers: Dict[str, str] = {"Content-Type": "application/json"}
session: Dict[str, str] = {}
AWS_REGION: str = os.environ.get("AWS_REGION", "")
LAUNCH_TYPES: List[str] = ["test", "cutover"]


class CloudEndure:
    """Define the CloudEndure general object."""

    def __init__(self):
        """Initialize the CloudEndure object.

        This entrypoint is primarily for use with the CLI.

        """
        self.config = CloudEndureConfig()
        self.api = CloudEndureAPI()
        self.api.login()
        self.api_client = ApiClient()
        self.project_name = self.config.active_config.get("project_name", "")
        self.project_id = self.get_project_id(
            project_name=self.project_name
        ) or self.config.active_config.get("project_id", "")
        self.event_handler = EventHandler()
        self.destination_accounts: List[str] = self.config.active_config.get(
            "destination_accounts", ""
        ).split(",")
        self.target_machines: List[str] = self.config.active_config.get(
            "machines", ""
        ).split(",")
        self.migration_wave: str = self.config.active_config.get("migration_wave", "0")
        self.max_lag_ttl: str = self.config.active_config.get("max_lag_ttl", "90")

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
        projects_result = self.api.api_call("projects")
        if projects_result.status_code != 200:
            print("Failed to fetch the project!")
            return ""

        if not project_name:
            project_name = self.project_name

        try:
            # Get Project ID
            projects = json.loads(projects_result.text).get("items", [])
            found_project = next(
                (item for item in projects if item.get("name", "NONE") == project_name),
                {},
            )
            project_id = found_project.get("id", "")
        except Exception as e:
            print(f"Exception: {str(e)}")
            return ""

        if project_id:
            print(f"Found project_id: {project_id}")
            return project_id
        print("Project Name does not exist!")
        return ""

    def check(
        self, project_name: str = "", launch_type: str = "test", dry_run: bool = False
    ):
        """Check the status of machines in the provided project."""
        if not project_name:
            project_name = self.project_name
            project_id = self.project_id
        else:
            project_id = self.get_project_id(project_name=project_name)

        if not project_id:
            return False

        print(
            f"Checking Project - Name: ({project_name}) - Launch Type: ({launch_type}) - Dry Run: ({dry_run})"
        )
        projects_response = self.api.api_call("projects")

        if projects_response.status_code != 200:
            print("Failed to fetch the project!")
            raise CloudEndureHTTPException("Failed to fetch the CloudEndure Project!")

        machine_status: int = 0
        machines_response = self.api.api_call(f"projects/{project_id}/machines")

        for _machine in self.target_machines:
            machine_exist = False
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
                        if launch_type == "test":
                            if machine.get("replica"):
                                machine_status += 1
                                print(
                                    f"{ref_name} has been launched in the migration account"
                                )
                            else:
                                print(
                                    f"{ref_name} has not completed launching in the migration account - Please wait..."
                                )
                        elif launch_type == "cutover":
                            if machine.get("replica"):
                                machine_status += 1
                                print(
                                    f"{ref_name} has been cutover into the migration account"
                                )
                            else:
                                print(
                                    f"{ref_name} has NOT been cutover into the migration account"
                                )

            if not machine_exist:
                print(f"ERROR: Machine: {_machine} does not exist!")

        if machine_status == len(self.target_machines):
            if launch_type == "test":
                print(
                    "All machines specified in CLOUDENDURE_MACHINES have been launched in the migration account"
                )
            if launch_type == "cutover":
                print(
                    "All machines specified in CLOUDENDURE_MACHINES have been cutover to the target account"
                )
        else:
            if launch_type == "test":
                print(
                    "Some machines have not yet completed launching in the migration account"
                )
            if launch_type == "cutover":
                print(
                    "Some machines have not yet completed cutting over into the migration account"
                )
        return True

    def update_encryption_key(
        self, kms_id: str, project_name: str = "", dry_run: bool = False
    ) -> bool:
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
        print("Updating encryption key...")

        if not project_name:
            project_name = self.project_name
            project_id = self.project_id
        else:
            project_id = self.get_project_id(project_name=project_name)

        if not project_id:
            return False

        machines_response = self.api.api_call(f"projects/{project_id}/machines")
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

            if dry_run:
                print(f"DRY RUN - Not updating key for {name} - DRY RUN")
                continue

            replication_config["volumeEncryptionKey"] = kms_id
            endpoint = f"projects/{project_id}/machines/{machine_id}"
            print(f"sending to {endpoint}")
            result = self.api.api_call(
                endpoint, method="patch", data=json.dumps(machine)
            )

            if result.status_code != 200:
                print(
                    f"Key update failure encountered for machine: {name} - {result.status_code}\n{result.json()}"
                )
            else:
                print(f"Key updated for or machine: {name}")

        return True

    def update_blueprint(self, project_name: str = "", dry_run: bool = False) -> bool:
        """Update the blueprint associated with the specified machines."""
        print("Updating the CloudEndure Blueprints...")

        if not project_name:
            project_name = self.project_name
            project_id = self.project_id
        else:
            project_id = self.get_project_id(project_name=project_name)

        if not project_id:
            return False

        machine_list = {}
        machines_response = self.api.api_call(f"projects/{project_id}/machines")
        for machine in json.loads(machines_response.text).get("items", []):
            source_props: Dict[str, Any] = machine.get("sourceProperties", {})
            machine_id: str = machine.get("id")
            machine_name: str = source_props.get("name")
            if (
                machine_name in self.target_machines
                or machine_name.upper() in self.target_machines
            ):
                machine_list[machine_id] = machine_name

        if not machine_list:
            print("No Machines Found!")
            return False

        try:
            blueprints_response = self.api.api_call(f"projects/{project_id}/blueprints")
            for blueprint in json.loads(blueprints_response.text).get("items", []):
                _machine_id = blueprint.get("machineId")
                _machine_name = machine_list.get(_machine_id)
                if not _machine_name:
                    continue

                _blueprint_id = blueprint.get("id", "")
                _endpoint = f"projects/{project_id}/blueprints/{_blueprint_id}"
                # Handle disk blueprints since we don't want provisioned IOPS $$$$
                for disk in blueprint["disks"]:
                    blueprint["disks"] = [{"type": "SSD", "name": disk.get("name", "")}]

                # Update machine tags
                blueprint["tags"] = [
                    {
                        "key": "CloneStatus",
                        "value": self.config.active_config.get(
                            "clone_status", "NOT_STARTED"
                        ),
                    },
                    {"key": "MigrationWave", "value": self.migration_wave},
                ]

                if dry_run:
                    print("This is a dry run! Not updating blueprints!")
                    return True

                result = self.api.api_call(
                    _endpoint, method="patch", data=json.dumps(blueprint)
                )

                if result.status_code != 200:
                    print(
                        "Blueprint update failure encountered for machine:",
                        f"({_machine_name}) - {result.status_code} fix blueprint settings!",
                    )
                else:
                    print("Blueprint for machine: " + _machine_name + " updated!")
        except Exception as e:
            print(f"Updating blueprint task failed! {e}")
            return False
        return True

    def launch(self, project_name="", launch_type="test", dry_run=False) -> bool:
        """Launch the test target instances."""
        if not project_name:
            project_name = self.project_name
            project_id = self.project_id
        else:
            project_id = self.get_project_id(project_name=project_name)

        if not project_id:
            return False

        print(
            f"Launching Project - Project ID: ({project_id}) - ",
            f"Launch Type: ({launch_type}) - Dry Run: ({dry_run})",
        )
        if dry_run:
            print("This is a dry run! Not launching any machines!")
            return False

        if launch_type not in LAUNCH_TYPES:
            print(
                "Invalid launch-type specified! Please specify a valid launch type: ",
                LAUNCH_TYPES,
            )
            return False

        machines_response = self.api.api_call(f"projects/{project_id}/machines")
        for _machine in self.target_machines:
            for machine in json.loads(machines_response.text).get("items", []):
                source_props = machine.get("sourceProperties", {})
                machine_data = {}
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
                    result = self.api.api_call(
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
                    self.event_handler.add_event(
                        Event.EVENT_IGNORED, machine_name=_machine
                    )
        return True

    def status(
        self, project_name: str = "", launch_type: str = "test", dry_run: bool = False
    ) -> bool:
        """Get the status of machines in the current wave."""
        if not project_name:
            project_name = self.project_name
            project_id = self.project_id
        else:
            project_id = self.get_project_id(project_name=project_name)

        if not project_id:
            return False

        print(
            f"Getting Status of Project - Project ID: ({project_id}) -",
            f"Launch Type: ({launch_type}) - Dry Run: ({dry_run})",
        )
        machine_status = 0
        machines_response = self.api.api_call(f"projects/{project_id}/machines")
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
                        last_consistent_dt_1 = int(
                            machine.get("replicationInfo", {}).get(
                                "lastConsistencyDateTime", ""
                            )[11:13]
                        )
                        last_consistent_dt_2 = int(
                            machine.get("replicationInfo", {}).get(
                                "lastConsistencyDateTime", ""
                            )[14:16]
                        )
                        datetime_1 = int(datetime.datetime.utcnow().isoformat()[11:13])
                        datetime_2 = int(datetime.datetime.utcnow().isoformat()[14:16])
                        result = (datetime_1 - last_consistent_dt_1) * 60 + (
                            datetime_2 - last_consistent_dt_2
                        )
                        if result > self.max_lag_ttl:
                            print(
                                f"{ref_name} is currently lagging greater than {self.max_lag_ttl} minutes - ({result})"
                            )
                            return False
                        else:
                            if dry_run:
                                machine_status += 1
                            else:
                                # Check whether or not the target machine has already been tested.
                                _m_life_cycle = machine.get("lifeCycle", {})
                                if launch_type == "test":
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
                                # Check if the target machine has been migrated to PROD already
                                elif launch_type == "cutover":
                                    if "lastTestLaunchDateTime" in machine["lifeCycle"]:
                                        if (
                                            "lastCutoverDateTime"
                                            not in machine["lifeCycle"]
                                        ):
                                            machine_status += 1
                                        else:
                                            print(
                                                "ERROR: Machine: "
                                                + ref_name
                                                + " has been migrated already"
                                            )
                                            return False
                                    else:
                                        print(
                                            "ERROR: Machine: "
                                            + ref_name
                                            + " has not been tested"
                                        )
                                        return False
            if not machine_exist:
                print("ERROR: Machine: " + _machine + " does not exist!")
                return False

        if machine_status == len(self.target_machines):
            print("All Machines in the targeted pool are ready!")
        else:
            print("ERROR: some machines in the targeted pool are not ready")
            return False

    def execute(
        self, project_name: str = "", launch_type: str = "test", dry_run: bool = False
    ) -> bool:
        """Start the migration project my checking and launching the migration wave."""
        if not project_name:
            project_name = self.project_name
            project_id = self.project_id
        else:
            project_id = self.get_project_id(project_name=project_name)

        if not project_id:
            return False

        print(
            f"Executing Project - Name: ({project_name}) - Launch Type: ({launch_type}) - Dry Run: ({dry_run})"
        )

        projects_result = self.api.api_call("projects")
        if projects_result.status_code != 200:
            print("Failed to fetch the project!")
            return False

        try:
            # Get Machine List
            machines_response = self.api.api_call(f"projects/{project_id}/machines")
            if "sourceProperties" not in machines_response.text:
                print("Failed to fetch the machines!")
                return False

            machinelist = {}
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
                machinelist[machine["id"]] = ref_name

            # Check Target Machines
            print("Checking Target machines...")
            self.status()

            # Launch Target machines
            if not dry_run:
                print("Launching target machines...")
                self.launch(launch_type=launch_type, dry_run=dry_run)
        except Exception as e:
            print(str(e))
            return False

    def share_image(
        self,
        image_id: str,
        dest_accounts: List[Any] = None,
        image_name: str = "CloudEndureImage",
    ) -> bool:
        """Share the generated AMIs to the provided destination accounts."""
        print("Loading EC2 client for region: ", AWS_REGION)
        _ec2_res = boto3.resource("ec2", AWS_REGION)

        # Access the image that needs to be copied
        image = _ec2_res.Image(image_id)

        if not dest_accounts:
            dest_accounts = self.destination_accounts

        for account in dest_accounts:
            try:
                # Share the image with the destination account
                image.modify_attribute(
                    ImageId=image.id,
                    Attribute="launchPermission",
                    OperationType="add",
                    LaunchPermission={"Add": [{"UserId": account}]},
                )
            except Exception as e:
                print(e)
                return False

            # We have to now share the snapshots associated with the AMI so it can be copied
            devices = image.block_device_mappings
            for device in devices:
                if "Ebs" in device:
                    snapshot_id = device["Ebs"]["SnapshotId"]
                    snapshot = _ec2_res.Snapshot(snapshot_id)
                    try:
                        snapshot.modify_attribute(
                            Attribute="createVolumePermission",
                            CreateVolumePermission={"Add": [{"UserId": account}]},
                            OperationType="add",
                        )
                    except Exception as e:
                        print(e)
                        return False
            print(f"AMI ID: ({image_id}) - Shared to: ({account})")
            return True

    def create_ami(self, project_name: str = "") -> bool:
        """Create an AMI from the specified instance.

        Args:
            project_name (str): The name of the CloudEndure project.

        Returns:
            bool: Whether or not the AMI creation was successful.

        """
        if not project_name:
            project_name: str = self.project_name
            project_id: str = self.project_id
        else:
            project_id: str = self.get_project_id(project_name=project_name)

        if not project_id:
            return False

        try:
            print("Loading EC2 client for region: ", AWS_REGION)
            _ec2_client = boto3.client("ec2", AWS_REGION)

            # Create an AMI from the migrated instance
            image_creation_time: str = datetime.datetime.utcnow().strftime(
                "%Y%m%d%H%M%S"
            )
            instances = _ec2_client.describe_instances(
                Filters=[
                    {"Name": "tag:MigrationWave", "Values": [self.migration_wave]},
                    {"Name": "tag:CloneStatus", "Values": ["NOT_STARTED"]},
                ]
            )
            for reservation in instances.get("Reservations", []):
                for instance in reservation.get("Instances", []):
                    instance_id: str = instance.get("InstanceId", "")
                    ec2_image = _ec2_client.create_image(
                        InstanceId=instance_id,
                        Name=f"{instance_id}-{image_creation_time}",
                        Description=f"{project_name} - {project_id} - {instance_id} - {image_creation_time}",
                        NoReboot=True,
                    )
                    _filters: List[Any] = [
                        {"Name": "resource-id", "Values": [instance_id]}
                    ]

                    # Tag the newly created AMI by getting the tags of the migrated instance to copy to the AMI.
                    ec2_tags = _ec2_client.describe_tags(Filters=_filters)

                    for tag in ec2_tags["Tags"]:
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
                    print(f"Instance ID: ({instance_id}) - AMI ID: ({ec2_image})")
        except ClientError as e:
            print(str(e))
            return False
        return True

    def copy_image(self, image_id: str, kms_id: str) -> str:
        """Copy a shared image to an account.

        Args:
            image_id (str): The AWS AMI to be copied.
            kms_id (str): The AWS KMS ID to be used for image encryption.

        Returns:
            str: The copied AWS AMI ID.

        """
        _ec2_client = boto3.client("ec2", AWS_REGION)

        new_image = _ec2_client.copy_image(
            SourceImageId=image_id,
            SourceRegion=AWS_REGION,
            Name=f"copied-ami-{image_id}",
            Encrypted=True,
            KmsKeyId=kms_id,
        )

        print(new_image)
        return new_image["ImageId"]

    def split_image(self, image_id: str) -> Dict[str, Any]:
        """Split the image into a root drive only AMI and a collection of snapshots.

        Args:
            image_id (str): The AWS AMI to be copied.

        Returns:
            dict: The mapping of AWS EBS block devices.

        """
        print("Loading EC2 client for region: ", AWS_REGION)
        _ec2_res = boto3.resource("ec2", AWS_REGION)

        # Access the image that needs to be split
        image = _ec2_res.Image(image_id)

        root_drive = {}
        drives = {}

        # separate the root drive from the other drives
        devices = image.block_device_mappings
        for device in devices:
            if "Ebs" in device:
                if device["DeviceName"] == image.root_device_name:
                    print(f"Found Root! {device}")
                    root_drive = device
                else:
                    drives[device["DeviceName"]] = device["Ebs"]

        # have to remove the encrypted flag
        del root_drive["Ebs"]["Encrypted"]

        # create a new AMI with only the root
        response = _ec2_res.register_image(
            Architecture=image.architecture,
            BlockDeviceMappings=[root_drive],
            Name=f"root-ami-{image_id}",
            RootDeviceName=image.root_device_name,
            VirtualizationType=image.virtualization_type,
        )

        # return the AMI
        drives["root_ami"] = response.id
        return drives


def main():
    """Define the main entry method for the CLI."""
    # Run CloudEndure via the pipeline object for easy CLI access.
    fire.Fire(CloudEndure)


if __name__ == "__main__":
    main()
