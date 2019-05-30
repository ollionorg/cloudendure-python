# CloudEndureReplica

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine** | **str** | The ID of the source machine for this target machine. | [optional]
**cloud_endure_creation_date_time** | **datetime** | Timestamp for launching this target machine. | [optional]
**name** | **str** | Target machine name in the target environment. | [optional]
**point_in_time** | **str** | The ID of the pointInTime object from which this target machine was created. | [optional]
**machine_cloud_state** | **str** | Target machine state in the target environment. | [optional]
**public_ips** | **list[str]** | Static (non-ephemral) public IPs. On some clouds this also includes ephemeral IPs. | [optional]
**region_id** | **str** | The ID of the region where this target machine has been launched. | [optional]
**id** | **str** |  | [optional]
**machine_cloud_id** | **str** | Target machine ID in the target environment. | [optional]

[[Back to Model list]](API_README.md#documentation-for-models) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to README]](API_README.md)

