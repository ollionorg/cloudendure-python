# cloudendure_api.UserApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password_post**](UserApi.md#change_password_post) | **POST** /changePassword | Change Password
[**me_get**](UserApi.md#me_get) | **GET** /me | Me
[**users_user_id_delete**](UserApi.md#users_user_id_delete) | **DELETE** /users/{userId} | Delete a User
[**users_user_id_patch**](UserApi.md#users_user_id_patch) | **PATCH** /users/{userId} | Modify user settings

# **change_password_post**
> change_password_post(body)

Change Password

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.UserApi()
body = NULL # object |

try:
    # Change Password
    api_instance.change_password_post(body)
except ApiException as e:
    print("Exception when calling UserApi->change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **me_get**
> CloudEndureUser me_get()

Me

Provides user configuration information for the currently logged in user.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.UserApi()

try:
    # Me
    api_response = api_instance.me_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->me_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudEndureUser**](CloudEndureUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **users_user_id_delete**
> users_user_id_delete(user_id)

Delete a User

todo

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.UserApi()
user_id = 'user_id_example' # str |

try:
    # Delete a User
    api_instance.users_user_id_delete(user_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **users_user_id_patch**
> CloudEndureUser users_user_id_patch(body, user_id)

Modify user settings

Configure which projects this user can receive e-mail notifications for.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.UserApi()
body = cloudendure_api.CloudEndureUser() # CloudEndureUser |
user_id = 'user_id_example' # str |

try:
    # Modify user settings
    api_response = api_instance.users_user_id_patch(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->users_user_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureUser**](CloudEndureUser.md)|  |
 **user_id** | **str**|  |

### Return type

[**CloudEndureUser**](CloudEndureUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

