# Project

Contains the project characteristics such as the replicationConfiguration in use, source region and project type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_configuration** | **str** | The ID of the replication configuration object to use (corresponding to the ones available in /projects/{projectId}/replicationConfigurations). | [optional] 
**features** | [**ProjectFeatures**](ProjectFeatures.md) |  | [optional] 
**replication_reversed** | **bool** |  | [optional] [readonly] 
**cloud_credentials_ids** | **[str]** | The IDs of the cloud credentials to use (array of one). | [optional] 
**source_region** | **str** | The ID of the region to use as source. | [optional] 
**id** | **str** |  | [optional] [readonly] 
**target_cloud_id** | **str** |  | [optional] 
**agent_installation_token** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**users_ids** | **[str]** |  | [optional] 
**type** | **str** |  | [optional] 
**source_cloud_credentials_id** | **str** |  | [optional] [readonly] 
**target_cloud_credentials_id** | **str** |  | [optional] [readonly] 
**licenses_ids** | **[str]** | The IDs of the licenses associated with this project (array of one). | [optional] 
**ce_admin_properties** | [**ProjectCeAdminProperties**](ProjectCeAdminProperties.md) |  | [optional] 
**source_cloud_id** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


