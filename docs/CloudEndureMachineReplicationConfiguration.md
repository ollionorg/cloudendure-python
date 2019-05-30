# CloudEndureMachineReplicationConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_encryption_key** | **str** | AWS only. ARN to private key for Volume Encryption. Possible values can be fetched from the Region object.  | [optional]
**replication_tags** | **list[object]** | AWS only. Tags that will be applied to every cloud resource created in the CloudEndure Staging Area. | [optional]
**subnet_host_project** | **str** | GCP only. Host project of cross project network subnet. | [optional]
**replication_server_type** | **str** |  | [optional]
**compute_location_id** | **str** | todo  vcenter only | [optional]
**subnet_id** | **str** | Subnet where replication servers will be created. Possible values can be fetched from the Region object. | [optional]
**logical_location_id** | **str** | vcenter &#x3D; vmFolder | [optional]
**bandwidth_throttling** | **int** | Mbps to use for Data Replication (zero means no throttling). | [optional]
**storage_location_id** | **str** | @todo backend creates cloudendure bla bla storage account upon need (empty string).  | [optional]
**use_dedicated_server** | **bool** |  | [optional]
**zone** | **str** | Relevant for GCP and Azure ARM. The Zone to replicate into. | [optional]
**replicator_security_group_i_ds** | **list[str]** | AWS only. The security groups that will be applied to the replication servers. Possible values can be fetched from the Region object. | [optional]
**use_private_ip** | **bool** | Should the CloudEndure agent access the replication server using its private IP address. | [optional]
**proxy_url** | **str** | The full URI for a proxy (schema, username, password, domain, port) if required for the CloudEndure agent. | [optional]
**volume_encryption_allowed** | **bool** | todo AWS only... not relevant for Backup Projects because EBS is not used | [optional]
**archiving_enabled** | **bool** |  | [optional]
**object_storage_location** | **str** | bucket in aws  | [optional]

[[Back to Model list]](API_README.md#documentation-for-models) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to README]](API_README.md)

