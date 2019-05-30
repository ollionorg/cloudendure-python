# cloudendure_api.CloudCredentialsApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_credentials_creds_id_get**](CloudCredentialsApi.md#cloud_credentials_creds_id_get) | **GET** /cloudCredentials/{credsId} | Get Credentials
[**cloud_credentials_creds_id_patch**](CloudCredentialsApi.md#cloud_credentials_creds_id_patch) | **PATCH** /cloudCredentials/{credsId} | Change Credentials
[**cloud_credentials_get**](CloudCredentialsApi.md#cloud_credentials_get) | **GET** /cloudCredentials | List Credentials
[**cloud_credentials_post**](CloudCredentialsApi.md#cloud_credentials_post) | **POST** /cloudCredentials | Create Credentials

# **cloud_credentials_creds_id_get**
> CloudEndureCloudCredentials cloud_credentials_creds_id_get(creds_id)

Get Credentials

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.CloudCredentialsApi()
creds_id = 'creds_id_example' # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\".

try:
    # Get Credentials
    api_response = api_instance.cloud_credentials_creds_id_get(creds_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCredentialsApi->cloud_credentials_creds_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |

### Return type

[**CloudEndureCloudCredentials**](CloudEndureCloudCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **cloud_credentials_creds_id_patch**
> CloudEndureCloudCredentials cloud_credentials_creds_id_patch(body, creds_id)

Change Credentials

Changes the cloud credentials.  @todo:v15 If the new Cloud Credentials are to a different cloud account (or different cloud), than PATCH should fail with ??? error code and ??? error message.  Old v14 behavior: If the these cloud credentials are used with the current replication, and the new credentials are to a different cloud account (or different cloud), all agents will be uninstalled and replication will stop on them.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.CloudCredentialsApi()
body = cloudendure_api.CloudEndureCloudCredentialsRequest() # CloudEndureCloudCredentialsRequest |
creds_id = 'creds_id_example' # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\".

try:
    # Change Credentials
    api_response = api_instance.cloud_credentials_creds_id_patch(body, creds_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCredentialsApi->cloud_credentials_creds_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureCloudCredentialsRequest**](CloudEndureCloudCredentialsRequest.md)|  |
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |

### Return type

[**CloudEndureCloudCredentials**](CloudEndureCloudCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **cloud_credentials_get**
> CloudEndureCloudCredentialsList cloud_credentials_get(offset=offset, limit=limit)

List Credentials

Returns the list of cloudCredentials in the account.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.CloudCredentialsApi()
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # List Credentials
    api_response = api_instance.cloud_credentials_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCredentialsApi->cloud_credentials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

[**CloudEndureCloudCredentialsList**](CloudEndureCloudCredentialsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **cloud_credentials_post**
> CloudEndureCloudCredentials cloud_credentials_post(body)

Create Credentials

Provide the credentials with which to access the cloud API. Returns the newly created object.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.CloudCredentialsApi()
body = cloudendure_api.CloudEndureCloudCredentialsRequest() # CloudEndureCloudCredentialsRequest |

try:
    # Create Credentials
    api_response = api_instance.cloud_credentials_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudCredentialsApi->cloud_credentials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureCloudCredentialsRequest**](CloudEndureCloudCredentialsRequest.md)|  |

### Return type

[**CloudEndureCloudCredentials**](CloudEndureCloudCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

