# CloudEndureBlueprint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam_role** | **str** | AWS only. Possible values can be fetched from the Region object. | [optional]
**scsi_adapter_type** | **str** | Currently relevant for vCenter cloud only. Possible values can be fetched from the Region object. | [optional]
**public_ip_action** | **str** | Whether to allocate an ephemeral public IP, or not. AS_SUBNET causes CloudEndure to copy this property from the source machine. | [optional]
**machine_name** | **str** |  | [optional]
**cpus** | **int** | Number of CPUs per per Target machine; Currently relevant for vCenter cloud only; Max value can be fetched from the maxCpusPerMachine property of the Region object.  | [optional]
**security_group_i_ds** | **list[str]** | AWS only. The security groups that will be applied to the target machine. Possible values can be fetched from the Region object. | [optional]
**run_after_launch** | **bool** | AWS only. Whether to power on the launched target machine after launch. True by default. | [optional]
**recommended_private_ip** | **str** | The private IP address recommended for use with this machine. | [optional]
**network_interface** | **str** |  | [optional]
**id** | **str** |  | [optional]
**mb_ram** | **int** | MB RAM per Target machine; Currently relevant for vCenter cloud only; Max value can be fetched from the maxMbRamPerMachine property of the Region object.  | [optional]
**instance_type** | **str** | Possible values can be fetched from the Region object, plus special values \&quot;COPY_ORIGIN\&quot; or \&quot;CUSTOM\&quot; | [optional]
**subnet_i_ds** | **list[str]** | AWS only. Configures a subnets in which the instance network interface will take part. Possible values can be fetched from the Region object. | [optional]
**cores_per_cpu** | **int** | Number of CPU cores per CPU in Target machine; Currently relevant for vCenter cloud only. | [optional]
**recommended_instance_type** | **str** | When instance rightsizing is enabled, the instance type suitable for the source machine&#x27;s HW | [optional]
**static_ip** | **str** | Possible values can be fetched from the Region object. | [optional]
**tags** | **list[object]** | AWS only. Tags that will be applied to the target machine. | [optional]
**security_group_action** | **str** | How to assign a security group to the target machine. | [optional]
**private_i_ps** | **list[str]** |  | [optional]
**tenancy** | **str** |  | [optional]
**compute_location_id** | **str** | todo | [optional]
**subnets_host_project** | **str** | GCP only. Host project for cross project network subnet. | [optional]
**logical_location_id** | **str** | vcenter &#x3D; vmFolder; relates to $ref LogicalLocation | [optional]
**network_adapter_type** | **str** | Currently relevant for vCenter cloud only. Possible values can be fetched from the Region object. | [optional]
**byol_on_dedicated_instance** | **bool** | specifies whether to use byol windows license if dedicated instance tenancy is selected. | [optional]
**placement_group** | **str** | AWS only. Possible values can be fetched from the Region object. | [optional]
**machine_id** | **str** |  | [optional]
**region** | **str** |  | [optional]
**disks** | **list[object]** | AWS only. Target machine disk properties. | [optional]
**private_ip_action** | **str** |  | [optional]
**static_ip_action** | **str** |  | [optional]
**dedicated_host_identifier** | **str** |  | [optional]
**use_shared_ram** | **bool** | todo | [optional]

[[Back to Model list]](API_README.md#documentation-for-models) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to README]](API_README.md)

