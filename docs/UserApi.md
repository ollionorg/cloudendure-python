# cloudendure.UserApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password_post**](UserApi.md#change_password_post) | **POST** /changePassword | Change Password
[**me_get**](UserApi.md#me_get) | **GET** /me | Me
[**users_user_id_delete**](UserApi.md#users_user_id_delete) | **DELETE** /users/{userId} | Delete a User
[**users_user_id_patch**](UserApi.md#users_user_id_patch) | **PATCH** /users/{userId} | Modify user settings


# **change_password_post**
> change_password_post(password_params)

Change Password

### Example

```python
import time
import cloudendure
from cloudendure.api import user_api
from cloudendure.model.error import Error
from cloudendure.model.inline_object import InlineObject
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    password_params = InlineObject(
        new_password="new_password_example",
        old_password="old_password_example",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Change Password
        api_instance.change_password_post(password_params)
    except cloudendure.ApiException as e:
        print("Exception when calling UserApi->change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_params** | [**InlineObject**](InlineObject.md)|  |

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
**204** | Password changed successfully. |  -  |
**400** | Password change did not succeed (e.g. Old password mismatch). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_get**
> User me_get()

Me

Provides user configuration information for the currently logged in user.

### Example

```python
import time
import cloudendure
from cloudendure.api import user_api
from cloudendure.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Me
        api_response = api_instance.me_get()
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling UserApi->me_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **users_user_id_delete**
> users_user_id_delete(user_id)

Delete a User

### Example

```python
import time
import cloudendure
from cloudendure.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a User
        api_instance.users_user_id_delete(user_id)
    except cloudendure.ApiException as e:
        print("Exception when calling UserApi->users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User deleted successfully |  -  |
**409** | User is Account Owner and cannot be deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_patch**
> User users_user_id_patch(user_id, user)

Modify user settings

Configure which projects this user can receive e-mail notifications for.

### Example

```python
import time
import cloudendure
from cloudendure.api import user_api
from cloudendure.model.error import Error
from cloudendure.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "userId_example" # str | 
    user = User(
        username="username_example",
        status="PENDING",
        account="account_example",
        roles=[
            "USER",
        ],
        settings=UserSettings(
            send_notifications=UserSettingsSendNotifications(
                project_ids=[
                    "project_ids_example",
                ],
                project_ids_untested_migrations=[
                    "project_ids_untested_migrations_example",
                ],
            ),
        ),
        api_token="api_token_example",
        has_password=True,
        terms_accepted=True,
        id="id_example",
        self_link="self_link_example",
    ) # User | 

    # example passing only required values which don't have defaults set
    try:
        # Modify user settings
        api_response = api_instance.users_user_id_patch(user_id, user)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling UserApi->users_user_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **user** | [**User**](User.md)|  |

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
**200** | Object updated successfully. |  -  |
**401** | Tried patching a user different to the currently logged in one. |  -  |
**404** | Cannot apply the project ids provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

