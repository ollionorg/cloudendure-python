# cloudendure_api.ActionsApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_find_files_post**](ActionsApi.md#projects_project_id_find_files_post) | **POST** /projects/{projectId}/findFiles | Search for files in a backup project
[**projects_project_id_jobs_get**](ActionsApi.md#projects_project_id_jobs_get) | **GET** /projects/{projectId}/jobs | List Jobs
[**projects_project_id_jobs_job_id_get**](ActionsApi.md#projects_project_id_jobs_job_id_get) | **GET** /projects/{projectId}/jobs/{jobId} | Get Job
[**projects_project_id_launch_machines_post**](ActionsApi.md#projects_project_id_launch_machines_post) | **POST** /projects/{projectId}/launchMachines | Launch target machines
[**projects_project_id_launch_restore_servers_post**](ActionsApi.md#projects_project_id_launch_restore_servers_post) | **POST** /projects/{projectId}/launchRestoreServers | Launch restore servers @todo
[**projects_project_id_move_machines_post**](ActionsApi.md#projects_project_id_move_machines_post) | **POST** /projects/{projectId}/moveMachines | Moves machines to another project
[**projects_project_id_pause_replication_post**](ActionsApi.md#projects_project_id_pause_replication_post) | **POST** /projects/{projectId}/pauseReplication | Pause replication
[**projects_project_id_replicas_delete**](ActionsApi.md#projects_project_id_replicas_delete) | **DELETE** /projects/{projectId}/replicas | Perform Cleanup
[**projects_project_id_restore_files_post**](ActionsApi.md#projects_project_id_restore_files_post) | **POST** /projects/{projectId}/restoreFiles | Restore selected files in a backup project
[**projects_project_id_reverse_replication_post**](ActionsApi.md#projects_project_id_reverse_replication_post) | **POST** /projects/{projectId}/reverseReplication | Reverse replication direction
[**projects_project_id_start_replication_post**](ActionsApi.md#projects_project_id_start_replication_post) | **POST** /projects/{projectId}/startReplication | Start replication
[**projects_project_id_stop_replication_post**](ActionsApi.md#projects_project_id_stop_replication_post) | **POST** /projects/{projectId}/stopReplication | Stop replication

# **projects_project_id_find_files_post**
> CloudEndureFindFilesResults projects_project_id_find_files_post(body, project_id)

Search for files in a backup project

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
body = cloudendure_api.CloudEndureFindFilesParameters() # CloudEndureFindFilesParameters | The query string and the machine id's to use it in
project_id = 'project_id_example' # str |

try:
    # Search for files in a backup project
    api_response = api_instance.projects_project_id_find_files_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_find_files_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureFindFilesParameters**](CloudEndureFindFilesParameters.md)| The query string and the machine id&#x27;s to use it in |
 **project_id** | **str**|  |

### Return type

[**CloudEndureFindFilesResults**](CloudEndureFindFilesResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_jobs_get**
> CloudEndureJobsList projects_project_id_jobs_get(project_id, offset=offset, limit=limit)

List Jobs

Returns the list of jobs in the project.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
project_id = 'project_id_example' # str |
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # List Jobs
    api_response = api_instance.projects_project_id_jobs_get(project_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

[**CloudEndureJobsList**](CloudEndureJobsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_jobs_job_id_get**
> CloudEndureJob projects_project_id_jobs_job_id_get(project_id, job_id)

Get Job

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
project_id = 'project_id_example' # str |
job_id = 'job_id_example' # str |

try:
    # Get Job
    api_response = api_instance.projects_project_id_jobs_job_id_get(project_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_jobs_job_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **job_id** | **str**|  |

### Return type

[**CloudEndureJob**](CloudEndureJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_launch_machines_post**
> CloudEndureJob projects_project_id_launch_machines_post(body, project_id)

Launch target machines

Launch target machines for test, recovery or cutover (by passing enum value to launchType param)

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
body = cloudendure_api.CloudEndureLaunchMachinesParameters() # CloudEndureLaunchMachinesParameters | Machines to launch
project_id = 'project_id_example' # str |

try:
    # Launch target machines
    api_response = api_instance.projects_project_id_launch_machines_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_launch_machines_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureLaunchMachinesParameters**](CloudEndureLaunchMachinesParameters.md)| Machines to launch |
 **project_id** | **str**|  |

### Return type

[**CloudEndureJob**](CloudEndureJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_launch_restore_servers_post**
> CloudEndureJob projects_project_id_launch_restore_servers_post(body, project_id)

Launch restore servers @todo

todo

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
body = cloudendure_api.CloudEndureLaunchMachinesParameters() # CloudEndureLaunchMachinesParameters | todo
project_id = 'project_id_example' # str |

try:
    # Launch restore servers @todo
    api_response = api_instance.projects_project_id_launch_restore_servers_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_launch_restore_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureLaunchMachinesParameters**](CloudEndureLaunchMachinesParameters.md)| todo |
 **project_id** | **str**|  |

### Return type

[**CloudEndureJob**](CloudEndureJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_move_machines_post**
> projects_project_id_move_machines_post(body, project_id)

Moves machines to another project

TBC

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
body = NULL # object |
project_id = 'project_id_example' # str |

try:
    # Moves machines to another project
    api_instance.projects_project_id_move_machines_post(body, project_id)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_move_machines_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  |
 **project_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_pause_replication_post**
> CloudEndureMachinesListInvalidIDsAndJob projects_project_id_pause_replication_post(body, project_id)

Pause replication

Pause replication for given machines

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
body = NULL # object | The machine IDs for which to pause replication.
project_id = 'project_id_example' # str |

try:
    # Pause replication
    api_response = api_instance.projects_project_id_pause_replication_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_pause_replication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The machine IDs for which to pause replication. |
 **project_id** | **str**|  |

### Return type

[**CloudEndureMachinesListInvalidIDsAndJob**](CloudEndureMachinesListInvalidIDsAndJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_replicas_delete**
> CloudEndureJob projects_project_id_replicas_delete(body, project_id)

Perform Cleanup

Spawns a cleanup job to remove the specified target machines from the cloud. Returns the job information.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
body = NULL # object | The list of replica IDs to delete (corresponding to the 'replica' field in the machine object.
project_id = 'project_id_example' # str |

try:
    # Perform Cleanup
    api_response = api_instance.projects_project_id_replicas_delete(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_replicas_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The list of replica IDs to delete (corresponding to the &#x27;replica&#x27; field in the machine object. |
 **project_id** | **str**|  |

### Return type

[**CloudEndureJob**](CloudEndureJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_restore_files_post**
> CloudEndureJob projects_project_id_restore_files_post(body, project_id)

Restore selected files in a backup project

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
body = cloudendure_api.CloudEndureRestoreFilesParameters() # CloudEndureRestoreFilesParameters | A list of file origins, each origin includes file path, machine id, and pit id.
project_id = 'project_id_example' # str |

try:
    # Restore selected files in a backup project
    api_response = api_instance.projects_project_id_restore_files_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_restore_files_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureRestoreFilesParameters**](CloudEndureRestoreFilesParameters.md)| A list of file origins, each origin includes file path, machine id, and pit id. |
 **project_id** | **str**|  |

### Return type

[**CloudEndureJob**](CloudEndureJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_reverse_replication_post**
> projects_project_id_reverse_replication_post(project_id)

Reverse replication direction

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
project_id = 'project_id_example' # str |

try:
    # Reverse replication direction
    api_instance.projects_project_id_reverse_replication_post(project_id)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_reverse_replication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_start_replication_post**
> CloudEndureMachinesListInvalidIDsAndJob projects_project_id_start_replication_post(body, project_id)

Start replication

Start replication of the specified source machines. Returns the machine for which replication has been successfully started, and the IDs for which replication could not be started.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
body = NULL # object | Specification of the machines for which replication will start.
project_id = 'project_id_example' # str |

try:
    # Start replication
    api_response = api_instance.projects_project_id_start_replication_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_start_replication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Specification of the machines for which replication will start. |
 **project_id** | **str**|  |

### Return type

[**CloudEndureMachinesListInvalidIDsAndJob**](CloudEndureMachinesListInvalidIDsAndJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_stop_replication_post**
> CloudEndureMachinesListInvalidIDsAndJob projects_project_id_stop_replication_post(body, project_id)

Stop replication

Stop replication of the specified source machines. Returns the machine for which replication has been successfully stopped, and the IDs for which replication could not be stopped.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ActionsApi()
body = NULL # object | Specification of the machines for which replication will stop.
project_id = 'project_id_example' # str |

try:
    # Stop replication
    api_response = api_instance.projects_project_id_stop_replication_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->projects_project_id_stop_replication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Specification of the machines for which replication will stop. |
 **project_id** | **str**|  |

### Return type

[**CloudEndureMachinesListInvalidIDsAndJob**](CloudEndureMachinesListInvalidIDsAndJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

