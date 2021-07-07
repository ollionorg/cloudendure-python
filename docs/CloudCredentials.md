# CloudCredentials

An object identifying the credentials used by CloudEndure to act on behalf of the user in a specific cloud.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**public_key** | **str** | The public part of the Cloud credentials. For AWS - access key ID; for GCP - user email; for Azure - SHA1 digestion of the certificate file.  | [optional] 
**account_identifier** | **str** | An ID provided by the cloud for the user account. | [optional] [readonly] 
**cloud** | **str** |  | [optional] [readonly] 
**name** | **str** | An optional (can be empty), user provided, descriptive name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


