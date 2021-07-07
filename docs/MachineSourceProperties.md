# MachineSourceProperties

Source machine properties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Machine name in the source environment. | [optional] 
**installed_applications** | [**MachineSourcePropertiesInstalledApplications**](MachineSourcePropertiesInstalledApplications.md) |  | [optional] 
**disks** | [**[MachineSourcePropertiesDisks]**](MachineSourcePropertiesDisks.md) | Identified disks. | [optional] 
**machine_cloud_state** | **str** | Machine current state in the source environment. | [optional] 
**public_ips** | **[str]** | Static (non-ephemral) public IPs. On some clouds this also includes ephemeral IPs. | [optional] 
**memory** | **int** | Available RAM (in Bytes). | [optional] 
**os** | **str** | Running Operating System. | [optional] 
**cpu** | [**[MachineSourcePropertiesCpu]**](MachineSourcePropertiesCpu.md) | Identified CPUs. | [optional] 
**running_services** | [**MachineSourcePropertiesRunningServices**](MachineSourcePropertiesRunningServices.md) |  | [optional] 
**machine_cloud_id** | **str** | Machine ID in the source environment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


