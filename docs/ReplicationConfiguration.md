# ReplicationConfiguration

Controls the location and behaviour of the replication servers, as well as the network communication from the CloudEndure agent.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_encryption_key** | **str** | AWS only. ARN to private key for Volume Encryption. Possible values can be fetched from the Region object. | [optional] 
**replication_tags** | [**[ReplicationConfigurationReplicationTags]**](ReplicationConfigurationReplicationTags.md) | AWS only. Tags that will be applied to every cloud resource created in the CloudEndure Staging Area. | [optional] 
**disable_public_ip** | **bool** | When private IP is used, do not allocate public IP for replication server | [optional] 
**subnet_host_project** | **str** | GCP only. Host project of cross project network subnet. | [optional] 
**cost_optimized_burst_balance_delta_threshold** | **int** | when using cost optimized disk type, threshold of delta between measurments to move to default | [optional] 
**replication_software_download_source** | **str** |  | [optional] 
**cost_optimized_sc1_volumes_throughput_window_size_minutes** | **int** | when using cost optimized disk type, size of window for sc1 volumes througput measurments | [optional] 
**replication_server_type** | **str** |  | [optional] 
**cost_optimized_burst_balance_window_size_minutes** | **int** | when using cost optimized disk type, size of window for burst balance measurments | [optional] 
**use_low_cost_disks** | **bool** | use low cost disks for replication whenever possible | [optional] 
**compute_location_id** | **str** |  | [optional] 
**cloud_credentials** | **str** | The ID for the cloudCredentials object containing the credentials to be used for accessing the target cloud. | [optional] 
**subnet_id** | **str** | Subnet where replication servers will be created. Possible values can be fetched from the Region object. | [optional] 
**logical_location_id** | **str** | vcenter &#x3D; vmFolder | [optional] 
**cost_optimized_default_volumes_throughput_window_size_minutes** | **int** | when using cost optimized disk type, size of window for default volumes througput measurments | [optional] 
**bandwidth_throttling** | **int** | Mbps to use for Data Replication (zero means no throttling). | [optional] 
**cost_optimized_burst_balance_threshold** | **int** | when using cost optimized disk type, threshold of burst balance under which to move to default | [optional] 
**use_dedicated_server** | **bool** |  | [optional] 
**daily_pit_number** | **int** | Number of days to Keep PIT snapshots | [optional] 
**zone** | **str** | Relevant for GCP and Azure ARM. The Zone to replicate into. | [optional] 
**replicator_security_group_ids** | **[str]** | AWS only. The security groups that will be applied to the replication servers. Possible values can be fetched from the Region object. | [optional] 
**use_private_ip** | **bool** | Should the CloudEndure agent access the replication server using its private IP address. | [optional] 
**region** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**proxy_url** | **str** | The full URI for a proxy (schema, username, password, domain, port) if required for the CloudEndure agent. | [optional] 
**volume_encryption_allowed** | **bool** |  | [optional] 
**object_storage_location** | **str** | bucket in aws  | [optional] 
**archiving_enabled** | **bool** |  | [optional] 
**converter_type** | **str** |  | [optional] 
**storage_location_id** | **str** |  | [optional] 
**use_cost_optimized_disk_type** | **bool** | use cost optimized disk type for replication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


