# cloudendure.BlueprintApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_blueprints_blueprint_id_get**](BlueprintApi.md#projects_project_id_blueprints_blueprint_id_get) | **GET** /projects/{projectId}/blueprints/{blueprintId} | Get Blueprint
[**projects_project_id_blueprints_blueprint_id_patch**](BlueprintApi.md#projects_project_id_blueprints_blueprint_id_patch) | **PATCH** /projects/{projectId}/blueprints/{blueprintId} | Configure Blueprint
[**projects_project_id_blueprints_get**](BlueprintApi.md#projects_project_id_blueprints_get) | **GET** /projects/{projectId}/blueprints | List Blueprints
[**projects_project_id_blueprints_post**](BlueprintApi.md#projects_project_id_blueprints_post) | **POST** /projects/{projectId}/blueprints | Create Blueprint


# **projects_project_id_blueprints_blueprint_id_get**
> Blueprint projects_project_id_blueprints_blueprint_id_get(project_id, blueprint_id)

Get Blueprint

### Example

```python
import time
import cloudendure
from cloudendure.api import blueprint_api
from cloudendure.model.blueprint import Blueprint
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blueprint_api.BlueprintApi(api_client)
    project_id = "projectId_example" # str | 
    blueprint_id = "blueprintId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Blueprint
        api_response = api_instance.projects_project_id_blueprints_blueprint_id_get(project_id, blueprint_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling BlueprintApi->projects_project_id_blueprints_blueprint_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **blueprint_id** | **str**|  |

### Return type

[**Blueprint**](Blueprint.md)

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

# **projects_project_id_blueprints_blueprint_id_patch**
> Blueprint projects_project_id_blueprints_blueprint_id_patch(project_id, blueprint_id, blueprint)

Configure Blueprint

Configure target machine characteristics: machine and disk types, network configuration, etc. Returns the modified object.

### Example

```python
import time
import cloudendure
from cloudendure.api import blueprint_api
from cloudendure.model.blueprint import Blueprint
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blueprint_api.BlueprintApi(api_client)
    project_id = "projectId_example" # str | 
    blueprint_id = "blueprintId_example" # str | 
    blueprint = Blueprint(
        iam_role="iam_role_example",
        scsi_adapter_type="scsi_adapter_type_example",
        public_ip_action="ALLOCATE",
        machine_name="machine_name_example",
        cpus=1,
        security_group_ids=[
            "security_group_ids_example",
        ],
        run_after_launch=True,
        recommended_private_ip="recommended_private_ip_example",
        instance_type="instance_type_example",
        mb_ram=1,
        network_interface="network_interface_example",
        subnet_ids=[
            "subnet_ids_example",
        ],
        cores_per_cpu=1,
        recommended_instance_type="recommended_instance_type_example",
        force_uefi=True,
        static_ip="static_ip_example",
        launch_on_instance_id="launch_on_instance_id_example",
        tags=[
            ReplicationConfigurationReplicationTags(
                key="key_example",
                value="value_example",
            ),
        ],
        security_group_action="FROM_POLICY",
        private_ips=[
            "private_ips_example",
        ],
        tenancy="SHARED",
        compute_location_id="compute_location_id_example",
        subnets_host_project="subnets_host_project_example",
        logical_location_id="logical_location_id_example",
        network_adapter_type="network_adapter_type_example",
        byol_on_dedicated_instance=True,
        placement_group="placement_group_example",
        machine_id="machine_id_example",
        region="region_example",
        disks=[
            BlueprintDisks(
                type="COPY_ORIGIN",
                iops=0,
                throughput=0,
                name="name_example",
            ),
        ],
        private_ip_action="CREATE_NEW",
        static_ip_action="EXISTING",
        id="id_example",
        dedicated_host_identifier="dedicated_host_identifier_example",
        use_shared_ram=True,
    ) # Blueprint | 

    # example passing only required values which don't have defaults set
    try:
        # Configure Blueprint
        api_response = api_instance.projects_project_id_blueprints_blueprint_id_patch(project_id, blueprint_id, blueprint)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling BlueprintApi->projects_project_id_blueprints_blueprint_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **blueprint_id** | **str**|  |
 **blueprint** | [**Blueprint**](Blueprint.md)|  |

### Return type

[**Blueprint**](Blueprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_blueprints_get**
> BlueprintList projects_project_id_blueprints_get(project_id)

List Blueprints

Returns the list of available blueprints in the project.

### Example

```python
import time
import cloudendure
from cloudendure.api import blueprint_api
from cloudendure.model.blueprint_list import BlueprintList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blueprint_api.BlueprintApi(api_client)
    project_id = "projectId_example" # str | 
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500

    # example passing only required values which don't have defaults set
    try:
        # List Blueprints
        api_response = api_instance.projects_project_id_blueprints_get(project_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling BlueprintApi->projects_project_id_blueprints_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Blueprints
        api_response = api_instance.projects_project_id_blueprints_get(project_id, offset=offset, limit=limit)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling BlueprintApi->projects_project_id_blueprints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500

### Return type

[**BlueprintList**](BlueprintList.md)

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

# **projects_project_id_blueprints_post**
> Blueprint projects_project_id_blueprints_post(project_id, blueprint)

Create Blueprint

Define the target machine characteristics: machine and disk types, network configuration, etc. There can be only one blueprint per machine per region. Returns the newly created object.

### Example

```python
import time
import cloudendure
from cloudendure.api import blueprint_api
from cloudendure.model.blueprint import Blueprint
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blueprint_api.BlueprintApi(api_client)
    project_id = "projectId_example" # str | 
    blueprint = Blueprint(
        iam_role="iam_role_example",
        scsi_adapter_type="scsi_adapter_type_example",
        public_ip_action="ALLOCATE",
        machine_name="machine_name_example",
        cpus=1,
        security_group_ids=[
            "security_group_ids_example",
        ],
        run_after_launch=True,
        recommended_private_ip="recommended_private_ip_example",
        instance_type="instance_type_example",
        mb_ram=1,
        network_interface="network_interface_example",
        subnet_ids=[
            "subnet_ids_example",
        ],
        cores_per_cpu=1,
        recommended_instance_type="recommended_instance_type_example",
        force_uefi=True,
        static_ip="static_ip_example",
        launch_on_instance_id="launch_on_instance_id_example",
        tags=[
            ReplicationConfigurationReplicationTags(
                key="key_example",
                value="value_example",
            ),
        ],
        security_group_action="FROM_POLICY",
        private_ips=[
            "private_ips_example",
        ],
        tenancy="SHARED",
        compute_location_id="compute_location_id_example",
        subnets_host_project="subnets_host_project_example",
        logical_location_id="logical_location_id_example",
        network_adapter_type="network_adapter_type_example",
        byol_on_dedicated_instance=True,
        placement_group="placement_group_example",
        machine_id="machine_id_example",
        region="region_example",
        disks=[
            BlueprintDisks(
                type="COPY_ORIGIN",
                iops=0,
                throughput=0,
                name="name_example",
            ),
        ],
        private_ip_action="CREATE_NEW",
        static_ip_action="EXISTING",
        id="id_example",
        dedicated_host_identifier="dedicated_host_identifier_example",
        use_shared_ram=True,
    ) # Blueprint | 

    # example passing only required values which don't have defaults set
    try:
        # Create Blueprint
        api_response = api_instance.projects_project_id_blueprints_post(project_id, blueprint)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling BlueprintApi->projects_project_id_blueprints_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **blueprint** | [**Blueprint**](Blueprint.md)|  |

### Return type

[**Blueprint**](Blueprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New object successfully created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

