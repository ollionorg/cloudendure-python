# cloudendure.DefaultApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_access_get**](DefaultApi.md#accounts_account_id_access_get) | **GET** /accounts/{accountId}/access | get a temporary token by email
[**extended_account_info_get**](DefaultApi.md#extended_account_info_get) | **GET** /extendedAccountInfo | Returns the extended current account information.
[**projects_assign_users_post**](DefaultApi.md#projects_assign_users_post) | **POST** /projects/assignUsers | Assign User
[**projects_project_id_audit_log_get**](DefaultApi.md#projects_project_id_audit_log_get) | **GET** /projects/{projectId}/auditLog | Get audit log
[**projects_project_id_machines_machine_id_force_rescan_post**](DefaultApi.md#projects_project_id_machines_machine_id_force_rescan_post) | **POST** /projects/{projectId}/machines/{machineId}/forceRescan | Force rescan of machine volumes.
[**projects_project_id_storage_get**](DefaultApi.md#projects_project_id_storage_get) | **GET** /projects/{projectId}/storage | project&#39;s storage
[**projects_remove_users_post**](DefaultApi.md#projects_remove_users_post) | **POST** /projects/removeUsers | Remove User
[**replace_api_token_post**](DefaultApi.md#replace_api_token_post) | **POST** /replaceApiToken | Replaces API token
[**set_password_post**](DefaultApi.md#set_password_post) | **POST** /setPassword | Set password for invited user
[**users_assign_roles_post**](DefaultApi.md#users_assign_roles_post) | **POST** /users/assignRoles | Add roles to users
[**users_post**](DefaultApi.md#users_post) | **POST** /users | Create a new User
[**users_revoke_roles_post**](DefaultApi.md#users_revoke_roles_post) | **POST** /users/revokeRoles | Revoke roles from users


# **accounts_account_id_access_get**
> InlineResponse2002 accounts_account_id_access_get(account_id, username)

get a temporary token by email

get a temporary token by email. Available for account owner when SSO is used

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.inline_response2002 import InlineResponse2002
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_id = "accountId_example" # str | 
    username = "username_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # get a temporary token by email
        api_response = api_instance.accounts_account_id_access_get(account_id, username)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->accounts_account_id_access_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **username** | **str**|  |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was processed. A one-time, time-limited token will be sent by email if conditions were met. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extended_account_info_get**
> ExtendedAccountInfo extended_account_info_get()

Returns the extended current account information.

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.extended_account_info import ExtendedAccountInfo
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the extended current account information.
        api_response = api_instance.extended_account_info_get()
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->extended_account_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExtendedAccountInfo**](ExtendedAccountInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_assign_users_post**
> projects_assign_users_post(projects_and_users)

Assign User

Assign User to Project

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.projects_and_users import ProjectsAndUsers
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    projects_and_users = ProjectsAndUsers(
        items=[
            ProjectsAndUsersItems(
                project_id="project_id_example",
                user_ids=[
                    "user_ids_example",
                ],
            ),
        ],
    ) # ProjectsAndUsers | 

    # example passing only required values which don't have defaults set
    try:
        # Assign User
        api_instance.projects_assign_users_post(projects_and_users)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->projects_assign_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_and_users** | [**ProjectsAndUsers**](ProjectsAndUsers.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users associated to Projects. |  -  |
**404** | Some of the Users or Projects do not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_audit_log_get**
> AuditLog projects_project_id_audit_log_get(project_id)

Get audit log

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.audit_log import AuditLog
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    project_id = "projectId_example" # str | 
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500
    from_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Used to limit the response to a specific date range. Must be used in conjunction with toDateTime param. (optional)
    to_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Used to limit the response to a specific date range. Must be used in conjunction with fromDateTime param. (optional)
    format = "json" # str |  (optional) if omitted the server will use the default value of "json"

    # example passing only required values which don't have defaults set
    try:
        # Get audit log
        api_response = api_instance.projects_project_id_audit_log_get(project_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->projects_project_id_audit_log_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get audit log
        api_response = api_instance.projects_project_id_audit_log_get(project_id, limit=limit, from_date_time=from_date_time, to_date_time=to_date_time, format=format)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->projects_project_id_audit_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500
 **from_date_time** | **datetime**| Used to limit the response to a specific date range. Must be used in conjunction with toDateTime param. | [optional]
 **to_date_time** | **datetime**| Used to limit the response to a specific date range. Must be used in conjunction with fromDateTime param. | [optional]
 **format** | **str**|  | [optional] if omitted the server will use the default value of "json"

### Return type

[**AuditLog**](AuditLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_machines_machine_id_force_rescan_post**
> projects_project_id_machines_machine_id_force_rescan_post(project_id, machine_id)

Force rescan of machine volumes.

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    project_id = "projectId_example" # str | 
    machine_id = "machineId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Force rescan of machine volumes.
        api_instance.projects_project_id_machines_machine_id_force_rescan_post(project_id, machine_id)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->projects_project_id_machines_machine_id_force_rescan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Force rescan applied successfully. |  -  |
**400** | Force rescan unavailable for this machine. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_storage_get**
> ProjectStorage projects_project_id_storage_get(project_id)

project's storage

get project's storage usage (vCenter only)

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.project_storage import ProjectStorage
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # project's storage
        api_response = api_instance.projects_project_id_storage_get(project_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->projects_project_id_storage_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**ProjectStorage**](ProjectStorage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_remove_users_post**
> projects_remove_users_post(projects_and_users)

Remove User

Remove User from Project

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.projects_and_users import ProjectsAndUsers
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    projects_and_users = ProjectsAndUsers(
        items=[
            ProjectsAndUsersItems(
                project_id="project_id_example",
                user_ids=[
                    "user_ids_example",
                ],
            ),
        ],
    ) # ProjectsAndUsers | 

    # example passing only required values which don't have defaults set
    try:
        # Remove User
        api_instance.projects_remove_users_post(projects_and_users)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->projects_remove_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_and_users** | [**ProjectsAndUsers**](ProjectsAndUsers.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users dis-associated from Projects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_api_token_post**
> InlineResponse2001 replace_api_token_post()

Replaces API token

Replaces API token

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Replaces API token
        api_response = api_instance.replace_api_token_post()
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->replace_api_token_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API replaced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password_post**
> set_password_post(set_password_params)

Set password for invited user

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.inline_object2 import InlineObject2
from cloudendure.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    set_password_params = InlineObject2(
        token="token_example",
        new_password="new_password_example",
    ) # InlineObject2 | 

    # example passing only required values which don't have defaults set
    try:
        # Set password for invited user
        api_instance.set_password_post(set_password_params)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->set_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_password_params** | [**InlineObject2**](InlineObject2.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Password set |  -  |
**400** | Invalid password |  -  |
**401** | Invalid setPasswordToken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_assign_roles_post**
> UsersList users_assign_roles_post(users_and_roles)

Add roles to users

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.users_and_roles import UsersAndRoles
from cloudendure.model.users_list import UsersList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    users_and_roles = UsersAndRoles(
        items=[
            UsersAndRolesItems(
                user_id="user_id_example",
                roles=[
                    "USER",
                ],
            ),
        ],
    ) # UsersAndRoles | 

    # example passing only required values which don't have defaults set
    try:
        # Add roles to users
        api_response = api_instance.users_assign_roles_post(users_and_roles)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->users_assign_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_and_roles** | [**UsersAndRoles**](UsersAndRoles.md)|  |

### Return type

[**UsersList**](UsersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changed Users. |  -  |
**404** | Some of the specified Users do not exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> User users_post(users_params)

Create a new User

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.user import User
from cloudendure.model.inline_object6 import InlineObject6
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    users_params = InlineObject6(
        username="username_example",
    ) # InlineObject6 | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new User
        api_response = api_instance.users_post(users_params)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_params** | [**InlineObject6**](InlineObject6.md)|  |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User created |  -  |
**202** | User created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_revoke_roles_post**
> UsersList users_revoke_roles_post(users_and_roles)

Revoke roles from users

### Example

```python
import time
import cloudendure
from cloudendure.api import default_api
from cloudendure.model.users_and_roles import UsersAndRoles
from cloudendure.model.users_list import UsersList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    users_and_roles = UsersAndRoles(
        items=[
            UsersAndRolesItems(
                user_id="user_id_example",
                roles=[
                    "USER",
                ],
            ),
        ],
    ) # UsersAndRoles | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke roles from users
        api_response = api_instance.users_revoke_roles_post(users_and_roles)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling DefaultApi->users_revoke_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_and_roles** | [**UsersAndRoles**](UsersAndRoles.md)|  |

### Return type

[**UsersList**](UsersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changed Users. |  -  |
**404** | Some of the specified Users do not exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

