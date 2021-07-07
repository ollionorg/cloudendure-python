# License

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total number of licenses. | [optional] 
**duration_from_start_of_use** | **str** | Validity period for a a single license from the time of agent installation. | [optional] 
**used** | **int** | How many licenses have already been consumed. | [optional] [readonly] 
**features** | [**LicenseFeatures**](LicenseFeatures.md) |  | [optional] 
**expiration_date_time** | **datetime** |  | [optional] 
**ce_admin_properties** | [**LicenseCeAdminProperties**](LicenseCeAdminProperties.md) |  | [optional] 
**type** | **str** | License type. DR licenses can be moved from one machine to another. Migration licenses are consumed upon installation. | [optional] 
**id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


