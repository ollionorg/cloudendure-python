# cloudendure_api.ProjectApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_get**](ProjectApi.md#projects_get) | **GET** /projects | List Projects
[**projects_post**](ProjectApi.md#projects_post) | **POST** /projects | Create Project
[**projects_project_id_delete**](ProjectApi.md#projects_project_id_delete) | **DELETE** /projects/{projectId} | Delete Project and all sub-resources including cloud assets other than launched target machines
[**projects_project_id_get**](ProjectApi.md#projects_project_id_get) | **GET** /projects/{projectId} | Get Project
[**projects_project_id_patch**](ProjectApi.md#projects_project_id_patch) | **PATCH** /projects/{projectId} | Update Project (including partial update)
[**projects_project_id_tags_get**](ProjectApi.md#projects_project_id_tags_get) | **GET** /projects/{projectId}/tags | Gets all instance tags of all machines in the project.

# **projects_get**
> CloudEndureProjectsList projects_get(offset=offset, limit=limit)

List Projects

Returns the list of projects defined in this account.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ProjectApi()
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # List Projects
    api_response = api_instance.projects_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

[**CloudEndureProjectsList**](CloudEndureProjectsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_post**
> CloudEndureProject projects_post(body)

Create Project

Create project

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ProjectApi()
body = cloudendure_api.CloudEndureProject() # CloudEndureProject |

try:
    # Create Project
    api_response = api_instance.projects_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureProject**](CloudEndureProject.md)|  |

### Return type

[**CloudEndureProject**](CloudEndureProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_delete**
> projects_project_id_delete(project_id)

Delete Project and all sub-resources including cloud assets other than launched target machines

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ProjectApi()
project_id = 'project_id_example' # str |

try:
    # Delete Project and all sub-resources including cloud assets other than launched target machines
    api_instance.projects_project_id_delete(project_id)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_project_id_delete: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_get**
> CloudEndureProject projects_project_id_get(project_id)

Get Project

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ProjectApi()
project_id = 'project_id_example' # str |

try:
    # Get Project
    api_response = api_instance.projects_project_id_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_project_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**CloudEndureProject**](CloudEndureProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_patch**
> CloudEndureProject projects_project_id_patch(body, project_id)

Update Project (including partial update)

Set project properties including Data Replication source location and replicationConfiguration to use.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ProjectApi()
body = cloudendure_api.CloudEndureProject() # CloudEndureProject |
project_id = 'project_id_example' # str |

try:
    # Update Project (including partial update)
    api_response = api_instance.projects_project_id_patch(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_project_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureProject**](CloudEndureProject.md)|  |
 **project_id** | **str**|  |

### Return type

[**CloudEndureProject**](CloudEndureProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_tags_get**
> object projects_project_id_tags_get(project_id, offset=offset, limit=limit)

Gets all instance tags of all machines in the project.

Returns all instance tags of all machines in the project.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.ProjectApi()
project_id = 'project_id_example' # str |
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # Gets all instance tags of all machines in the project.
    api_response = api_instance.projects_project_id_tags_get(project_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_project_id_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

