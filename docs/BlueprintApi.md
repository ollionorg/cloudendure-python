# cloudendure_api.BlueprintApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_blueprints_blueprint_id_get**](BlueprintApi.md#projects_project_id_blueprints_blueprint_id_get) | **GET** /projects/{projectId}/blueprints/{blueprintId} | Get Blueprint
[**projects_project_id_blueprints_blueprint_id_patch**](BlueprintApi.md#projects_project_id_blueprints_blueprint_id_patch) | **PATCH** /projects/{projectId}/blueprints/{blueprintId} | Configure Blueprint
[**projects_project_id_blueprints_get**](BlueprintApi.md#projects_project_id_blueprints_get) | **GET** /projects/{projectId}/blueprints | List Blueprints
[**projects_project_id_blueprints_post**](BlueprintApi.md#projects_project_id_blueprints_post) | **POST** /projects/{projectId}/blueprints | Create Blueprint

# **projects_project_id_blueprints_blueprint_id_get**
> CloudEndureBlueprint projects_project_id_blueprints_blueprint_id_get(project_id, blueprint_id)

Get Blueprint

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.BlueprintApi()
project_id = 'project_id_example' # str |
blueprint_id = 'blueprint_id_example' # str |

try:
    # Get Blueprint
    api_response = api_instance.projects_project_id_blueprints_blueprint_id_get(project_id, blueprint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlueprintApi->projects_project_id_blueprints_blueprint_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **blueprint_id** | **str**|  |

### Return type

[**CloudEndureBlueprint**](CloudEndureBlueprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_blueprints_blueprint_id_patch**
> CloudEndureBlueprint projects_project_id_blueprints_blueprint_id_patch(body, project_id, blueprint_id)

Configure Blueprint

Configure target machine characteristics: machine and disk types, network configuration, etc. Returns the modified object.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.BlueprintApi()
body = cloudendure_api.CloudEndureBlueprint() # CloudEndureBlueprint |
project_id = 'project_id_example' # str |
blueprint_id = 'blueprint_id_example' # str |

try:
    # Configure Blueprint
    api_response = api_instance.projects_project_id_blueprints_blueprint_id_patch(body, project_id, blueprint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlueprintApi->projects_project_id_blueprints_blueprint_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureBlueprint**](CloudEndureBlueprint.md)|  |
 **project_id** | **str**|  |
 **blueprint_id** | **str**|  |

### Return type

[**CloudEndureBlueprint**](CloudEndureBlueprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_blueprints_get**
> CloudEndureBlueprintList projects_project_id_blueprints_get(project_id, offset=offset, limit=limit)

List Blueprints

Returns the list of available blueprints in the project.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.BlueprintApi()
project_id = 'project_id_example' # str |
offset = 56 # int | With which item to start (0 based). (optional)
limit = 56 # int | A number specifying how many entries to return. (optional)

try:
    # List Blueprints
    api_response = api_instance.projects_project_id_blueprints_get(project_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlueprintApi->projects_project_id_blueprints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional]
 **limit** | **int**| A number specifying how many entries to return. | [optional]

### Return type

[**CloudEndureBlueprintList**](CloudEndureBlueprintList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

# **projects_project_id_blueprints_post**
> CloudEndureBlueprint projects_project_id_blueprints_post(body, project_id)

Create Blueprint

Define the target machine characteristics: machine and disk types, network configuration, etc. There can be only one blueprint per machine per region. Returns the newly created object.

### Example
```python
from __future__ import print_function
import time
from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudendure_api.BlueprintApi()
body = cloudendure_api.CloudEndureBlueprint() # CloudEndureBlueprint |
project_id = 'project_id_example' # str |

try:
    # Create Blueprint
    api_response = api_instance.projects_project_id_blueprints_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlueprintApi->projects_project_id_blueprints_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudEndureBlueprint**](CloudEndureBlueprint.md)|  |
 **project_id** | **str**|  |

### Return type

[**CloudEndureBlueprint**](CloudEndureBlueprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to README]](API_README.md)

