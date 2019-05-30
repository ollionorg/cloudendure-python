# cloudendure_api.RecoveryPlansApi

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
> CloudEndureRecoveryPlanList projects_project_id_recovery_plans_get(project_id)

Gets all recovery plans for the project.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.RecoveryPlansApi()
project_id = 'project_id_example' # str |

try:
    # Gets all recovery plans for the project.
    api_response = api_instance.projects_project_id_recovery_plans_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryPlansApi->projects_project_id_recovery_plans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**CloudEndureRecoveryPlanList**](CloudEndureRecoveryPlanList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_recovery_plans_post**
> CloudEndureRecoveryPlan projects_project_id_recovery_plans_post(body, project_id)

Creates a new recovery plan.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.RecoveryPlansApi()
body = cloudendure_api.CloudEndureRecoveryPlan() # CloudEndureRecoveryPlan | Recovery Plan to create
project_id = 'project_id_example' # str |

try:
    # Creates a new recovery plan.
    api_response = api_instance.projects_project_id_recovery_plans_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryPlansApi->projects_project_id_recovery_plans_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureRecoveryPlan**](CloudEndureRecoveryPlan.md)| Recovery Plan to create |
 **project_id** | **str**|  |

### Return type

[**CloudEndureRecoveryPlan**](CloudEndureRecoveryPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_recovery_plans_recovery_plan_id_delete**
> projects_project_id_recovery_plans_recovery_plan_id_delete(project_id, recovery_plan_id)

Deletes a recovery plan.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.RecoveryPlansApi()
project_id = 'project_id_example' # str |
recovery_plan_id = 'recovery_plan_id_example' # str |

try:
    # Deletes a recovery plan.
    api_instance.projects_project_id_recovery_plans_recovery_plan_id_delete(project_id, recovery_plan_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_recovery_plans_recovery_plan_id_get**
> CloudEndureRecoveryPlan projects_project_id_recovery_plans_recovery_plan_id_get(project_id, recovery_plan_id)

Gets a recovery plan.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.RecoveryPlansApi()
project_id = 'project_id_example' # str |
recovery_plan_id = 'recovery_plan_id_example' # str |

try:
    # Gets a recovery plan.
    api_response = api_instance.projects_project_id_recovery_plans_recovery_plan_id_get(project_id, recovery_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryPlansApi->projects_project_id_recovery_plans_recovery_plan_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **recovery_plan_id** | **str**|  |

### Return type

[**CloudEndureRecoveryPlan**](CloudEndureRecoveryPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_recovery_plans_recovery_plan_id_patch**
> CloudEndureRecoveryPlan projects_project_id_recovery_plans_recovery_plan_id_patch(body, project_id, recovery_plan_id)

Updates a new recovery plan.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.RecoveryPlansApi()
body = cloudendure_api.CloudEndureRecoveryPlan() # CloudEndureRecoveryPlan | Recovery Plan to create
project_id = 'project_id_example' # str |
recovery_plan_id = 'recovery_plan_id_example' # str |

try:
    # Updates a new recovery plan.
    api_response = api_instance.projects_project_id_recovery_plans_recovery_plan_id_patch(body, project_id, recovery_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryPlansApi->projects_project_id_recovery_plans_recovery_plan_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureRecoveryPlan**](CloudEndureRecoveryPlan.md)| Recovery Plan to create |
 **project_id** | **str**|  |
 **recovery_plan_id** | **str**|  |

### Return type

[**CloudEndureRecoveryPlan**](CloudEndureRecoveryPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_run_recovery_plan_post**
> CloudEndureJob projects_project_id_run_recovery_plan_post(body, project_id)

Launch a recovery plan.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.RecoveryPlansApi()
body = NULL # object | Recovery Plan to create
project_id = 'project_id_example' # str |

try:
    # Launch a recovery plan.
    api_response = api_instance.projects_project_id_run_recovery_plan_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecoveryPlansApi->projects_project_id_run_recovery_plan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Recovery Plan to create |
 **project_id** | **str**|  |

### Return type

[**CloudEndureJob**](CloudEndureJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

