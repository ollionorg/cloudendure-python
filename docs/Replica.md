# Replica

A launched target machine (For a specific replication source).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine** | **str** | The ID of the source machine for this target machine. | [optional] 
**cloud_endure_creation_date_time** | **datetime** | Timestamp for launching this target machine. | [optional] [readonly] 
**name** | **str** | Target machine name in the target environment. | [optional] [readonly] 
**point_in_time** | **str** | The ID of the pointInTime object from which this target machine was created. | [optional] 
**job_id** | **str** |  | [optional] [readonly] 
**machine_cloud_state** | **str** | Target machine state in the target environment. | [optional] [readonly] 
**public_ips** | **[str]** | Static (non-ephemral) public IPs. On some clouds this also includes ephemeral IPs. | [optional] [readonly] 
**machine_cloud_health_checks** | **str** | Cloud healthcheck string | [optional] [readonly] 
**region_id** | **str** | The ID of the region where this target machine has been launched. | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**machine_cloud_id** | **str** | Target machine ID in the target environment. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


