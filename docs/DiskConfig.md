# DiskConfig

AWS only. Replicator and/or Target machine disk properties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of disk to allocate in the target machine. COPY_ORIGIN will use the source setting. | 
**name** | **str** | Disk name as appears in the source machine object. | 
**actual_type** | **str** | The actual disk type in case of type is DEFAULT | [optional] 
**iops** | **int** |  | [optional] 
**throughput** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


