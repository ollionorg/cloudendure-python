# cloudendure.CloudCredentialsApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_credentials_creds_id_get**](CloudCredentialsApi.md#cloud_credentials_creds_id_get) | **GET** /cloudCredentials/{credsId} | Get Credentials
[**cloud_credentials_creds_id_patch**](CloudCredentialsApi.md#cloud_credentials_creds_id_patch) | **PATCH** /cloudCredentials/{credsId} | Change Credentials
[**cloud_credentials_get**](CloudCredentialsApi.md#cloud_credentials_get) | **GET** /cloudCredentials | List Credentials
[**cloud_credentials_post**](CloudCredentialsApi.md#cloud_credentials_post) | **POST** /cloudCredentials | Create Credentials


# **cloud_credentials_creds_id_get**
> CloudCredentials cloud_credentials_creds_id_get(creds_id)

Get Credentials

### Example

```python
import time
import cloudendure
from cloudendure.api import cloud_credentials_api
from cloudendure.model.cloud_credentials import CloudCredentials
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloud_credentials_api.CloudCredentialsApi(api_client)
    creds_id = "credsId_example" # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\". 

    # example passing only required values which don't have defaults set
    try:
        # Get Credentials
        api_response = api_instance.cloud_credentials_creds_id_get(creds_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling CloudCredentialsApi->cloud_credentials_creds_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |

### Return type

[**CloudCredentials**](CloudCredentials.md)

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

# **cloud_credentials_creds_id_patch**
> CloudCredentials cloud_credentials_creds_id_patch(creds_id, cloud_credentials)

Change Credentials

Changes the cloud credentials. 

### Example

```python
import time
import cloudendure
from cloudendure.api import cloud_credentials_api
from cloudendure.model.cloud_credentials import CloudCredentials
from cloudendure.model.cloud_credentials_request import CloudCredentialsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloud_credentials_api.CloudCredentialsApi(api_client)
    creds_id = "credsId_example" # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\". 
    cloud_credentials = CloudCredentialsRequest(
        public_key="public_key_example",
        name="name_example",
        cloud_id="cloud_id_example",
        private_key='YQ==',
        account_identifier="account_identifier_example",
        id="id_example",
    ) # CloudCredentialsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Change Credentials
        api_response = api_instance.cloud_credentials_creds_id_patch(creds_id, cloud_credentials)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling CloudCredentialsApi->cloud_credentials_creds_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |
 **cloud_credentials** | [**CloudCredentialsRequest**](CloudCredentialsRequest.md)|  |

### Return type

[**CloudCredentials**](CloudCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloud_credentials_get**
> CloudCredentialsList cloud_credentials_get()

List Credentials

Returns the list of cloudCredentials in the account.

### Example

```python
import time
import cloudendure
from cloudendure.api import cloud_credentials_api
from cloudendure.model.cloud_credentials_list import CloudCredentialsList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloud_credentials_api.CloudCredentialsApi(api_client)
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Credentials
        api_response = api_instance.cloud_credentials_get(offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling CloudCredentialsApi->cloud_credentials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**CloudCredentialsList**](CloudCredentialsList.md)

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

# **cloud_credentials_post**
> CloudCredentials cloud_credentials_post(cloud_credentials)

Create Credentials

Provide the credentials with which to access the cloud API. Returns the newly created object.

### Example

```python
import time
import cloudendure
from cloudendure.api import cloud_credentials_api
from cloudendure.model.cloud_credentials import CloudCredentials
from cloudendure.model.cloud_credentials_request import CloudCredentialsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloud_credentials_api.CloudCredentialsApi(api_client)
    cloud_credentials = CloudCredentialsRequest(
        public_key="public_key_example",
        name="name_example",
        cloud_id="cloud_id_example",
        private_key='YQ==',
        account_identifier="account_identifier_example",
        id="id_example",
    ) # CloudCredentialsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Credentials
        api_response = api_instance.cloud_credentials_post(cloud_credentials)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling CloudCredentialsApi->cloud_credentials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_credentials** | [**CloudCredentialsRequest**](CloudCredentialsRequest.md)|  |

### Return type

[**CloudCredentials**](CloudCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New object successfully created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

