# cloudendure_api.MachinesApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_machines_delete**](MachinesApi.md#projects_project_id_machines_delete) | **DELETE** /projects/{projectId}/machines | Uninstall agent
[**projects_project_id_machines_get**](MachinesApi.md#projects_project_id_machines_get) | **GET** /projects/{projectId}/machines | List Machines
[**projects_project_id_machines_machine_id_get**](MachinesApi.md#projects_project_id_machines_machine_id_get) | **GET** /projects/{projectId}/machines/{machineId} | Get a specific machine.
[**projects_project_id_machines_machine_id_patch**](MachinesApi.md#projects_project_id_machines_machine_id_patch) | **PATCH** /projects/{projectId}/machines/{machineId} | Update a machine. Accepts only Launch time updates.
[**projects_project_id_machines_patch**](MachinesApi.md#projects_project_id_machines_patch) | **PATCH** /projects/{projectId}/machines | Batch-update multiple machines
[**projects_project_id_replicas_replica_id_get**](MachinesApi.md#projects_project_id_replicas_replica_id_get) | **GET** /projects/{projectId}/replicas/{replicaId} | Get Target Machine

# **projects_project_id_machines_delete**
> projects_project_id_machines_delete(body, project_id)

Uninstall agent

Stops replication and removes the cloudendure agent from the specified machines. All cloud artifacts associated with those machines with the exception of launched target machines are deleted.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.MachinesApi()
body = NULL # object | The list of machine IDs to remove from the CloudEndure service.
project_id = 'project_id_example' # str |

try:
    # Uninstall agent
    api_instance.projects_project_id_machines_delete(body, project_id)
except ApiException as e:
    print("Exception when calling MachinesApi->projects_project_id_machines_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The list of machine IDs to remove from the CloudEndure service. |
 **project_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_machines_get**
> CloudEndureMachinesList projects_project_id_machines_get(project_id, offset=offset, limit=limit, all=all, types=types)

List Machines

Returns the list of all source machines in the Project (i.e. machines that have an Agent installed).

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.MachinesApi()
project_id = 'project_id_example' # str |
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)
all = true # bool | When set to false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status. machines are consuming/ have consumed licenses.  Note that some license types are transferable and therefore once you remove the and set to true false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status.  (optional)
types = 'types_example' # str | Use this url query param to control which machines are returned when doing GET.  If you do not include the \\\"types\\\" query param, you will only get source machines  (optional)

try:
    # List Machines
    api_response = api_instance.projects_project_id_machines_get(project_id, offset=offset, limit=limit, all=all, types=types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->projects_project_id_machines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]
 **all** | **bool**| When set to false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status. machines are consuming/ have consumed licenses.  Note that some license types are transferable and therefore once you remove the and set to true false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status.  | [optional]
 **types** | **str**| Use this url query param to control which machines are returned when doing GET.  If you do not include the \\\&quot;types\\\&quot; query param, you will only get source machines  | [optional]

### Return type

[**CloudEndureMachinesList**](CloudEndureMachinesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_machines_machine_id_get**
> CloudEndureMachine projects_project_id_machines_machine_id_get(project_id, machine_id)

Get a specific machine.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.MachinesApi()
project_id = 'project_id_example' # str |
machine_id = 'machine_id_example' # str |

try:
    # Get a specific machine.
    api_response = api_instance.projects_project_id_machines_machine_id_get(project_id, machine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->projects_project_id_machines_machine_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |

### Return type

[**CloudEndureMachine**](CloudEndureMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_machines_machine_id_patch**
> CloudEndureMachine projects_project_id_machines_machine_id_patch(body, project_id, machine_id)

Update a machine. Accepts only Launch time updates.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.MachinesApi()
body = cloudendure_api.CloudEndureMachine() # CloudEndureMachine |
project_id = 'project_id_example' # str |
machine_id = 'machine_id_example' # str |

try:
    # Update a machine. Accepts only Launch time updates.
    api_response = api_instance.projects_project_id_machines_machine_id_patch(body, project_id, machine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->projects_project_id_machines_machine_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureMachine**](CloudEndureMachine.md)|  |
 **project_id** | **str**|  |
 **machine_id** | **str**|  |

### Return type

[**CloudEndureMachine**](CloudEndureMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_machines_patch**
> CloudEndureMachinesList projects_project_id_machines_patch(body, project_id)

Batch-update multiple machines

todo must allow update of tags, update of replicationConfiguration; may allow update of launch times

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.MachinesApi()
body = cloudendure_api.CloudEndureMachinesList() # CloudEndureMachinesList |
project_id = 'project_id_example' # str |

try:
    # Batch-update multiple machines
    api_response = api_instance.projects_project_id_machines_patch(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->projects_project_id_machines_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureMachinesList**](CloudEndureMachinesList.md)|  |
 **project_id** | **str**|  |

### Return type

[**CloudEndureMachinesList**](CloudEndureMachinesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_replicas_replica_id_get**
> CloudEndureReplica projects_project_id_replicas_replica_id_get(project_id, replica_id)

Get Target Machine

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.MachinesApi()
project_id = 'project_id_example' # str |
replica_id = 'replica_id_example' # str |

try:
    # Get Target Machine
    api_response = api_instance.projects_project_id_replicas_replica_id_get(project_id, replica_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->projects_project_id_replicas_replica_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **replica_id** | **str**|  |

### Return type

[**CloudEndureReplica**](CloudEndureReplica.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

