# cloudendure_api.AuthenticationApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_post**](AuthenticationApi.md#login_post) | **POST** /login | Login
[**logout_post**](AuthenticationApi.md#logout_post) | **POST** /logout | Logout

# **login_post**
> CloudEndureUser login_post(body)

Login

@todo: fix re use of XSRF-TOKEN cookie + X-XSRF-TOKEN header Upon successful authentication, this method returns a session identifier cookie that can be used to authenticate subsequent API calls.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.AuthenticationApi()
body = NULL # object | Login info

try:
    # Login
    api_response = api_instance.login_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Login info |

### Return type

[**CloudEndureUser**](CloudEndureUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **logout_post**
> logout_post()

Logout

Invalidates the session identifier associated with this session.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.AuthenticationApi()

try:
    # Logout
    api_instance.logout_post()
except ApiException as e:
    print("Exception when calling AuthenticationApi->logout_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

