# cloudendure_api.CloudApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_credentials_creds_id_regions_get**](CloudApi.md#cloud_credentials_creds_id_regions_get) | **GET** /cloudCredentials/{credsId}/regions | List Regions
[**cloud_credentials_creds_id_regions_region_id_delete**](CloudApi.md#cloud_credentials_creds_id_regions_region_id_delete) | **DELETE** /cloudCredentials/{credsId}/regions/{regionId} | Delete region (VCenter)
[**cloud_credentials_creds_id_regions_region_id_get**](CloudApi.md#cloud_credentials_creds_id_regions_region_id_get) | **GET** /cloudCredentials/{credsId}/regions/{regionId} | Get Region
[**cloud_credentials_creds_id_regions_region_id_patch**](CloudApi.md#cloud_credentials_creds_id_regions_region_id_patch) | **PATCH** /cloudCredentials/{credsId}/regions/{regionId} | Patch region (rename)
[**clouds_get**](CloudApi.md#clouds_get) | **GET** /clouds | List Clouds

# **cloud_credentials_creds_id_regions_get**
> CloudEndureRegionsList cloud_credentials_creds_id_regions_get(creds_id, offset=offset, limit=limit)

List Regions

Returns the list of regions these credentials provide access to.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.CloudApi()
creds_id = 'creds_id_example' # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\".
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # List Regions
    api_response = api_instance.cloud_credentials_creds_id_regions_get(creds_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->cloud_credentials_creds_id_regions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

[**CloudEndureRegionsList**](CloudEndureRegionsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **cloud_credentials_creds_id_regions_region_id_delete**
> cloud_credentials_creds_id_regions_region_id_delete(creds_id, region_id)

Delete region (VCenter)

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.CloudApi()
creds_id = 'creds_id_example' # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\".
region_id = 'region_id_example' # str |

try:
    # Delete region (VCenter)
    api_instance.cloud_credentials_creds_id_regions_region_id_delete(creds_id, region_id)
except ApiException as e:
    print("Exception when calling CloudApi->cloud_credentials_creds_id_regions_region_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |
 **region_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **cloud_credentials_creds_id_regions_region_id_get**
> CloudEndureRegion cloud_credentials_creds_id_regions_region_id_get(creds_id, region_id)

Get Region

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.CloudApi()
creds_id = 'creds_id_example' # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\".
region_id = 'region_id_example' # str |

try:
    # Get Region
    api_response = api_instance.cloud_credentials_creds_id_regions_region_id_get(creds_id, region_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->cloud_credentials_creds_id_regions_region_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |
 **region_id** | **str**|  |

### Return type

[**CloudEndureRegion**](CloudEndureRegion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **cloud_credentials_creds_id_regions_region_id_patch**
> CloudEndureRegion cloud_credentials_creds_id_regions_region_id_patch(body, creds_id, region_id)

Patch region (rename)

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.CloudApi()
body = cloudendure_api.CloudEndureRegion() # CloudEndureRegion |
creds_id = 'creds_id_example' # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\".
region_id = 'region_id_example' # str |

try:
    # Patch region (rename)
    api_response = api_instance.cloud_credentials_creds_id_regions_region_id_patch(body, creds_id, region_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->cloud_credentials_creds_id_regions_region_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureRegion**](CloudEndureRegion.md)|  |
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |
 **region_id** | **str**|  |

### Return type

[**CloudEndureRegion**](CloudEndureRegion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **clouds_get**
> CloudEndureCloudsList clouds_get(offset=offset, limit=limit)

List Clouds

Returns a list of clouds that can be used with CloudEndure. The roles array determines whether this cloud can be used as source, target, or both.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.CloudApi()
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # List Clouds
    api_response = api_instance.clouds_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->clouds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

[**CloudEndureCloudsList**](CloudEndureCloudsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

