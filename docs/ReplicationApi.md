# cloudendure_api.ReplicationApi

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
> CloudEndureBandwidthThrottling projects_project_id_machines_machine_id_bandwidth_throttling_get(project_id, machine_id)

Get value of network bandwidth throttling setting for Machine

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ReplicationApi()
project_id = 'project_id_example' # str |
machine_id = 'machine_id_example' # str |

try:
    # Get value of network bandwidth throttling setting for Machine
    api_response = api_instance.projects_project_id_machines_machine_id_bandwidth_throttling_get(project_id, machine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->projects_project_id_machines_machine_id_bandwidth_throttling_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |

### Return type

[**CloudEndureBandwidthThrottling**](CloudEndureBandwidthThrottling.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_machines_machine_id_bandwidth_throttling_patch**
> CloudEndureBandwidthThrottling projects_project_id_machines_machine_id_bandwidth_throttling_patch(body, project_id, machine_id)

Set value of network bandwidth throttling setting for Machine

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ReplicationApi()
body = cloudendure_api.CloudEndureBandwidthThrottling() # CloudEndureBandwidthThrottling |
project_id = 'project_id_example' # str |
machine_id = 'machine_id_example' # str |

try:
    # Set value of network bandwidth throttling setting for Machine
    api_response = api_instance.projects_project_id_machines_machine_id_bandwidth_throttling_patch(body, project_id, machine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->projects_project_id_machines_machine_id_bandwidth_throttling_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureBandwidthThrottling**](CloudEndureBandwidthThrottling.md)|  |
 **project_id** | **str**|  |
 **machine_id** | **str**|  |

### Return type

[**CloudEndureBandwidthThrottling**](CloudEndureBandwidthThrottling.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_machines_machine_id_delete**
> projects_project_id_machines_machine_id_delete(project_id, machine_id)

Uninstall agent

Stops replication and removes the cloudendure agent from this machine. All cloud artifacts associated with those machines with the exception of launched target machine are deleted.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ReplicationApi()
project_id = 'project_id_example' # str |
machine_id = 'machine_id_example' # str |

try:
    # Uninstall agent
    api_instance.projects_project_id_machines_machine_id_delete(project_id, machine_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_machines_machine_id_pointsintime_get**
> CloudEndurePointInTimeList projects_project_id_machines_machine_id_pointsintime_get(project_id, machine_id, offset=offset, limit=limit)

List Available Points-in-time

Returns the list of available recovery points for this machine.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ReplicationApi()
project_id = 'project_id_example' # str |
machine_id = 'machine_id_example' # str |
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # List Available Points-in-time
    api_response = api_instance.projects_project_id_machines_machine_id_pointsintime_get(project_id, machine_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->projects_project_id_machines_machine_id_pointsintime_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

[**CloudEndurePointInTimeList**](CloudEndurePointInTimeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_replication_configurations_get**
> CloudEndureReplicationConfigurationList projects_project_id_replication_configurations_get(project_id, offset=offset, limit=limit)

List Replication Configurations

Returns the list of replication configuration objects defined in this project.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ReplicationApi()
project_id = 'project_id_example' # str |
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # List Replication Configurations
    api_response = api_instance.projects_project_id_replication_configurations_get(project_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->projects_project_id_replication_configurations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

[**CloudEndureReplicationConfigurationList**](CloudEndureReplicationConfigurationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_replication_configurations_post**
> CloudEndureReplicationConfiguration projects_project_id_replication_configurations_post(body, project_id)

Create Replication Configuration

Control Data Replication parameters such as target cloud credentials, Staging Area and replication network configuration. A single configuration can exist per target region. Returns the newly created object.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ReplicationApi()
body = cloudendure_api.CloudEndureReplicationConfiguration() # CloudEndureReplicationConfiguration |
project_id = 'project_id_example' # str |

try:
    # Create Replication Configuration
    api_response = api_instance.projects_project_id_replication_configurations_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->projects_project_id_replication_configurations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureReplicationConfiguration**](CloudEndureReplicationConfiguration.md)|  |
 **project_id** | **str**|  |

### Return type

[**CloudEndureReplicationConfiguration**](CloudEndureReplicationConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_replication_configurations_replication_configuration_id_patch**
> CloudEndureReplicationConfiguration projects_project_id_replication_configurations_replication_configuration_id_patch(body, project_id, replication_configuration_id)

Modify Replication Configuration

Modifying volumeEncryptionKey or modifying cloudCredentials to ones matching a different cloud account will result in replication restarting from initial sync. Returns the modified object.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ReplicationApi()
body = cloudendure_api.CloudEndureReplicationConfiguration() # CloudEndureReplicationConfiguration |
project_id = 'project_id_example' # str |
replication_configuration_id = 'replication_configuration_id_example' # str |

try:
    # Modify Replication Configuration
    api_response = api_instance.projects_project_id_replication_configurations_replication_configuration_id_patch(body, project_id, replication_configuration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->projects_project_id_replication_configurations_replication_configuration_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureReplicationConfiguration**](CloudEndureReplicationConfiguration.md)|  |
 **project_id** | **str**|  |
 **replication_configuration_id** | **str**|  |

### Return type

[**CloudEndureReplicationConfiguration**](CloudEndureReplicationConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

