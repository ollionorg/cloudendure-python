# cloudendure.ActionsApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_jobs_get**](ActionsApi.md#projects_project_id_jobs_get) | **GET** /projects/{projectId}/jobs | List Jobs
[**projects_project_id_jobs_job_id_get**](ActionsApi.md#projects_project_id_jobs_job_id_get) | **GET** /projects/{projectId}/jobs/{jobId} | Get Job
[**projects_project_id_launch_machines_post**](ActionsApi.md#projects_project_id_launch_machines_post) | **POST** /projects/{projectId}/launchMachines | Launch target machines
[**projects_project_id_move_machines_post**](ActionsApi.md#projects_project_id_move_machines_post) | **POST** /projects/{projectId}/moveMachines | Moves machines to another project
[**projects_project_id_pause_replication_post**](ActionsApi.md#projects_project_id_pause_replication_post) | **POST** /projects/{projectId}/pauseReplication | Pause replication
[**projects_project_id_replicas_delete**](ActionsApi.md#projects_project_id_replicas_delete) | **DELETE** /projects/{projectId}/replicas | Perform Cleanup
[**projects_project_id_reverse_replication_post**](ActionsApi.md#projects_project_id_reverse_replication_post) | **POST** /projects/{projectId}/reverseReplication | Reverse replication direction
[**projects_project_id_start_replication_post**](ActionsApi.md#projects_project_id_start_replication_post) | **POST** /projects/{projectId}/startReplication | Start replication
[**projects_project_id_stop_replication_post**](ActionsApi.md#projects_project_id_stop_replication_post) | **POST** /projects/{projectId}/stopReplication | Stop replication


# **projects_project_id_jobs_get**
> JobsList projects_project_id_jobs_get(project_id)

List Jobs

Returns the list of jobs in the project.

### Example

```python
import time
import cloudendure
from cloudendure.api import actions_api
from cloudendure.model.jobs_list import JobsList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    project_id = "projectId_example" # str | 
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    try:
        # List Jobs
        api_response = api_instance.projects_project_id_jobs_get(project_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ActionsApi->projects_project_id_jobs_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Jobs
        api_response = api_instance.projects_project_id_jobs_get(project_id, offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ActionsApi->projects_project_id_jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**JobsList**](JobsList.md)

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

# **projects_project_id_jobs_job_id_get**
> Job projects_project_id_jobs_job_id_get(project_id, job_id)

Get Job

### Example

```python
import time
import cloudendure
from cloudendure.api import actions_api
from cloudendure.model.job import Job
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    project_id = "projectId_example" # str | 
    job_id = "jobId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Job
        api_response = api_instance.projects_project_id_jobs_job_id_get(project_id, job_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ActionsApi->projects_project_id_jobs_job_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **job_id** | **str**|  |

### Return type

[**Job**](Job.md)

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

# **projects_project_id_launch_machines_post**
> Job projects_project_id_launch_machines_post(project_id, launch_machines)

Launch target machines

Launch target machines for test, recovery or cutover (by passing enum value to launchType param)

### Example

```python
import time
import cloudendure
from cloudendure.api import actions_api
from cloudendure.model.job import Job
from cloudendure.model.launch_machines_parameters import LaunchMachinesParameters
from cloudendure.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    project_id = "projectId_example" # str | 
    launch_machines = LaunchMachinesParameters(
        items=[
            MachineAndPointInTime(
                machine_id="machine_id_example",
                point_in_time_id="point_in_time_id_example",
            ),
        ],
        launch_type="TEST",
        debug_scripts=LaunchMachinesParametersDebugScripts(
            postboot=[
                "postboot_example",
            ],
            preboot=[
                "preboot_example",
            ],
        ),
    ) # LaunchMachinesParameters | Machines to launch

    # example passing only required values which don't have defaults set
    try:
        # Launch target machines
        api_response = api_instance.projects_project_id_launch_machines_post(project_id, launch_machines)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ActionsApi->projects_project_id_launch_machines_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **launch_machines** | [**LaunchMachinesParameters**](LaunchMachinesParameters.md)| Machines to launch |

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Test job created. |  -  |
**400** | Another job is already running in this project. |  -  |
**402** | Project license has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_move_machines_post**
> projects_project_id_move_machines_post(project_id, move_machines_params)

Moves machines to another project

TBC 

### Example

```python
import time
import cloudendure
from cloudendure.api import actions_api
from cloudendure.model.inline_object4 import InlineObject4
from cloudendure.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    project_id = "projectId_example" # str | 
    move_machines_params = InlineObject4(
        machine_ids=[
            "machine_ids_example",
        ],
        destination_project_id="destination_project_id_example",
    ) # InlineObject4 | 

    # example passing only required values which don't have defaults set
    try:
        # Moves machines to another project
        api_instance.projects_project_id_move_machines_post(project_id, move_machines_params)
    except cloudendure.ApiException as e:
        print("Exception when calling ActionsApi->projects_project_id_move_machines_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **move_machines_params** | [**InlineObject4**](InlineObject4.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Machines moved successfully |  -  |
**404** | A machine or project not found in Account |  -  |
**409** | Machines could not be moved due to conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_pause_replication_post**
> MachinesListInvalidIDsAndJob projects_project_id_pause_replication_post(project_id, machine_ids)

Pause replication

Pause replication for given machines

### Example

```python
import time
import cloudendure
from cloudendure.api import actions_api
from cloudendure.model.machines_list_invalid_ids_and_job import MachinesListInvalidIDsAndJob
from cloudendure.model.inline_object9 import InlineObject9
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    project_id = "projectId_example" # str | 
    machine_ids = InlineObject9(
        machine_ids=[
            "machine_ids_example",
        ],
    ) # InlineObject9 | 

    # example passing only required values which don't have defaults set
    try:
        # Pause replication
        api_response = api_instance.projects_project_id_pause_replication_post(project_id, machine_ids)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ActionsApi->projects_project_id_pause_replication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_ids** | [**InlineObject9**](InlineObject9.md)|  |

### Return type

[**MachinesListInvalidIDsAndJob**](MachinesListInvalidIDsAndJob.md)

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

# **projects_project_id_replicas_delete**
> Job projects_project_id_replicas_delete(project_id, replica_ids)

Perform Cleanup

Spawns a cleanup job to remove the specified target machines from the cloud. Returns the job information.

### Example

```python
import time
import cloudendure
from cloudendure.api import actions_api
from cloudendure.model.job import Job
from cloudendure.model.inline_object5 import InlineObject5
from cloudendure.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    project_id = "projectId_example" # str | 
    replica_ids = InlineObject5(
        replica_ids=[
            "replica_ids_example",
        ],
    ) # InlineObject5 | 

    # example passing only required values which don't have defaults set
    try:
        # Perform Cleanup
        api_response = api_instance.projects_project_id_replicas_delete(project_id, replica_ids)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ActionsApi->projects_project_id_replicas_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **replica_ids** | [**InlineObject5**](InlineObject5.md)|  |

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Cleanup job created. |  -  |
**400** | Another job is already running in this project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_reverse_replication_post**
> projects_project_id_reverse_replication_post(project_id)

Reverse replication direction

### Example

```python
import time
import cloudendure
from cloudendure.api import actions_api
from cloudendure.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Reverse replication direction
        api_instance.projects_project_id_reverse_replication_post(project_id)
    except cloudendure.ApiException as e:
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | A job is running. |  -  |
**422** | Project cannot be reversed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_start_replication_post**
> MachinesListInvalidIDsAndJob projects_project_id_start_replication_post(project_id, machine_ids)

Start replication

Start replication of the specified source machines. Returns the machine for which replication has been successfully started, and the IDs for which replication could not be started.

### Example

```python
import time
import cloudendure
from cloudendure.api import actions_api
from cloudendure.model.machines_list_invalid_ids_and_job import MachinesListInvalidIDsAndJob
from cloudendure.model.inline_object3 import InlineObject3
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    project_id = "projectId_example" # str | 
    machine_ids = InlineObject3(
        machine_ids=[
            "machine_ids_example",
        ],
    ) # InlineObject3 | 

    # example passing only required values which don't have defaults set
    try:
        # Start replication
        api_response = api_instance.projects_project_id_start_replication_post(project_id, machine_ids)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ActionsApi->projects_project_id_start_replication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_ids** | [**InlineObject3**](InlineObject3.md)|  |

### Return type

[**MachinesListInvalidIDsAndJob**](MachinesListInvalidIDsAndJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request acknowledged. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_stop_replication_post**
> MachinesListInvalidIDsAndJob projects_project_id_stop_replication_post(project_id, machine_ids)

Stop replication

Stop replication of the specified source machines. Returns the machine for which replication has been successfully stopped, and the IDs for which replication could not be stopped.

### Example

```python
import time
import cloudendure
from cloudendure.api import actions_api
from cloudendure.model.inline_object7 import InlineObject7
from cloudendure.model.machines_list_invalid_ids_and_job import MachinesListInvalidIDsAndJob
from cloudendure.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = actions_api.ActionsApi(api_client)
    project_id = "projectId_example" # str | 
    machine_ids = InlineObject7(
        machine_ids=[
            "machine_ids_example",
        ],
        move_vmdks=True,
    ) # InlineObject7 | 

    # example passing only required values which don't have defaults set
    try:
        # Stop replication
        api_response = api_instance.projects_project_id_stop_replication_post(project_id, machine_ids)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ActionsApi->projects_project_id_stop_replication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_ids** | [**InlineObject7**](InlineObject7.md)|  |

### Return type

[**MachinesListInvalidIDsAndJob**](MachinesListInvalidIDsAndJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request acknowledged. |  -  |
**409** | Another job is already running in this project. |  -  |
**429** | Too many jobs are running for this project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

