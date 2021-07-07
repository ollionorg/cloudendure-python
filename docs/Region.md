# Region

A representation of a cloud region within a specific account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | [**[Subnet]**](Subnet.md) |  | [optional] 
**scsi_adapter_types** | **[str]** |  | [optional] 
**outposts** | [**[Outpost]**](Outpost.md) |  | [optional] 
**placement_groups** | **[str]** |  | [optional] 
**instance_types** | **[str]** |  | [optional] 
**logical_locations** | [**[LogicalLocation]**](LogicalLocation.md) |  | [optional] 
**zones** | **[str]** |  | [optional] 
**volume_encryption_keys** | **[str]** |  | [optional] 
**cloud** | **str** |  | [optional] 
**security_groups** | [**[SecurityGroup]**](SecurityGroup.md) |  | [optional] 
**id** | **str** |  | [optional] 
**max_cpus_per_machine** | **int** | Maximum CPUs per per Target machine (currently relevant for vCenter cloud only) | [optional] 
**network_interfaces** | [**[NetworkInterface]**](NetworkInterface.md) |  | [optional] 
**compute_locations** | [**[ComputeLocation]**](ComputeLocation.md) | Compute location (e.g. vCenter Host) | [optional] 
**name** | **str** |  | [optional] 
**storage_locations** | [**[StorageLocation]**](StorageLocation.md) | Storage location (e.g. Azure Storage Account, vCenter Data Store) | [optional] 
**iam_roles** | **[str]** |  | [optional] 
**static_ips** | **[str]** |  | [optional] 
**max_cores_per_machine_cpu** | **int** | Maximum CPU cores per CPU in Target machines (currently relevant for vCenter cloud only) | [optional] 
**dedicated_hosts** | **[str]** |  | [optional] 
**network_adapter_types** | **[str]** |  | [optional] 
**max_mb_ram_per_machine** | **int** | Maximum MB RAM per Target machine (currently relevant for vCenter cloud only) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


