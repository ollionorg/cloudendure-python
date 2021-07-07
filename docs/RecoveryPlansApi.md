# cloudendure.RecoveryPlansApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_recovery_plans_get**](RecoveryPlansApi.md#projects_project_id_recovery_plans_get) | **GET** /projects/{projectId}/recoveryPlans | Gets all recovery plans for the project.
[**projects_project_id_recovery_plans_post**](RecoveryPlansApi.md#projects_project_id_recovery_plans_post) | **POST** /projects/{projectId}/recoveryPlans | Creates a new recovery plan.
[**projects_project_id_recovery_plans_recovery_plan_id_delete**](RecoveryPlansApi.md#projects_project_id_recovery_plans_recovery_plan_id_delete) | **DELETE** /projects/{projectId}/recoveryPlans/{recoveryPlanId} | Deletes a recovery plan.
[**projects_project_id_recovery_plans_recovery_plan_id_get**](RecoveryPlansApi.md#projects_project_id_recovery_plans_recovery_plan_id_get) | **GET** /projects/{projectId}/recoveryPlans/{recoveryPlanId} | Gets a recovery plan.
[**projects_project_id_recovery_plans_recovery_plan_id_patch**](RecoveryPlansApi.md#projects_project_id_recovery_plans_recovery_plan_id_patch) | **PATCH** /projects/{projectId}/recoveryPlans/{recoveryPlanId} | Updates a new recovery plan.
[**projects_project_id_run_recovery_plan_post**](RecoveryPlansApi.md#projects_project_id_run_recovery_plan_post) | **POST** /projects/{projectId}/runRecoveryPlan | Launch a recovery plan.


# **projects_project_id_recovery_plans_get**
> RecoveryPlanList projects_project_id_recovery_plans_get(project_id)

Gets all recovery plans for the project.

### Example

```python
import time
import cloudendure
from cloudendure.api import recovery_plans_api
from cloudendure.model.recovery_plan_list import RecoveryPlanList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recovery_plans_api.RecoveryPlansApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets all recovery plans for the project.
        api_response = api_instance.projects_project_id_recovery_plans_get(project_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling RecoveryPlansApi->projects_project_id_recovery_plans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**RecoveryPlanList**](RecoveryPlanList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_recovery_plans_post**
> RecoveryPlan projects_project_id_recovery_plans_post(project_id, recovery_plan)

Creates a new recovery plan.

### Example

```python
import time
import cloudendure
from cloudendure.api import recovery_plans_api
from cloudendure.model.recovery_plan import RecoveryPlan
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recovery_plans_api.RecoveryPlansApi(api_client)
    project_id = "projectId_example" # str | 
    recovery_plan = RecoveryPlan(
        steps=RecoveryPlanSteps(
            items=[
                RecoveryPlanStep(
                    machine_ids=[
                        "machine_ids_example",
                    ],
                    wait_before="wait_before_example",
                    name="name_example",
                ),
            ],
        ),
        id="id_example",
        name="name_example",
    ) # RecoveryPlan | Recovery Plan to create

    # example passing only required values which don't have defaults set
    try:
        # Creates a new recovery plan.
        api_response = api_instance.projects_project_id_recovery_plans_post(project_id, recovery_plan)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling RecoveryPlansApi->projects_project_id_recovery_plans_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **recovery_plan** | [**RecoveryPlan**](RecoveryPlan.md)| Recovery Plan to create |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_recovery_plans_recovery_plan_id_delete**
> projects_project_id_recovery_plans_recovery_plan_id_delete(project_id, recovery_plan_id)

Deletes a recovery plan.

### Example

```python
import time
import cloudendure
from cloudendure.api import recovery_plans_api
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recovery_plans_api.RecoveryPlansApi(api_client)
    project_id = "projectId_example" # str | 
    recovery_plan_id = "recoveryPlanId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a recovery plan.
        api_instance.projects_project_id_recovery_plans_recovery_plan_id_delete(project_id, recovery_plan_id)
    except cloudendure.ApiException as e:
        print("Exception when calling RecoveryPlansApi->projects_project_id_recovery_plans_recovery_plan_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **recovery_plan_id** | **str**|  |

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_recovery_plans_recovery_plan_id_get**
> RecoveryPlan projects_project_id_recovery_plans_recovery_plan_id_get(project_id, recovery_plan_id)

Gets a recovery plan.

### Example

```python
import time
import cloudendure
from cloudendure.api import recovery_plans_api
from cloudendure.model.recovery_plan import RecoveryPlan
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recovery_plans_api.RecoveryPlansApi(api_client)
    project_id = "projectId_example" # str | 
    recovery_plan_id = "recoveryPlanId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a recovery plan.
        api_response = api_instance.projects_project_id_recovery_plans_recovery_plan_id_get(project_id, recovery_plan_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling RecoveryPlansApi->projects_project_id_recovery_plans_recovery_plan_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **recovery_plan_id** | **str**|  |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_recovery_plans_recovery_plan_id_patch**
> RecoveryPlan projects_project_id_recovery_plans_recovery_plan_id_patch(project_id, recovery_plan_id, recovery_plan)

Updates a new recovery plan.

### Example

```python
import time
import cloudendure
from cloudendure.api import recovery_plans_api
from cloudendure.model.recovery_plan import RecoveryPlan
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recovery_plans_api.RecoveryPlansApi(api_client)
    project_id = "projectId_example" # str | 
    recovery_plan_id = "recoveryPlanId_example" # str | 
    recovery_plan = RecoveryPlan(
        steps=RecoveryPlanSteps(
            items=[
                RecoveryPlanStep(
                    machine_ids=[
                        "machine_ids_example",
                    ],
                    wait_before="wait_before_example",
                    name="name_example",
                ),
            ],
        ),
        id="id_example",
        name="name_example",
    ) # RecoveryPlan | Recovery Plan to create

    # example passing only required values which don't have defaults set
    try:
        # Updates a new recovery plan.
        api_response = api_instance.projects_project_id_recovery_plans_recovery_plan_id_patch(project_id, recovery_plan_id, recovery_plan)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling RecoveryPlansApi->projects_project_id_recovery_plans_recovery_plan_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **recovery_plan_id** | **str**|  |
 **recovery_plan** | [**RecoveryPlan**](RecoveryPlan.md)| Recovery Plan to create |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_run_recovery_plan_post**
> Job projects_project_id_run_recovery_plan_post(project_id, init_recovery_plan_params)

Launch a recovery plan.

### Example

```python
import time
import cloudendure
from cloudendure.api import recovery_plans_api
from cloudendure.model.job import Job
from cloudendure.model.inline_object10 import InlineObject10
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = recovery_plans_api.RecoveryPlansApi(api_client)
    project_id = "projectId_example" # str | 
    init_recovery_plan_params = InlineObject10(
        recovery_plan_id="recovery_plan_id_example",
        execution_mode="TEST",
        point_in_time_id="point_in_time_id_example",
    ) # InlineObject10 | 

    # example passing only required values which don't have defaults set
    try:
        # Launch a recovery plan.
        api_response = api_instance.projects_project_id_run_recovery_plan_post(project_id, init_recovery_plan_params)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling RecoveryPlansApi->projects_project_id_run_recovery_plan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **init_recovery_plan_params** | [**InlineObject10**](InlineObject10.md)|  |

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
**202** | Job created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

