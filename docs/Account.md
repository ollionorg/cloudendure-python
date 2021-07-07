# Account

Contains the account identifier which is referenced by other resources, as well as feature information for the account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_credentials_api** | **bool** | used to enable targetCloudCredentials. This API should be replaced soon. | [optional] 
**allow_archiving_default_value** | **bool** |  | [optional] 
**per_account_user_pool** | **bool** |  | [optional] 
**default_license_type** | **str** |  | [optional] [readonly] 
**is_med_one** | **bool** |  | [optional] 
**id** | **str** | UUID of the account | [optional] [readonly] 
**invite_token_expiry_minutes** | **int** |  | [optional] 
**is_gcp_self_service** | **bool** |  | [optional] [readonly] 
**is_dr_trial** | **bool** |  | [optional] [readonly] 
**is_arm_self_service** | **bool** |  | [optional] [readonly] 
**is_aws_self_service** | **bool** |  | [optional] [readonly] 
**saml_settings** | [**SamlSettings**](SamlSettings.md) |  | [optional] 
**is_right_sizing_enabled** | **bool** |  | [optional] 
**max_projects_allowed** | **int** |  | [optional] 
**ce_admin_properties** | [**AccountCeAdminProperties**](AccountCeAdminProperties.md) |  | [optional] 
**owner_id** | **str** | Account Owner (a User) | [optional] 
**creation_datetime** | **datetime** | Date and time in which account was created | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


