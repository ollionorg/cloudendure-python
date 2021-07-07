# cloudendure.LicensingApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licenses_get**](LicensingApi.md#licenses_get) | **GET** /licenses | List Licenses
[**licenses_license_id_get**](LicensingApi.md#licenses_license_id_get) | **GET** /licenses/{licenseId} | Get License


# **licenses_get**
> LicenseList licenses_get()

List Licenses

Returns the list of licenses currently associated with this user.

### Example

```python
import time
import cloudendure
from cloudendure.api import licensing_api
from cloudendure.model.license_list import LicenseList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = licensing_api.LicensingApi(api_client)
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Licenses
        api_response = api_instance.licenses_get(offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling LicensingApi->licenses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**LicenseList**](LicenseList.md)

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

# **licenses_license_id_get**
> License licenses_license_id_get(license_id)

Get License

### Example

```python
import time
import cloudendure
from cloudendure.api import licensing_api
from cloudendure.model.license import License
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = licensing_api.LicensingApi(api_client)
    license_id = "licenseId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get License
        api_response = api_instance.licenses_license_id_get(license_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling LicensingApi->licenses_license_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**|  |

### Return type

[**License**](License.md)

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

