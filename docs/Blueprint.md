# Blueprint

Target machine characteristics: machine and disk types, network configuration, etc.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam_role** | **str** | AWS only. Possible values can be fetched from the Region object. | [optional] 
**scsi_adapter_type** | **str** | Currently relevant for vCenter cloud only. Possible values can be fetched from the Region object. | [optional] 
**public_ip_action** | **str** | Whether to allocate an ephemeral public IP, or not. AS_SUBNET causes CloudEndure to copy this property from the source machine. | [optional] 
**machine_name** | **str** |  | [optional] 
**cpus** | **int** | Number of CPUs per per Target machine; Currently relevant for vCenter cloud only; Max value can be fetched from the maxCpusPerMachine property of the Region object.  | [optional] 
**security_group_ids** | **[str]** | AWS only. The security groups that will be applied to the target machine. Possible values can be fetched from the Region object. | [optional] 
**run_after_launch** | **bool** | AWS only. Whether to power on the launched target machine after launch. True by default. | [optional] 
**recommended_private_ip** | **str** | The private IP address recommended for use with this machine. | [optional] [readonly] 
**instance_type** | **str** | Possible values can be fetched from the Region object, plus special values \&quot;COPY_ORIGIN\&quot; or \&quot;CUSTOM\&quot; | [optional] 
**mb_ram** | **int** | MB RAM per Target machine; Currently relevant for vCenter cloud only; Max value can be fetched from the maxMbRamPerMachine property of the Region object.  | [optional] 
**network_interface** | **str** |  | [optional] 
**subnet_ids** | **[str]** | AWS only. Configures a subnets in which the instance network interface will take part. Possible values can be fetched from the Region object. | [optional] 
**cores_per_cpu** | **int** | Number of CPU cores per CPU in Target machine; Currently relevant for vCenter cloud only. | [optional] 
**recommended_instance_type** | **str** | When instance rightsizing is enabled, the instance type suitable for the source machine&#39;s HW | [optional] [readonly] 
**force_uefi** | **bool** |  | [optional] 
**static_ip** | **str** | Possible values can be fetched from the Region object. | [optional] 
**launch_on_instance_id** | **str** | instance id for target machine managed by AMS. | [optional] 
**tags** | [**[ReplicationConfigurationReplicationTags]**](ReplicationConfigurationReplicationTags.md) | AWS only. Tags that will be applied to the target machine. | [optional] 
**security_group_action** | **str** | How to assign a security group to the target machine. | [optional]  if omitted the server will use the default value of "FROM_POLICY"
**private_ips** | **[str]** |  | [optional] 
**tenancy** | **str** |  | [optional] 
**compute_location_id** | **str** |  | [optional] 
**subnets_host_project** | **str** | GCP only. Host project for cross project network subnet. | [optional] 
**logical_location_id** | **str** | vcenter &#x3D; vmFolder; relates to $ref LogicalLocation | [optional] 
**network_adapter_type** | **str** | Currently relevant for vCenter cloud only. Possible values can be fetched from the Region object. | [optional] 
**byol_on_dedicated_instance** | **bool** | specifies whether to use byol windows license if dedicated instance tenancy is selected. | [optional] 
**placement_group** | **str** | AWS only. Possible values can be fetched from the Region object. | [optional] 
**machine_id** | **str** |  | [optional] [readonly] 
**region** | **str** |  | [optional] [readonly] 
**disks** | [**[BlueprintDisks]**](BlueprintDisks.md) | AWS only. Target machine disk properties. | [optional] 
**private_ip_action** | **str** |  | [optional] 
**static_ip_action** | **str** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**dedicated_host_identifier** | **str** |  | [optional] 
**use_shared_ram** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


