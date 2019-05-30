# cloudendure.cloudendure_api.AccountApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_get**](AccountApi.md#accounts_account_id_get) | **GET** /accounts/{accountId} | Get Account information

## **accounts_account_id_get**

> CloudEndureAccount accounts_account_id_get(account_id)

Get Account information

### Example

```python
from __future__ import print_function

import time

from pprint import pprint

from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException


# create an instance of the API class
api_instance = cloudendure_api.AccountApi()
account_id = 'account_id_example' # str |

try:
    # Get Account information
    api_response = api_instance.accounts_account_id_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->accounts_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |

### Return type

[**CloudEndureAccount**](CloudEndureAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

