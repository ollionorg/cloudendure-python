#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Define the CloudEndure main entry logic."""
import datetime
import json
import os
from typing import Dict, List

import boto3
import fire
from botocore.exceptions import ClientError

from cloudendure.cloudendure_api.api_client import ApiClient

from .api import CloudEndureAPI
from .config import CloudEndureConfig
from .exceptions import CloudEndureHTTPException
from .models import Project

HOST: str = 'https://console.cloudendure.com'
headers: Dict[str, str] = {'Content-Type': 'application/json'}
session: Dict[str, str] = {}
endpoint = '/api/latest/{}'
env_machines: str = os.environ.get('CLOUDENDURE_MACHINES', '')
_machines: List[str] = env_machines.split(',')
global_project_id: str = os.environ.get('CLOUDENDURE_PROJECT_ID', '')
global_project_name: str = os.environ.get('CLOUDENDURE_PROJECT_NAME', '')
AWS_REGION: str = os.environ.get('AWS_REGION', '')
_DESTINATION_ACCOUNTS: str = os.environ.get('CLOUDENDURE_DESTINATION_ACCOUNTS', '')
DESTINATION_ACCOUNTS: List[str] = _DESTINATION_ACCOUNTS.split(',')
LAUNCH_TYPES: List[str] = ['test', 'cutover']
MIGRATION_WAVE: str = os.environ.get('CLOUDENDURE_MIGRATION_WAVE', '0')
CLONE_STATUS: str = os.environ.get('CLOUDENDURE_CLONE_STATUS', 'NOT_STARTED')
MAX_LAG_TTL: int = int(os.environ.get('CLOUDENDURE_MAX_LAG_TTL', '90'))


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
        self.project = Project()

    @staticmethod
    def get_endpoint(path: str, api_version: str = 'latest', host: str = 'https://console.cloudendure.com') -> str:
        """Build the endpoint path.

        Returns:
            str: The CloudEndure API endpoint to be used.

        """
        return f'{host}/api/{api_version}/{path}'

    def check(self, project_name=global_project_name, launch_type='test', dry_run=False):
        """Check the status of machines in the provided project."""
        print(f'Checking Project - Name: ({project_name}) - Launch Type: ({launch_type}) - Dry Run: ({dry_run})')
        projects_response = self.api.api_call('projects')

        if projects_response.status_code != 200:
            print('Failed to fetch the project!')
            raise CloudEndureHTTPException('Failed to fetch the CloudEndure Project!')

        try:
            # Get Project ID
            projects = json.loads(projects_response.text).get('items', [])
            project_exist = False
            for project in projects:
                if project["name"] == project_name:
                    project_id = project["id"]
                    project_exist = True

            if not project_exist:
                print("ERROR: Project Name does not exist!")
                return False
        except Exception as e:
            print(str(e))
            return False

        machine_status = 0
        machines_response = self.api.api_call(f'projects/{project_id}/machines')

        for _machine in _machines:
            machine_exist = False
            for machine in json.loads(machines_response.text).get('items', []):
                source_props = machine.get('sourceProperties', {})
                ref_name = source_props.get('name') or source_props.get('machineCloudId', 'NONE')
                if _machine == source_props.get('name', 'NONE') or \
                        _machine == source_props.get('machineCloudId', 'NONE'):
                    machine_exist = True

                    if 'lastConsistencyDateTime' not in machine['replicationInfo']:
                        print(f'{ref_name} replication into the migration account in progress!')
                    else:
                        if launch_type == "test":
                            if 'lastTestLaunchDateTime' in machine["lifeCycle"]:
                                machine_status += 1
                                print(f'{ref_name} has been launched in the migration account')
                            else:
                                print(
                                    f'{ref_name} has not completed launching in the migration account - Please wait...'
                                )
                        elif launch_type == "cutover":
                            if 'lastCutoverDateTime' in machine["lifeCycle"]:
                                machine_status += 1
                                print(f'{ref_name} has been cutover into the migration account')
                            else:
                                print(f'{ref_name} has NOT been cutover into the migration account')

            if not machine_exist:
                print(f'ERROR: Machine: {_machine} does not exist!')

        if machine_status == len(_machines):
            if launch_type == 'test':
                print('All machines specified in CLOUDENDURE_MACHINES have been launched in the migration account')
            if launch_type == 'cutover':
                print('All machines specified in CLOUDENDURE_MACHINES have been cutover to the target account')
        else:
            if launch_type == 'test':
                print('Some machines have not yet completed launching in the migration account')
            if launch_type == 'cutover':
                print('Some machines have not yet completed cutting over into the migration account')

    def update_blueprint(self, project_id=global_project_id, launch_type='test', dry_run=False, machine_list=None):
        print('Updating the CloudEndure Blueprints...')

        try:
            blueprints_response = self.api.api_call(f'projects/{project_id}/blueprints')
            for blueprint in json.loads(blueprints_response.text).get('items', []):
                _machine_id = blueprint.get('machineId')
                _machine_name = machine_list[_machine_id]
                _blueprint_id = blueprint.get('id', '')
                _endpoint = f'projects/{project_id}/blueprints/{_blueprint_id}'

                for _machine in _machines:
                    if _machine_name == _machine:
                        # Handle disk blueprints since we don't want provisioned IOPS $$$$
                        for disk in blueprint['disks']:
                            blueprint['disks'] = [{'type': 'SSD', 'name': disk.get('name', '')}]

                        # Update machine tags
                        blueprint['tags'] = {'CloneStatus': CLONE_STATUS, 'MigrationWave': MIGRATION_WAVE}

                        result = self.api.api_call(_endpoint, method='patch', data=json.dumps(blueprint))

                        if result.status_code != 200:
                            print(
                                f'Blueprint update failure encountered for machine: ({_machine_name}) - fix blueprint settings!'
                            )
                        print('Blueprint for machine: ' + _machine_name + ' updated!')
        except Exception as e:
            print(f'Updating blueprint task failed! {e}')
            return False

    def launch(self, project_id=global_project_id, launch_type='test', dry_run=False):
        print(f'Launching Project - Project ID: ({project_id}) - Launch Type: ({launch_type}) - Dry Run: ({dry_run})')
        if dry_run:
            print('This is a dry run! Not launching any machines!')
            return False

        if launch_type not in LAUNCH_TYPES:
            print('Invalid launch-type specified! Please specify a valid launch type: ', LAUNCH_TYPES)
            return False

        machines_response = self.api.session.get(HOST + endpoint.format(f'projects/{project_id}/machines'))
        for _machine in _machines:
            for machine in json.loads(machines_response.text).get('items', []):
                source_props = machine.get('sourceProperties', {})
                machine_data = {}
                if _machine == source_props.get('name', 'NONE'):
                    if launch_type == 'test':
                        machine_data = {'items': [{'machineId': machine['id']}], 'launchType': 'TEST'}
                    elif launch_type == 'cutover':
                        machine_data = {'items': [{'machineId': machine['id']}], 'launchType': 'CUTOVER'}
                    else:
                        print('ERROR: Invalid Launch Type!')

                if machine_data:
                    result = self.api.session.post(
                        HOST + endpoint.format(f'projects/{project_id}/launchMachines'),
                        data=json.dumps(machine_data),
                    )
                    if result.status_code == 202:
                        if launch_type == 'test':
                            print('Test Job created for machine ', _machine)
                        elif launch_type == 'cutover':
                            print('Cutover Job created for machine ', _machine)
                    elif result.status_code == 409:
                        print(f'ERROR: ({_machine}) is currently in progress!')
                    elif result.status_code == 402:
                        print('ERROR: Project license has expired!')
                    else:
                        print('ERROR: Launch target machine failed!')
                else:
                    print(f'Machine: ({_machine}) - Not a machine we want to launch...')

    def status(self, project_id=global_project_id, launch_type='test', dry_run=False):
        print(
            f'Getting Status of Project - Project ID: ({project_id}) -',
            f'Launch Type: ({launch_type}) - Dry Run: ({dry_run})'
        )
        machine_status = 0
        machines_response = self.api.api_call(f'projects/{project_id}/machines')
        for _machine in _machines:
            machine_exist = False
            for machine in json.loads(machines_response.text).get('items', []):
                source_props = machine.get('sourceProperties', {})
                ref_name = source_props.get('name') or source_props.get('machineCloudId', 'NONE')
                if ref_name == source_props.get('name', 'NONE'):
                    machine_exist = True
                    # Check if replication is done
                    if 'lastConsistencyDateTime' not in machine['replicationInfo']:
                        print(f"ERROR: Machine: {ref_name} replication in progress")
                        return False
                    else:
                        # Check the replication lag between source and CE destination.
                        last_consistent_dt_1 = int(
                            machine.get('replicationInfo', {}).get('lastConsistencyDateTime', '')[11:13]
                        )
                        last_consistent_dt_2 = int(
                            machine.get('replicationInfo', {}).get('lastConsistencyDateTime', '')[14:16]
                        )
                        datetime_1 = int(datetime.datetime.utcnow().isoformat()[11:13])
                        datetime_2 = int(datetime.datetime.utcnow().isoformat()[14:16])
                        result = (datetime_1 - last_consistent_dt_1) * 60 + (datetime_2 - last_consistent_dt_2)
                        if result > MAX_LAG_TTL:
                            print(f'{ref_name} is currently lagging greater than {MAX_LAG_TTL} minutes - ({result})')
                            return False
                        else:
                            if dry_run:
                                machine_status += 1
                            else:
                                # Check whether or not the target machine has already been tested.
                                _m_life_cycle = machine.get('lifeCycle', {})
                                if launch_type == 'test':
                                    if 'lastTestLaunchDateTime' not in _m_life_cycle and \
                                        'lastCutoverDateTime' not in _m_life_cycle:
                                        machine_status += 1
                                    else:
                                        print(f'{ref_name} has already been tested - you can create AMIs now!')
                                        return False
                                # Check if the target machine has been migrated to PROD already
                                elif launch_type == 'cutover':
                                    if 'lastTestLaunchDateTime' in machine['lifeCycle']:
                                        if 'lastCutoverDateTime' not in machine['lifeCycle']:
                                            machine_status += 1
                                        else:
                                            print('ERROR: Machine: ' + ref_name + ' has been migrated already')
                                            return False
                                    else:
                                        print('ERROR: Machine: ' + ref_name + ' has not been tested')
                                        return False
            if not machine_exist:
                print('ERROR: Machine: ' + _machine + ' does not exist!')
                return False

        if machine_status == len(_machines):
            print('All Machines in the targeted pool are ready!')
        else:
            print('ERROR: some machines in the targeted pool are not ready')
            return False

    def execute(self, project_name=global_project_name, launch_type='test', dry_run=False):
        """Start the migration project my checking and launching the migration wave."""
        print(f'Executing Project - Name: ({project_name}) - Launch Type: ({launch_type}) - Dry Run: ({dry_run})')

        projects_result = self.api.api_call('projects')
        if projects_result.status_code != 200:
            print('Failed to fetch the project!')
            return False

        try:
            # Get Project ID
            projects = json.loads(projects_result.text).get('items', [])
            project_exist = False
            for project in projects:
                if project.get('name', 'NONE') == project_name:
                    project_id = project.get('id', '')
                    project_exist = True
            if not project_exist:
                print('Project Name does not exist!')
                return False

            # Get Machine List
            machines_response = self.api.api_call(f'projects/{project_id}/machines')
            if 'sourceProperties' not in machines_response.text:
                print('Failed to fetch the machines!')
                return False

            machinelist = {}
            for machine in json.loads(machines_response.text).get('items', []):
                source_props = machine.get('sourceProperties', {})
                if not source_props:
                    print('No source properties found!')
                    continue

                ref_name = source_props.get('name') or source_props.get('machineCloudId', 'NONE')
                _machine_id = source_props.get('id', '')
                print(f'Machine name: {ref_name}, Machine ID: {_machine_id}')
                machinelist[machine['id']] = ref_name

            # Check Target Machines
            print('Checking Target machines...')
            self.status()

            # Launch Target machines
            if not dry_run:
                print('Launching target machines...')
                self.launch(launch_type=launch_type, dry_run=dry_run)
        except Exception as e:
            print(str(e))
            return False

    def share_image(self, image_id, dest_accounts=None, image_name='CloudEndureImage'):
        """Share the generated AMIs to the provided destination accounts."""
        print('Loading EC2 client for region: ', AWS_REGION)
        _ec2_client = boto3.client('ec2', AWS_REGION)

        # Access the image that needs to be copied
        image = _ec2_client.Image(image_id)

        if not dest_accounts:
            dest_accounts = DESTINATION_ACCOUNTS

        for account in dest_accounts:
            # Share the image with the destination account
            image.modify_attribute(
                ImageId=image.id,
                Attribute='launchPermission',
                OperationType='add',
                LaunchPermission={'Add': [{
                    'UserId': account
                }]}
            )

            # We have to now share the snapshots associated with the AMI so it can be copied
            devices = image.block_device_mappings
            for device in devices:
                if 'Ebs' in device:
                    snapshot_id = device['Ebs']['SnapshotId']
                    snapshot = _ec2_client.Snapshot(snapshot_id)
                    snapshot.modify_attribute(
                        Attribute='createVolumePermission',
                        CreateVolumePermission={'Add': [{
                            'UserId': account
                        }]},
                        OperationType='add',
                    )

    def create_ami(self, instance_ids=None, project_id=global_project_id, project_name=global_project_name):
        """Create an AMI from the specified instance."""
        try:
            print('Loading EC2 client for region: ', AWS_REGION)
            _ec2_client = boto3.client('ec2', AWS_REGION)

            # Create an AMI from the migrated instance
            image_creation_time = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
            instances = _ec2_client.describe_instances(
                Filters=[{
                    'Name': 'tag:MigrationWave',
                    'Values': ['0']
                }, {
                    'Name': 'tag:CloneStatus',
                    'Values': ['NOT_STARTED']
                }]
            )
            for reservation in instances.get('Reservations', []):
                for instance in reservation.get('Instances', []):
                    instance_id = instance.get('InstanceId', '')
                    ec2_image = _ec2_client.create_image(
                        InstanceId=instance_id,
                        Name=f"{image_creation_time}",
                        Description=f"{project_name} - {project_id} - {image_creation_time}",
                        NoReboot=True,
                    )
                    _filters = [{'Name': 'resource-id', 'Values': [instance_id]}]

                    # Tag the newly created AMI by getting the tags of the migrated instance to copy to the AMI.
                    ec2_tags = _ec2_client.describe_tags(Filters=_filters)

                    for tag in ec2_tags['Tags']:
                        _ec2_client.create_tags(
                            Resources=[ec2_image['ImageId']], Tags=[{
                                'Key': tag['Key'],
                                'Value': tag['Value']
                            }]
                        )

                    _ec2_client.create_tags(
                        Resources=[instance_id], Tags=[{
                            'Key': 'CloneStatus',
                            'Value': 'IMAGE_CREATED'
                        }]
                    )
                    _ec2_client.delete_tags(Resources=[ec2_image['ImageId']], Tags=[{'Key': 'CloneStatus'}])
                    print(f'Instance ID: ({instance_id}) - AMI ID: ({ec2_image})')
        except ClientError as e:
            print(str(e))
            pass


def main():
    """Define the main entry method for the CLI."""
    # Run CloudEndure via the pipeline object for easy CLI access.
    fire.Fire(CloudEndure)


if __name__ == '__main__':
    main()
