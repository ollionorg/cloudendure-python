# cloudendure.ReplicationApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_machines_machine_id_bandwidth_throttling_get**](ReplicationApi.md#projects_project_id_machines_machine_id_bandwidth_throttling_get) | **GET** /projects/{projectId}/machines/{machineId}/bandwidthThrottling | Get value of network bandwidth throttling setting for Machine
[**projects_project_id_machines_machine_id_bandwidth_throttling_patch**](ReplicationApi.md#projects_project_id_machines_machine_id_bandwidth_throttling_patch) | **PATCH** /projects/{projectId}/machines/{machineId}/bandwidthThrottling | Set value of network bandwidth throttling setting for Machine
[**projects_project_id_machines_machine_id_delete**](ReplicationApi.md#projects_project_id_machines_machine_id_delete) | **DELETE** /projects/{projectId}/machines/{machineId} | Uninstall agent
[**projects_project_id_machines_machine_id_pointsintime_get**](ReplicationApi.md#projects_project_id_machines_machine_id_pointsintime_get) | **GET** /projects/{projectId}/machines/{machineId}/pointsintime | List Available Points-in-time
[**projects_project_id_replication_configurations_get**](ReplicationApi.md#projects_project_id_replication_configurations_get) | **GET** /projects/{projectId}/replicationConfigurations | List Replication Configurations
[**projects_project_id_replication_configurations_post**](ReplicationApi.md#projects_project_id_replication_configurations_post) | **POST** /projects/{projectId}/replicationConfigurations | Create Replication Configuration
[**projects_project_id_replication_configurations_replication_configuration_id_patch**](ReplicationApi.md#projects_project_id_replication_configurations_replication_configuration_id_patch) | **PATCH** /projects/{projectId}/replicationConfigurations/{replicationConfigurationId} | Modify Replication Configuration


# **projects_project_id_machines_machine_id_bandwidth_throttling_get**
> BandwidthThrottling projects_project_id_machines_machine_id_bandwidth_throttling_get(project_id, machine_id)

Get value of network bandwidth throttling setting for Machine

### Example

```python
import time
import cloudendure
from cloudendure.api import replication_api
from cloudendure.model.bandwidth_throttling import BandwidthThrottling
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)
    project_id = "projectId_example" # str | 
    machine_id = "machineId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get value of network bandwidth throttling setting for Machine
        api_response = api_instance.projects_project_id_machines_machine_id_bandwidth_throttling_get(project_id, machine_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ReplicationApi->projects_project_id_machines_machine_id_bandwidth_throttling_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |

### Return type

[**BandwidthThrottling**](BandwidthThrottling.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_machines_machine_id_bandwidth_throttling_patch**
> BandwidthThrottling projects_project_id_machines_machine_id_bandwidth_throttling_patch(project_id, machine_id, bandwidth_throttling)

Set value of network bandwidth throttling setting for Machine

### Example

```python
import time
import cloudendure
from cloudendure.api import replication_api
from cloudendure.model.bandwidth_throttling import BandwidthThrottling
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)
    project_id = "projectId_example" # str | 
    machine_id = "machineId_example" # str | 
    bandwidth_throttling = BandwidthThrottling(
        bandwidth_throttling=1,
    ) # BandwidthThrottling | 

    # example passing only required values which don't have defaults set
    try:
        # Set value of network bandwidth throttling setting for Machine
        api_response = api_instance.projects_project_id_machines_machine_id_bandwidth_throttling_patch(project_id, machine_id, bandwidth_throttling)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ReplicationApi->projects_project_id_machines_machine_id_bandwidth_throttling_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |
 **bandwidth_throttling** | [**BandwidthThrottling**](BandwidthThrottling.md)|  |

### Return type

[**BandwidthThrottling**](BandwidthThrottling.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_machines_machine_id_delete**
> projects_project_id_machines_machine_id_delete(project_id, machine_id)

Uninstall agent

Stops replication and removes the cloudendure agent from this machine. All cloud artifacts associated with those machines with the exception of launched target machine are deleted.

### Example

```python
import time
import cloudendure
from cloudendure.api import replication_api
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)
    project_id = "projectId_example" # str | 
    machine_id = "machineId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Uninstall agent
        api_instance.projects_project_id_machines_machine_id_delete(project_id, machine_id)
    except cloudendure.ApiException as e:
        print("Exception when calling ReplicationApi->projects_project_id_machines_machine_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |

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
**204** | Machine removed from CloudEndure service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_machines_machine_id_pointsintime_get**
> PointInTimeList projects_project_id_machines_machine_id_pointsintime_get(project_id, machine_id)

List Available Points-in-time

Returns the list of available recovery points for this machine.

### Example

```python
import time
import cloudendure
from cloudendure.api import replication_api
from cloudendure.model.point_in_time_list import PointInTimeList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)
    project_id = "projectId_example" # str | 
    machine_id = "machineId_example" # str | 
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    try:
        # List Available Points-in-time
        api_response = api_instance.projects_project_id_machines_machine_id_pointsintime_get(project_id, machine_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ReplicationApi->projects_project_id_machines_machine_id_pointsintime_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Available Points-in-time
        api_response = api_instance.projects_project_id_machines_machine_id_pointsintime_get(project_id, machine_id, offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ReplicationApi->projects_project_id_machines_machine_id_pointsintime_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**PointInTimeList**](PointInTimeList.md)

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

# **projects_project_id_replication_configurations_get**
> ReplicationConfigurationList projects_project_id_replication_configurations_get(project_id)

List Replication Configurations

Returns the list of replication configuration objects defined in this project.

### Example

```python
import time
import cloudendure
from cloudendure.api import replication_api
from cloudendure.model.replication_configuration_list import ReplicationConfigurationList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)
    project_id = "projectId_example" # str | 
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    try:
        # List Replication Configurations
        api_response = api_instance.projects_project_id_replication_configurations_get(project_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ReplicationApi->projects_project_id_replication_configurations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Replication Configurations
        api_response = api_instance.projects_project_id_replication_configurations_get(project_id, offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ReplicationApi->projects_project_id_replication_configurations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**ReplicationConfigurationList**](ReplicationConfigurationList.md)

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

# **projects_project_id_replication_configurations_post**
> ReplicationConfiguration projects_project_id_replication_configurations_post(project_id, replication_configuration)

Create Replication Configuration

Control Data Replication parameters such as target cloud credentials, Staging Area and replication network configuration. A single configuration can exist per target region. Returns the newly created object. 

### Example

```python
import time
import cloudendure
from cloudendure.api import replication_api
from cloudendure.model.error import Error
from cloudendure.model.replication_configuration import ReplicationConfiguration
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)
    project_id = "projectId_example" # str | 
    replication_configuration = ReplicationConfiguration(
        volume_encryption_key="volume_encryption_key_example",
        replication_tags=[
            ReplicationConfigurationReplicationTags(
                key="key_example",
                value="value_example",
            ),
        ],
        disable_public_ip=True,
        subnet_host_project="subnet_host_project_example",
        cost_optimized_burst_balance_delta_threshold=1,
        replication_software_download_source="replication_software_download_source_example",
        cost_optimized_sc1_volumes_throughput_window_size_minutes=1,
        replication_server_type="replication_server_type_example",
        cost_optimized_burst_balance_window_size_minutes=1,
        use_low_cost_disks=True,
        compute_location_id="compute_location_id_example",
        cloud_credentials="cloud_credentials_example",
        subnet_id="subnet_id_example",
        logical_location_id="logical_location_id_example",
        cost_optimized_default_volumes_throughput_window_size_minutes=1,
        bandwidth_throttling=1,
        cost_optimized_burst_balance_threshold=1,
        use_dedicated_server=True,
        daily_pit_number=1,
        zone="zone_example",
        replicator_security_group_ids=[
            "replicator_security_group_ids_example",
        ],
        use_private_ip=True,
        region="region_example",
        id="id_example",
        proxy_url="proxy_url_example",
        volume_encryption_allowed=True,
        object_storage_location="object_storage_location_example",
        archiving_enabled=True,
        converter_type="converter_type_example",
        storage_location_id="storage_location_id_example",
        use_cost_optimized_disk_type=True,
    ) # ReplicationConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        # Create Replication Configuration
        api_response = api_instance.projects_project_id_replication_configurations_post(project_id, replication_configuration)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ReplicationApi->projects_project_id_replication_configurations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **replication_configuration** | [**ReplicationConfiguration**](ReplicationConfiguration.md)|  |

### Return type

[**ReplicationConfiguration**](ReplicationConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New object successfully created. |  -  |
**400** | There is a conflict in the replication configuration. This can be due to: subnet ID which does not exist in the region, security groups that are not in the same network as the subnet, etc. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_replication_configurations_replication_configuration_id_patch**
> ReplicationConfiguration projects_project_id_replication_configurations_replication_configuration_id_patch(project_id, replication_configuration_id, replication_configuration)

Modify Replication Configuration

Modifying volumeEncryptionKey or modifying cloudCredentials to ones matching a different cloud account will result in replication restarting from initial sync. Returns the modified object.

### Example

```python
import time
import cloudendure
from cloudendure.api import replication_api
from cloudendure.model.error import Error
from cloudendure.model.replication_configuration import ReplicationConfiguration
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = replication_api.ReplicationApi(api_client)
    project_id = "projectId_example" # str | 
    replication_configuration_id = "replicationConfigurationId_example" # str | 
    replication_configuration = ReplicationConfiguration(
        volume_encryption_key="volume_encryption_key_example",
        replication_tags=[
            ReplicationConfigurationReplicationTags(
                key="key_example",
                value="value_example",
            ),
        ],
        disable_public_ip=True,
        subnet_host_project="subnet_host_project_example",
        cost_optimized_burst_balance_delta_threshold=1,
        replication_software_download_source="replication_software_download_source_example",
        cost_optimized_sc1_volumes_throughput_window_size_minutes=1,
        replication_server_type="replication_server_type_example",
        cost_optimized_burst_balance_window_size_minutes=1,
        use_low_cost_disks=True,
        compute_location_id="compute_location_id_example",
        cloud_credentials="cloud_credentials_example",
        subnet_id="subnet_id_example",
        logical_location_id="logical_location_id_example",
        cost_optimized_default_volumes_throughput_window_size_minutes=1,
        bandwidth_throttling=1,
        cost_optimized_burst_balance_threshold=1,
        use_dedicated_server=True,
        daily_pit_number=1,
        zone="zone_example",
        replicator_security_group_ids=[
            "replicator_security_group_ids_example",
        ],
        use_private_ip=True,
        region="region_example",
        id="id_example",
        proxy_url="proxy_url_example",
        volume_encryption_allowed=True,
        object_storage_location="object_storage_location_example",
        archiving_enabled=True,
        converter_type="converter_type_example",
        storage_location_id="storage_location_id_example",
        use_cost_optimized_disk_type=True,
    ) # ReplicationConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        # Modify Replication Configuration
        api_response = api_instance.projects_project_id_replication_configurations_replication_configuration_id_patch(project_id, replication_configuration_id, replication_configuration)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ReplicationApi->projects_project_id_replication_configurations_replication_configuration_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **replication_configuration_id** | **str**|  |
 **replication_configuration** | [**ReplicationConfiguration**](ReplicationConfiguration.md)|  |

### Return type

[**ReplicationConfiguration**](ReplicationConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object updated successfully. |  -  |
**400** | There is a conflict in the replication configuration. This can be due to: subnet ID which does not exist in the region, security groups that are not in the same network as the subnet, etc. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

