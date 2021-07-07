# CSLPItem

defines CLSP (Conversion Scripts Live Patching) single script item 1-1 to DB item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_patch_comment** | **str** | script live patch reason - like &#39;git comment&#39; | [optional] 
**ce_versions** | **[str]** | all management versions for this specific script content | [optional] 
**live_patch_type** | **str** | type of the live patch in DB | [optional] 
**script_text** | **str** | multi-line script text | [optional] 
**sha256sum_orig** | **str** | SHA-256 of the not runnable script with &#39;constants.CE_DOMAIN_KEY&#39; placeholder (empty CE DNS as stored in git source control) | [optional] 
**script_name** | **str** | name relative to conversion_scripts sub-folder, eg. \&quot;windows/postboot/setup_win_replica.bat\&quot; | [optional] 
**sha256sum** | **str** | SHA-256 of the runnable script with actual CE DNS replacing &#39;constants.CE_DOMAIN_KEY&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


