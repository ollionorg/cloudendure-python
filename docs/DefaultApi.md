# cloudendure_api.DefaultApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_access_get**](DefaultApi.md#accounts_account_id_access_get) | **GET** /accounts/{accountId}/access | get a temporary token by email
[**extended_account_info_get**](DefaultApi.md#extended_account_info_get) | **GET** /extendedAccountInfo | Returns the extended current account information.
[**projects_assign_users_post**](DefaultApi.md#projects_assign_users_post) | **POST** /projects/assignUsers | todo
[**projects_project_id_audit_log_get**](DefaultApi.md#projects_project_id_audit_log_get) | **GET** /projects/{projectId}/auditLog | Get audit log
[**projects_project_id_storage_get**](DefaultApi.md#projects_project_id_storage_get) | **GET** /projects/{projectId}/storage | project&#x27;s storage
[**projects_remove_users_post**](DefaultApi.md#projects_remove_users_post) | **POST** /projects/removeUsers | todo
[**replace_api_token_post**](DefaultApi.md#replace_api_token_post) | **POST** /replaceApiToken | Replaces API token
[**set_password_post**](DefaultApi.md#set_password_post) | **POST** /setPassword | Set password for invited user
[**users_assign_roles_post**](DefaultApi.md#users_assign_roles_post) | **POST** /users/assignRoles | Add roles to users
[**users_post**](DefaultApi.md#users_post) | **POST** /users | Create a new User
[**users_revoke_roles_post**](DefaultApi.md#users_revoke_roles_post) | **POST** /users/revokeRoles | Add roles to users

# **accounts_account_id_access_get**
> object accounts_account_id_access_get(account_id, username)

get a temporary token by email

get a temporary token by email. Available for account owner when SSO is used

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()
account_id = 'account_id_example' # str |
username = 'username_example' # str |

try:
    # get a temporary token by email
    api_response = api_instance.accounts_account_id_access_get(account_id, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->accounts_account_id_access_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **username** | **str**|  |

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **extended_account_info_get**
> CloudEndureExtendedAccountInfo extended_account_info_get()

Returns the extended current account information.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()

try:
    # Returns the extended current account information.
    api_response = api_instance.extended_account_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->extended_account_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudEndureExtendedAccountInfo**](CloudEndureExtendedAccountInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_assign_users_post**
> projects_assign_users_post(body)

todo

todo

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()
body = cloudendure_api.CloudEndureProjectsAndUsers() # CloudEndureProjectsAndUsers |

try:
    # todo
    api_instance.projects_assign_users_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_assign_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureProjectsAndUsers**](CloudEndureProjectsAndUsers.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_audit_log_get**
> CloudEndureAuditLog projects_project_id_audit_log_get(project_id, limit=limit, from_date_time=from_date_time, to_date_time=to_date_time, format=format)

Get audit log

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()
project_id = 'project_id_example' # str |
limit = 56 # int | A number specifying how many entries to return. (optional)
from_date_time = '2013-10-20T19:20:30+01:00' # datetime | Used to limit the response to a specific date range. Must be used in conjunction with toDateTime param. (optional)
to_date_time = '2013-10-20T19:20:30+01:00' # datetime | Used to limit the response to a specific date range. Must be used in conjunction with fromDateTime param. (optional)
format = 'format_example' # str |  (optional)

try:
    # Get audit log
    api_response = api_instance.projects_project_id_audit_log_get(project_id, limit=limit, from_date_time=from_date_time, to_date_time=to_date_time, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_project_id_audit_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **limit** | **int**| A number specifying how many entries to return. | [optional]
 **from_date_time** | **datetime**| Used to limit the response to a specific date range. Must be used in conjunction with toDateTime param. | [optional]
 **to_date_time** | **datetime**| Used to limit the response to a specific date range. Must be used in conjunction with fromDateTime param. | [optional]
 **format** | **str**|  | [optional]

### Return type

[**CloudEndureAuditLog**](CloudEndureAuditLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_storage_get**
> CloudEndureProjectStorage projects_project_id_storage_get(project_id)

project's storage

get project's storage usage (vCenter only)

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()
project_id = 'project_id_example' # str |

try:
    # project's storage
    api_response = api_instance.projects_project_id_storage_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_project_id_storage_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**CloudEndureProjectStorage**](CloudEndureProjectStorage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_remove_users_post**
> projects_remove_users_post(body)

todo

todo

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()
body = cloudendure_api.CloudEndureProjectsAndUsers() # CloudEndureProjectsAndUsers |

try:
    # todo
    api_instance.projects_remove_users_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->projects_remove_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureProjectsAndUsers**](CloudEndureProjectsAndUsers.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **replace_api_token_post**
> object replace_api_token_post()

Replaces API token

Replaces API token

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()

try:
    # Replaces API token
    api_response = api_instance.replace_api_token_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_api_token_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **set_password_post**
> set_password_post(body)

Set password for invited user

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()
body = NULL # object | set password token and new password

try:
    # Set password for invited user
    api_instance.set_password_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->set_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| set password token and new password |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **users_assign_roles_post**
> CloudEndureUsersList users_assign_roles_post(body)

Add roles to users

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()
body = cloudendure_api.CloudEndureUsersAndRoles() # CloudEndureUsersAndRoles |

try:
    # Add roles to users
    api_response = api_instance.users_assign_roles_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_assign_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureUsersAndRoles**](CloudEndureUsersAndRoles.md)|  |

### Return type

[**CloudEndureUsersList**](CloudEndureUsersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **users_post**
> CloudEndureUser users_post(body)

Create a new User

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()
body = NULL # object |

try:
    # Create a new User
    api_response = api_instance.users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  |

### Return type

[**CloudEndureUser**](CloudEndureUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **users_revoke_roles_post**
> CloudEndureUsersList users_revoke_roles_post(body)

Add roles to users

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.DefaultApi()
body = cloudendure_api.CloudEndureUsersAndRoles() # CloudEndureUsersAndRoles |

try:
    # Add roles to users
    api_response = api_instance.users_revoke_roles_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_revoke_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureUsersAndRoles**](CloudEndureUsersAndRoles.md)|  |

### Return type

[**CloudEndureUsersList**](CloudEndureUsersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

