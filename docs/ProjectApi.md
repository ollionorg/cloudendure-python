# cloudendure.ProjectApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_get**](ProjectApi.md#projects_get) | **GET** /projects | List Projects
[**projects_post**](ProjectApi.md#projects_post) | **POST** /projects | Create Project
[**projects_project_id_delete**](ProjectApi.md#projects_project_id_delete) | **DELETE** /projects/{projectId} | Delete Project and all sub-resources including cloud assets other than launched target machines
[**projects_project_id_get**](ProjectApi.md#projects_project_id_get) | **GET** /projects/{projectId} | Get Project
[**projects_project_id_patch**](ProjectApi.md#projects_project_id_patch) | **PATCH** /projects/{projectId} | Update Project (including partial update)
[**projects_project_id_tags_get**](ProjectApi.md#projects_project_id_tags_get) | **GET** /projects/{projectId}/tags | Gets all instance tags of all machines in the project.
[**projects_project_id_target_cloud_credentials_post**](ProjectApi.md#projects_project_id_target_cloud_credentials_post) | **POST** /projects/{projectId}/targetCloudCredentials | Set target cloud credentials


# **projects_get**
> ProjectsList projects_get()

List Projects

Returns the list of projects defined in this account.

### Example

```python
import time
import cloudendure
from cloudendure.api import project_api
from cloudendure.model.projects_list import ProjectsList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Projects
        api_response = api_instance.projects_get(offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ProjectApi->projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**ProjectsList**](ProjectsList.md)

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

# **projects_post**
> Project projects_post(project)

Create Project

Create project

### Example

```python
import time
import cloudendure
from cloudendure.api import project_api
from cloudendure.model.project import Project
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
    api_instance = project_api.ProjectApi(api_client)
    project = Project(
        replication_configuration="replication_configuration_example",
        features=ProjectFeatures(
            aws_extended_hdd_types=True,
            allow_recovery_plans=True,
            force_no_rescan_after_reboot=True,
            allow_no_rescan_after_reboot=True,
            allow_archiving=True,
            is_demo=True,
            dr_tier2=True,
            allow_byol_on_dedicated_instance=True,
            pit=True,
        ),
        replication_reversed=True,
        cloud_credentials_ids=[
            "cloud_credentials_ids_example",
        ],
        source_region="source_region_example",
        id="id_example",
        target_cloud_id="target_cloud_id_example",
        agent_installation_token="agent_installation_token_example",
        name="name_example",
        users_ids=[
            "users_ids_example",
        ],
        type="MIGRATION",
        source_cloud_credentials_id="source_cloud_credentials_id_example",
        target_cloud_credentials_id="target_cloud_credentials_id_example",
        licenses_ids=[
            "licenses_ids_example",
        ],
        ce_admin_properties=ProjectCeAdminProperties(
            comments="comments_example",
            history="history_example",
        ),
        source_cloud_id="source_cloud_id_example",
    ) # Project | 

    # example passing only required values which don't have defaults set
    try:
        # Create Project
        api_response = api_instance.projects_post(project)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ProjectApi->projects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)|  |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Project created. |  -  |
**400** | Max Projects per Account reached. |  -  |
**409** | Cannot be completed due to conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_delete**
> projects_project_id_delete(project_id)

Delete Project and all sub-resources including cloud assets other than launched target machines

### Example

```python
import time
import cloudendure
from cloudendure.api import project_api
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Project and all sub-resources including cloud assets other than launched target machines
        api_instance.projects_project_id_delete(project_id)
    except cloudendure.ApiException as e:
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_get**
> Project projects_project_id_get(project_id)

Get Project

### Example

```python
import time
import cloudendure
from cloudendure.api import project_api
from cloudendure.model.project import Project
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Project
        api_response = api_instance.projects_project_id_get(project_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ProjectApi->projects_project_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**Project**](Project.md)

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

# **projects_project_id_patch**
> Project projects_project_id_patch(project_id, project)

Update Project (including partial update)

Set project properties including Data Replication source location and replicationConfiguration to use.

### Example

```python
import time
import cloudendure
from cloudendure.api import project_api
from cloudendure.model.project import Project
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
    api_instance = project_api.ProjectApi(api_client)
    project_id = "projectId_example" # str | 
    project = Project(
        replication_configuration="replication_configuration_example",
        features=ProjectFeatures(
            aws_extended_hdd_types=True,
            allow_recovery_plans=True,
            force_no_rescan_after_reboot=True,
            allow_no_rescan_after_reboot=True,
            allow_archiving=True,
            is_demo=True,
            dr_tier2=True,
            allow_byol_on_dedicated_instance=True,
            pit=True,
        ),
        replication_reversed=True,
        cloud_credentials_ids=[
            "cloud_credentials_ids_example",
        ],
        source_region="source_region_example",
        id="id_example",
        target_cloud_id="target_cloud_id_example",
        agent_installation_token="agent_installation_token_example",
        name="name_example",
        users_ids=[
            "users_ids_example",
        ],
        type="MIGRATION",
        source_cloud_credentials_id="source_cloud_credentials_id_example",
        target_cloud_credentials_id="target_cloud_credentials_id_example",
        licenses_ids=[
            "licenses_ids_example",
        ],
        ce_admin_properties=ProjectCeAdminProperties(
            comments="comments_example",
            history="history_example",
        ),
        source_cloud_id="source_cloud_id_example",
    ) # Project | 

    # example passing only required values which don't have defaults set
    try:
        # Update Project (including partial update)
        api_response = api_instance.projects_project_id_patch(project_id, project)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ProjectApi->projects_project_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **project** | [**Project**](Project.md)|  |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object updated successfully. |  -  |
**409** | Cannot be completed due to conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_tags_get**
> InlineResponse200 projects_project_id_tags_get(project_id)

Gets all instance tags of all machines in the project.

Returns all instance tags of all machines in the project.

### Example

```python
import time
import cloudendure
from cloudendure.api import project_api
from cloudendure.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)
    project_id = "projectId_example" # str | 
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    try:
        # Gets all instance tags of all machines in the project.
        api_response = api_instance.projects_project_id_tags_get(project_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ProjectApi->projects_project_id_tags_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets all instance tags of all machines in the project.
        api_response = api_instance.projects_project_id_tags_get(project_id, offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ProjectApi->projects_project_id_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **projects_project_id_target_cloud_credentials_post**
> Project projects_project_id_target_cloud_credentials_post(project_id, cloud_credentials)

Set target cloud credentials

Used to set different account for staging and target. Changes target credentials for account. null values can be used to remove the credentials. 

### Example

```python
import time
import cloudendure
from cloudendure.api import project_api
from cloudendure.model.cloud_credentials_request import CloudCredentialsRequest
from cloudendure.model.project import Project
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
    api_instance = project_api.ProjectApi(api_client)
    project_id = "projectId_example" # str | 
    cloud_credentials = CloudCredentialsRequest(
        public_key="public_key_example",
        name="name_example",
        cloud_id="cloud_id_example",
        private_key='YQ==',
        account_identifier="account_identifier_example",
        id="id_example",
    ) # CloudCredentialsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set target cloud credentials
        api_response = api_instance.projects_project_id_target_cloud_credentials_post(project_id, cloud_credentials)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling ProjectApi->projects_project_id_target_cloud_credentials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **cloud_credentials** | [**CloudCredentialsRequest**](CloudCredentialsRequest.md)|  |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**409** | Cannot be completed due to conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

