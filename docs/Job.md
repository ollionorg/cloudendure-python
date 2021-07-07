# Job

An asynchoronous job running in the backend. A single job can run at any given time for a specific project.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**participating_machines** | **[str]** |  | [optional] 
**log** | [**[JobLog]**](JobLog.md) |  | [optional] 
**type** | **str** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 
**target_machines** | [**[JobTargetMachine]**](JobTargetMachine.md) |  | [optional] 
**creation_date_time** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**initiated_by** | **str** | username of user who initiated the job | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


