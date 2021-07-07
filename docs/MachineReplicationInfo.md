# MachineReplicationInfo

Detailed information on the state of replication.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rescanned_storage_bytes** | **int** | Amount of data rescanned (in Bytes). | [optional] 
**backlogged_storage_bytes** | **int** | Amount of data requiring sync (in Bytes), that has not yet been sent. | [optional] 
**failback_client_last_seen_date_time** | **datetime** |  | [optional] 
**last_consistency_date_time** | **datetime** | Timestamp of last disk replication consistency event. | [optional] 
**next_consistency_estimated_date_time** | **datetime** | Timestamp of estimate for the next disk replication consistency event. | [optional] 
**total_storage_bytes** | **int** | Total storage being replicated (in Bytes). | [optional] 
**initiation_states** | [**MachineReplicationInfoInitiationStates**](MachineReplicationInfoInitiationStates.md) |  | [optional] 
**replicated_storage_bytes** | **int** | Amount of data already synced (in Bytes). | [optional] 
**last_seen_date_time** | **datetime** |  | [optional] 
**last_scan_start_date_time** | **datetime** | Timestamp of last time a volume scan has started. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


