# Machine

A machine on which a CloudEndure agent has been installed (Replication source).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_source_cloud_id** | **str** | The cloud id of the source machine from which a machine was originally replicated from. | [optional] [readonly] 
**source_properties** | [**MachineSourceProperties**](MachineSourceProperties.md) |  | [optional] 
**replication_info** | [**MachineReplicationInfo**](MachineReplicationInfo.md) |  | [optional] 
**license** | [**MachineLicense**](MachineLicense.md) |  | [optional] 
**tags** | **[str]** |  | [optional] 
**restore_servers** | **[str]** | RestoreServer IDs  | [optional] 
**from_point_in_time** | [**PointInTime**](PointInTime.md) |  | [optional] 
**replication_status** | **str** | Is replication started, paused or stopped | [optional] 
**replica** | **str** | The ID of the target machine that has been previously launched, if such exists. | [optional] 
**id** | **str** |  | [optional] 
**replication_configuration** | [**MachineReplicationConfiguration**](MachineReplicationConfiguration.md) |  | [optional] 
**life_cycle** | [**MachineLifeCycle**](MachineLifeCycle.md) |  | [optional] 
**is_agent_installed** | **bool** | Whether a CloudEndure agent is currently installed on this machine. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


