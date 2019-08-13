# -*- coding: utf-8 -*-
"""Define the CloudEndure API wrapper related logic."""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any, Dict

from dateutil.tz import tzlocal

logger: logging.Logger = logging.getLogger(__name__)


class CloudEndureModel:
    """Define the CloudEndure Model base object."""

    def __init__(self) -> None:
        """Initialize the CloudEndure Model."""
        self._valid_properties: Dict[str, Any] = {}

    @classmethod
    def _is_builtin(self, obj) -> bool:
        """Define the built-in property."""
        return isinstance(obj, (int, float, str, list, dict, bool))

    def as_dict(self) -> Dict[str, Any]:
        """Return a dict representation of the model."""
        result: Dict[Any, Any] = {}
        for key in self._valid_properties:
            val = getattr(self, key)
            if isinstance(val, datetime):
                val = val.isoformat()
            # Parse custom classes
            elif val and not CloudEndureModel._is_builtin(val):
                val = val.as_dict()
            # Parse lists of objects
            elif isinstance(val, list):
                # We only want to call as_dict in the case where the item
                # isn't a builtin type.
                for i in range(len(val)):
                    if CloudEndureModel._is_builtin(val[i]):
                        continue
                    val[i] = val[i].as_dict()
            # If it's a boolean, add it regardless of the value
            elif isinstance(val, bool):
                result[key] = val

            # Add it if it's not None
            if val:
                result[key] = val
        return result

    @classmethod
    def parse(self, json: Dict[str, Any]) -> None:
        """Parse a JSON object into a model instance."""
        raise NotImplementedError


# class CloudEndureResource(CloudEndureModel):
#     """Define the CloudEndure resource base object."""

#     RESOURCE_TYPES = (('Blueprint', 'BP'), ('Projects', 'PS'), )

#     def __init__(self, resource_type: str = ''):
#         """Initialize the CloudEndure resource."""
#         self.type: str = resource_type

#     def to_dict(self) -> Dict[str, str]:
#         """Get the dictionary representation of the object."""
#         return {
#             'resource_type': '',
#         }

# class CloudEndureBlueprint(CloudEndureResource):
#     """Define the CloudEndure Blueprint schema."""

#     def __init__(self, project_id: str = '', blueprint_id: str = ''):
#         """Initialize the CloudEndure Blueprint."""
#         self.project_id: str = project_id
#         self.blueprint_id: str = blueprint_id


class Cloud(CloudEndureModel):
    """Define the CloudEndure Cloud model schema."""

    endpoint: str = "clouds"
    _valid_properties: Dict[str, Any] = {
        # Standard Schema
        "id": "",
        "roles": [],
        "name": "",
        # Instantiation Datetimes
        "fetched_datetime": datetime.now(tzlocal()),
    }

    def __init__(self, **kwargs) -> None:
        """Initialize a new campaign instance."""
        for key, default in Cloud._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(self, json: Dict[str, Any]) -> Cloud:
        """Parse the Cloud object."""
        cloud: Cloud = self()
        return cloud


class Project(CloudEndureModel):
    """Define the CloudEndure Project model schema."""

    endpoint: str = "projects"
    _valid_properties: Dict[str, Any] = {
        # Standard Schema
        "agentInstallationToken": "",
        "cloudCredentialsIDs": [],
        "features": {
            "allowArchiving": False,
            "allowByolOnDedicatedInstance": False,
            "allowRecoveryPlans": False,
            "awsExtendedHddTypes": False,
            "drTier2": False,
            "isDemo": False,
            "pit": False,
        },
        "id": "",
        "licensesIDs": [],
        "name": "",
        "replicationReversed": False,
        "targetCloudId": "",
        "type": "",
        "userIDs": [],
        # Instantiation Datetimes
        "fetched_datetime": datetime.now(tzlocal()),
    }

    def __init__(self, **kwargs) -> None:
        """Initialize a new campaign instance."""
        for key, default in Project._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(self, json: Dict[str, Any]) -> Project:
        """Parse the Project object."""
        project: Project = self()
        return project


class Machine(CloudEndureModel):
    """Define the CloudEndure Machine model schema."""

    parent: Project = Project()
    endpoint: str = "projects/{}/machines"
    _valid_properties: Dict[str, Any] = {
        # Standard Schema
        "sourceProperties": {
            "name": "",
            "installedApplications": {
                "items": [{"applicationName": ""}],
                "lastUpdatedDateTime": "",
            },
            "disks": [{"isProtected": False, "name": "", "size": 0}],
            "machineCloudState": "",
            "publicIps": [],
            "memory": 0,
            "os": "",
            "cpu": [{"cores": 0, "modelName": ""}],
            "runningServices": {
                "items": [{"serviceName": ""}],
                "lastUpdatedDateTime": "",
            },
            "machineCloudId": "",
        },
        "replicationInfo": {
            "lastConsistencyDateTime": "",
            "nextConsistencyEstimatedDateTime": "",
            "rescannedStorageBytes": 0,
            "backloggedStorageBytes": 0,
            "initiationStates": {
                "items": [
                    {
                        "steps": [{"status": "", "message": "", "name": ""}],
                        "startDateTime": "",
                    }
                ],
                "estimatedNextAttemptDateTime": "",
            },
            "replicatedStorageBytes": 0,
            "totalStorageBytes": 0,
        },
        "license": {"startOfUseDateTime": "", "licenseId": "string"},
        "tags": [],
        "restoreServers": [],
        "fromPointInTime": {"id": "", "dateTime": ""},
        "replicationStatus": "",
        "replica": "",
        "id": "",
        "replicationConfiguration": {
            "volumeEncryptionKey": "",
            "replicationTags": [],
            "subnetHostProject": "",
            "replicationServerType": "",
            "computeLocationId": "",
            "subnetId": "",
            "logicalLocationId": "",
            "bandwidthThrottling": 0,
            "storageLocationId": "",
            "useDedicatedServer": False,
            "zone": "",
            "replicatorSecurityGroupIDs": [],
            "usePrivateIp": False,
            "proxyUrl": "",
            "volumeEncryptionAllowed": False,
            "archivingEnabled": False,
            "objectStorageLocation": "",
        },
        "lifeCycle": {
            "lastTestLaunchDateTime": "",
            "connectionEstablishedDateTime": "",
            "agentInstallationDateTime": "",
            "lastCutoverDateTime": "",
            "lastRecoveryLaunchDateTime": "",
        },
        "isAgentInstalled": False,
        # Instantiation Datetimes
        "fetched_datetime": datetime.now(tzlocal()),
    }

    def __init__(self, **kwargs) -> None:
        """Initialize a new machine instance."""
        for key, default in Project._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(self, json: Dict[str, Any]) -> Machine:
        """Parse the Machine object.

        TODO:
            * Add parsing for nested resources.

        """
        machine: Machine = self()
        # # TODO (mbeacom): Add parsing for nested resources.
        # for key, val in json.items():
        #     if key == 'some_resource':
        #         resources = [Resource.parse(resource) for resource in val]
        #         setattr(machine, key, resources)
        #     elif key == 'another_resource':
        #         if val is not None:
        #             resources = [Resource2.parse(resource) for resource in val]
        #             setattr(machine, key, resources)
        #     elif key == 'another_resource_3':
        #         setattr(machine, key, Resource3.parse(val))
        #     elif key in self._valid_properties:
        #         setattr(machine, key, val)
        return machine
