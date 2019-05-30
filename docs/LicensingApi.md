# cloudendure_api.LicensingApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licenses_get**](LicensingApi.md#licenses_get) | **GET** /licenses | List Licenses
[**licenses_license_id_get**](LicensingApi.md#licenses_license_id_get) | **GET** /licenses/{licenseId} | Get License

# **licenses_get**
> CloudEndureLicenseList licenses_get(offset=offset, limit=limit)

List Licenses

Returns the list of licenses currently associated with this user.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.LicensingApi()
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # List Licenses
    api_response = api_instance.licenses_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->licenses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

[**CloudEndureLicenseList**](CloudEndureLicenseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **licenses_license_id_get**
> CloudEndureLicense licenses_license_id_get(license_id)

Get License

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.LicensingApi()
license_id = 'license_id_example' # str |

try:
    # Get License
    api_response = api_instance.licenses_license_id_get(license_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->licenses_license_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**|  |

### Return type

[**CloudEndureLicense**](CloudEndureLicense.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

