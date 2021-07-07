# cloudendure.AuthenticationApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_post**](AuthenticationApi.md#login_post) | **POST** /login | Login
[**logout_post**](AuthenticationApi.md#logout_post) | **POST** /logout | Logout


# **login_post**
> User login_post(login_info)

Login

Upon successful authentication, this method returns a session identifier cookie that can be used to authenticate subsequent API calls. 

### Example

```python
import time
import cloudendure
from cloudendure.api import authentication_api
from cloudendure.model.inline_object1 import InlineObject1
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
    api_instance = authentication_api.AuthenticationApi(api_client)
    login_info = InlineObject1(
        username="username_example",
        login_token="login_token_example",
        user_api_token="user_api_token_example",
        agent_installation_token="agent_installation_token_example",
        password="password_example",
        account_identifier="account_identifier_example",
        google_oauth_code="google_oauth_code_example",
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Login
        api_response = api_instance.login_post(login_info)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling AuthenticationApi->login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_info** | [**InlineObject1**](InlineObject1.md)|  |

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
**200** | Login successful. |  -  |
**307** | A different endpoint is required to service this user. A redirect address is provided to where subsequent calls should go.  |  -  |
**401** | The login credentials provided cannot be authenticated. |  -  |
**402** | There is no active license configured for this account (A license must be purchased or extended). |  -  |
**429** | Authentication failure limit has been reached. The service will become available for additional requests after a timeout.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_post**
> logout_post()

Logout

Invalidates the session identifier associated with this session.

### Example

```python
import time
import cloudendure
from cloudendure.api import authentication_api
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Logout
        api_instance.logout_post()
    except cloudendure.ApiException as e:
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Logout successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

