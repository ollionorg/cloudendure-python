# CloudEndureRegion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | [**list[CloudEndureSubnet]**](CloudEndureSubnet.md) |  | [optional]
**placement_groups** | **list[str]** |  | [optional]
**scsi_adapter_types** | **list[str]** | todo | [optional]
**instance_types** | **list[str]** |  | [optional]
**zones** | **list[str]** |  | [optional]
**volume_encryption_keys** | **list[str]** |  | [optional]
**cloud** | **str** |  | [optional]
**security_groups** | [**list[CloudEndureSecurityGroup]**](CloudEndureSecurityGroup.md) |  | [optional]
**logical_locations** | [**list[CloudEndureLogicalLocation]**](CloudEndureLogicalLocation.md) |  | [optional]
**static_ips** | **list[str]** |  | [optional]
**max_cpus_per_machine** | **int** | Maximum CPUs per per Target machine (currently relevant for vCenter cloud only) | [optional]
**network_interfaces** | [**list[CloudEndureNetworkInterface]**](CloudEndureNetworkInterface.md) |  | [optional]
**compute_locations** | [**list[CloudEndureComputeLocation]**](CloudEndureComputeLocation.md) | Compute location (e.g. vCenter Host) | [optional]
**name** | **str** |  | [optional]
**storage_locations** | [**list[CloudEndureStorageLocation]**](CloudEndureStorageLocation.md) | Storage location (e.g. Azure Storage Account, vCenter Data Store) | [optional]
**iam_roles** | **list[str]** |  | [optional]
**id** | **str** |  | [optional]
**max_cores_per_machine_cpu** | **int** | Maximum CPU cores per CPU in Target machines (currently relevant for vCenter cloud only) | [optional]
**dedicated_hosts** | **list[str]** |  | [optional]
**network_adapter_types** | **list[str]** | todo | [optional]
**max_mb_ram_per_machine** | **int** | Maximum MB RAM per Target machine (currently relevant for vCenter cloud only) | [optional]

[[Back to Model list]](API_README.md#documentation-for-models) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to README]](API_README.md)

