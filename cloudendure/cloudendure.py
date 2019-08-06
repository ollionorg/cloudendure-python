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
from .exceptions import CloudEndureHTTPException

HOST: str = "https://console.cloudendure.com"
headers: Dict[str, str] = {"Content-Type": "application/json"}
session: Dict[str, str] = {}
env_machines: str = os.environ.get("CLOUDENDURE_MACHINES", "")
_machines: List[str] = env_machines.split(",")
global_project_id: str = os.environ.get("CLOUDENDURE_PROJECT_ID", "")
global_project_name: str = os.environ.get("CLOUDENDURE_PROJECT_NAME", "")
AWS_REGION: str = os.environ.get("AWS_REGION", "")
_DESTINATION_ACCOUNTS: str = os.environ.get("CLOUDENDURE_DESTINATION_ACCOUNTS", "")
DESTINATION_ACCOUNTS: List[str] = _DESTINATION_ACCOUNTS.split(",")
LAUNCH_TYPES: List[str] = ["test", "cutover"]
MIGRATION_WAVE: str = os.environ.get("CLOUDENDURE_MIGRATION_WAVE", "0")
CLONE_STATUS: str = os.environ.get("CLOUDENDURE_CLONE_STATUS", "NOT_STARTED")
MAX_LAG_TTL: int = int(os.environ.get("CLOUDENDURE_MAX_LAG_TTL", "90"))
SHARE_IMAGE: str = os.environ.get("", "")


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
        self.project_name = self.config.active_config.get(
            "project_name", global_project_name
        )
        self.project_id = (
            self.get_project_id(project_name=self.project_name) or global_project_id
        )

    @staticmethod
    def get_endpoint(
        path: str,
        api_version: str = "latest",
        host: str = "https://console.cloudendure.com",
    ) -> str:
        """Build the endpoint path.

        Returns:
            str: The CloudEndure API endpoint to be used.

        """
        return f"{host}/api/{api_version}/{path}"

    def get_project_id(self, project_name: str = ""):
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

        for _machine in _machines:
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

        if machine_status == len(_machines):
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
            if machine_name in _machines or machine_name.upper() in _machines:
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
                    {"key": "CloneStatus", "value": CLONE_STATUS},
                    {"key": "MigrationWave", "value": MIGRATION_WAVE},
                ]

                if dry_run:
                    print("This is a dry run! Not launching any machines!")
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

    def launch(self, project_name="", launch_type="test", dry_run=False):
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
        for _machine in _machines:
            for machine in json.loads(machines_response.text).get("items", []):
                source_props = machine.get("sourceProperties", {})
                machine_data = {}
                if _machine == source_props.get("name", "NONE"):
                    if machine.get("replica"):
                        print("Target machine already launched")
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
                    else:
                        print("ERROR: Invalid Launch Type!")

                if machine_data:
                    result = self.api.api_call(
                        f"projects/{project_id}/launchMachines",
                        method="post",
                        data=json.dumps(machine_data),
                    )
                    if result.status_code == 202:
                        if launch_type == "test":
                            print("Test Job created for machine ", _machine)
                        elif launch_type == "cutover":
                            print("Cutover Job created for machine ", _machine)
                    elif result.status_code == 409:
                        print(f"ERROR: ({_machine}) is currently in progress!")
                    elif result.status_code == 402:
                        print("ERROR: Project license has expired!")
                    else:
                        print("ERROR: Launch target machine failed!")
                else:
                    print(
                        f"Machine: ({source_props['name']}) - Not a machine we want to launch..."
                    )

    def status(
        self, project_id: str = "", launch_type: str = "test", dry_run: bool = False
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
        for _machine in _machines:
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
                        if result > MAX_LAG_TTL:
                            print(
                                f"{ref_name} is currently lagging greater than {MAX_LAG_TTL} minutes - ({result})"
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

        if machine_status == len(_machines):
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
            dest_accounts = DESTINATION_ACCOUNTS

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

    def create_ami(
        self, instance_ids: List[str] = None, project_name: str = ""
    ) -> bool:
        """Create an AMI from the specified instance."""
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
                    {"Name": "tag:MigrationWave", "Values": [MIGRATION_WAVE]},
                    {"Name": "tag:CloneStatus", "Values": ["NOT_STARTED"]},
                ]
            )
            for reservation in instances.get("Reservations", []):
                for instance in reservation.get("Instances", []):
                    instance_id: str = instance.get("InstanceId", "")
                    ec2_image = _ec2_client.create_image(
                        InstanceId=instance_id,
                        Name=f"{image_creation_time}",
                        Description=f"{project_name} - {project_id} - {image_creation_time}",
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

    def copy_image(self, image_id: str, kms_id: str):
        """Copy a shared image to a account"""
        _ec2_client = boto3.client("ec2", AWS_REGION)

        new_image = _ec2_client.copy_image(
            SourceImageId=image_id,
            SourceRegion=AWS_REGION,
            Name="test",
            Encrypted=True,
            KmsKeyId=kms_id,
        )

        print(new_image)
        return new_image["ImageId"]

    def split_image(self, image_id: str, root_name: str = "root_image"):
        """Split the image into a root drive only AMI and a collection of snapshots."""
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
            Name=root_name,
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
