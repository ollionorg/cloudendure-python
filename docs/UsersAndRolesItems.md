# UsersAndRolesItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**roles** | **[str]** | The list of roles you want to add to the User (when used with the assignRoles API) or the list of roles you want to remove from the User (when used with the revokeRoles API). All Users have the \&quot;User\&quot; role which cannot be removed.  The following cases will be silently ignored: trying to remove the \&quot;User\&quot; role, passing an empty string as a role and using an empty array.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


