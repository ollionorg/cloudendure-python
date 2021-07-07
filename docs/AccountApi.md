# cloudendure.AccountApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_get**](AccountApi.md#accounts_account_id_get) | **GET** /accounts/{accountId} | Get Account information


# **accounts_account_id_get**
> Account accounts_account_id_get(account_id)

Get Account information

### Example

```python
import time
import cloudendure
from cloudendure.api import account_api
from cloudendure.model.account import Account
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Account information
        api_response = api_instance.accounts_account_id_get(account_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling AccountApi->accounts_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

