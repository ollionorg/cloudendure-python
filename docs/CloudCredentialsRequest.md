# CloudCredentialsRequest

The credentials with which CloudEndure acts on behalf of the user in a specific cloud.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **str** |  | 
**public_key** | **str** | The public part of the Cloud credentials. For AWS - The access key ID, For GCP and Azure - N/A. | [optional] 
**name** | **str** | An optional (can be empty), user provided, descriptive name. | [optional] 
**private_key** | **str** | Cloud credentials secret, Base64-encoded. For AWS - The secret access key, For GCP - The private key in JSON format, For Azure - The certificate file. | [optional] 
**account_identifier** | **str** | Cloud account identifier. For AWS - N/A, For GCP - The project ID, For Azure - The subscription ID. | [optional] 
**id** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


