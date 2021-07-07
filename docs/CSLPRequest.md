# CSLPRequest

CLSP (Conversion Scripts Live Patching) 'post' operation request parameters
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script_names** | **[str]** | list of names relative to conversion_scripts sub-folder as a query filter parameter | [optional] 
**live_patch_comment** | **str** | script live patch reason - like &#39;git comment&#39; | [optional] 
**operation** | **str** | one of hard-coded labels in the CSLPOperation enum | [optional] 
**ce_version** | **str** | management version query filter parameter | [optional] 
**script_items** | [**[CSLPItem]**](CSLPItem.md) | list of input script items (tbd) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


