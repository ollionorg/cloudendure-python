# cloudendure.CloudApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_credentials_creds_id_regions_get**](CloudApi.md#cloud_credentials_creds_id_regions_get) | **GET** /cloudCredentials/{credsId}/regions | List Regions
[**cloud_credentials_creds_id_regions_region_id_delete**](CloudApi.md#cloud_credentials_creds_id_regions_region_id_delete) | **DELETE** /cloudCredentials/{credsId}/regions/{regionId} | Delete region (VCenter)
[**cloud_credentials_creds_id_regions_region_id_get**](CloudApi.md#cloud_credentials_creds_id_regions_region_id_get) | **GET** /cloudCredentials/{credsId}/regions/{regionId} | Get Region
[**cloud_credentials_creds_id_regions_region_id_patch**](CloudApi.md#cloud_credentials_creds_id_regions_region_id_patch) | **PATCH** /cloudCredentials/{credsId}/regions/{regionId} | Patch region (rename)
[**clouds_get**](CloudApi.md#clouds_get) | **GET** /clouds | List Clouds


# **cloud_credentials_creds_id_regions_get**
> RegionsList cloud_credentials_creds_id_regions_get(creds_id)

List Regions

Returns the list of regions these credentials provide access to.

### Example

```python
import time
import cloudendure
from cloudendure.api import cloud_api
from cloudendure.model.regions_list import RegionsList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloud_api.CloudApi(api_client)
    creds_id = "credsId_example" # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\". 
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    try:
        # List Regions
        api_response = api_instance.cloud_credentials_creds_id_regions_get(creds_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling CloudApi->cloud_credentials_creds_id_regions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Regions
        api_response = api_instance.cloud_credentials_creds_id_regions_get(creds_id, offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling CloudApi->cloud_credentials_creds_id_regions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**RegionsList**](RegionsList.md)

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

# **cloud_credentials_creds_id_regions_region_id_delete**
> cloud_credentials_creds_id_regions_region_id_delete(creds_id, region_id)

Delete region (VCenter)

### Example

```python
import time
import cloudendure
from cloudendure.api import cloud_api
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloud_api.CloudApi(api_client)
    creds_id = "credsId_example" # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\". 
    region_id = "regionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete region (VCenter)
        api_instance.cloud_credentials_creds_id_regions_region_id_delete(creds_id, region_id)
    except cloudendure.ApiException as e:
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Region deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloud_credentials_creds_id_regions_region_id_get**
> Region cloud_credentials_creds_id_regions_region_id_get(creds_id, region_id)

Get Region

### Example

```python
import time
import cloudendure
from cloudendure.api import cloud_api
from cloudendure.model.region import Region
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloud_api.CloudApi(api_client)
    creds_id = "credsId_example" # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\". 
    region_id = "regionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Region
        api_response = api_instance.cloud_credentials_creds_id_regions_region_id_get(creds_id, region_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling CloudApi->cloud_credentials_creds_id_regions_region_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |
 **region_id** | **str**|  |

### Return type

[**Region**](Region.md)

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

# **cloud_credentials_creds_id_regions_region_id_patch**
> Region cloud_credentials_creds_id_regions_region_id_patch(creds_id, region_id, region)

Patch region (rename)

### Example

```python
import time
import cloudendure
from cloudendure.api import cloud_api
from cloudendure.model.region import Region
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloud_api.CloudApi(api_client)
    creds_id = "credsId_example" # str | UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\". 
    region_id = "regionId_example" # str | 
    region = Region(
        subnets=[
            Subnet(
                subnet_id="subnet_id_example",
                network_id="network_id_example",
                name="name_example",
                outpost_arn="outpost_arn_example",
            ),
        ],
        scsi_adapter_types=[
            "scsi_adapter_types_example",
        ],
        outposts=[
            Outpost(
                outpost_arn="outpost_arn_example",
                instance_types=[
                    "instance_types_example",
                ],
                error="error_example",
            ),
        ],
        placement_groups=[
            "placement_groups_example",
        ],
        instance_types=[],
        logical_locations=[
            LogicalLocation(
                location_id="location_id_example",
                name="name_example",
            ),
        ],
        zones=[
            "zones_example",
        ],
        volume_encryption_keys=[
            "volume_encryption_keys_example",
        ],
        cloud="cloud_example",
        security_groups=[
            SecurityGroup(
                network_id="network_id_example",
                security_group_id="security_group_id_example",
                name="name_example",
            ),
        ],
        id="id_example",
        max_cpus_per_machine=1,
        network_interfaces=[
            NetworkInterface(
                subnet_id="subnet_id_example",
                name="name_example",
                private_ip="private_ip_example",
            ),
        ],
        compute_locations=[
            ComputeLocation(
                is_encryption_supported=True,
                location_id="location_id_example",
                name="name_example",
            ),
        ],
        name="name_example",
        storage_locations=[
            StorageLocation(
                location_id="location_id_example",
                name="name_example",
            ),
        ],
        iam_roles=[
            "iam_roles_example",
        ],
        static_ips=[
            "static_ips_example",
        ],
        max_cores_per_machine_cpu=1,
        dedicated_hosts=[
            "dedicated_hosts_example",
        ],
        network_adapter_types=[
            "network_adapter_types_example",
        ],
        max_mb_ram_per_machine=1,
    ) # Region | 

    # example passing only required values which don't have defaults set
    try:
        # Patch region (rename)
        api_response = api_instance.cloud_credentials_creds_id_regions_region_id_patch(creds_id, region_id, region)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling CloudApi->cloud_credentials_creds_id_regions_region_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **str**| UUID of the credentials to use. In case of on-premise, you should use the null UUID \&quot;00000000-0000-0000-0000-000000000000\&quot;.  |
 **region_id** | **str**|  |
 **region** | [**Region**](Region.md)|  |

### Return type

[**Region**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Renamed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clouds_get**
> CloudsList clouds_get()

List Clouds

Returns a list of clouds that can be used with CloudEndure. The roles array determines whether this cloud can be used as source, target, or both.

### Example

```python
import time
import cloudendure
from cloudendure.api import cloud_api
from cloudendure.model.clouds_list import CloudsList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloud_api.CloudApi(api_client)
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Clouds
        api_response = api_instance.clouds_get(offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling CloudApi->clouds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**CloudsList**](CloudsList.md)

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

