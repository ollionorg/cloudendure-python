# User

Contains the user identification properties such as e-mail address and Installation Token as well as user preferences.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**status** | **str** |  | [optional] [readonly] 
**account** | **str** |  | [optional] [readonly] 
**roles** | **[str]** |  | [optional] [readonly] 
**settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**api_token** | **str** |  | [optional] [readonly] 
**has_password** | **bool** |  | [optional] 
**terms_accepted** | **bool** | one-way; cannot be set at time of POST | [optional] 
**id** | **str** |  | [optional] [readonly] 
**self_link** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


