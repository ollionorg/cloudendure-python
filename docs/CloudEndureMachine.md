# CloudEndureMachine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_properties** | **object** | Source machine properties. | [optional]
**replication_info** | **object** | Detailed information on the state of replication. | [optional]
**license** | **object** | Detailed machine license consumption information. | [optional]
**tags** | **list[str]** |  | [optional]
**restore_servers** | **list[str]** | todo restoreServer ids | [optional]
**from_point_in_time** | [**CloudEndurePointInTime**](CloudEndurePointInTime.md) |  | [optional]
**replication_status** | **str** | Is replication started, paused or stopped | [optional]
**replica** | **str** | The ID of the target machine that has been previously launched, if such exists. | [optional]
**id** | **str** |  | [optional]
**replication_configuration** | [**CloudEndureMachineReplicationConfiguration**](CloudEndureMachineReplicationConfiguration.md) |  | [optional]
**life_cycle** | **object** | Detailed machine lifecycle information. | [optional]
**is_agent_installed** | **bool** | Whether a CloudEndure agent is currently installed on this machine. | [optional]

[[Back to Model list]](API_README.md#documentation-for-models) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to README]](API_README.md)

