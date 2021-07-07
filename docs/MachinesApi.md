# cloudendure.MachinesApi

All URIs are relative to *https://console.cloudendure.com/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_machines_delete**](MachinesApi.md#projects_project_id_machines_delete) | **DELETE** /projects/{projectId}/machines | Uninstall multiple agents
[**projects_project_id_machines_get**](MachinesApi.md#projects_project_id_machines_get) | **GET** /projects/{projectId}/machines | List Machines
[**projects_project_id_machines_machine_id_delete**](MachinesApi.md#projects_project_id_machines_machine_id_delete) | **DELETE** /projects/{projectId}/machines/{machineId} | Uninstall agent
[**projects_project_id_machines_machine_id_get**](MachinesApi.md#projects_project_id_machines_machine_id_get) | **GET** /projects/{projectId}/machines/{machineId} | Get a specific machine.
[**projects_project_id_machines_machine_id_patch**](MachinesApi.md#projects_project_id_machines_machine_id_patch) | **PATCH** /projects/{projectId}/machines/{machineId} | Update a machine. Accepts only Launch time updates.
[**projects_project_id_machines_patch**](MachinesApi.md#projects_project_id_machines_patch) | **PATCH** /projects/{projectId}/machines | Batch-update multiple machines
[**projects_project_id_replicas_replica_id_get**](MachinesApi.md#projects_project_id_replicas_replica_id_get) | **GET** /projects/{projectId}/replicas/{replicaId} | Get Target Machine


# **projects_project_id_machines_delete**
> projects_project_id_machines_delete(project_id, machine_ids)

Uninstall multiple agents

Stops replication and removes the cloudendure agent from the specified machines. All cloud artifacts associated with those machines with the exception of launched target machines are deleted.

### Example

```python
import time
import cloudendure
from cloudendure.api import machines_api
from cloudendure.model.inline_object8 import InlineObject8
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = machines_api.MachinesApi(api_client)
    project_id = "projectId_example" # str | 
    machine_ids = InlineObject8(
        machine_ids=[
            "machine_ids_example",
        ],
    ) # InlineObject8 | 

    # example passing only required values which don't have defaults set
    try:
        # Uninstall multiple agents
        api_instance.projects_project_id_machines_delete(project_id, machine_ids)
    except cloudendure.ApiException as e:
        print("Exception when calling MachinesApi->projects_project_id_machines_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_ids** | [**InlineObject8**](InlineObject8.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Machines removed from CloudEndure service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_machines_get**
> MachinesList projects_project_id_machines_get(project_id)

List Machines

Returns the list of all source machines in the Project (i.e. machines that have an Agent installed).

### Example

```python
import time
import cloudendure
from cloudendure.api import machines_api
from cloudendure.model.machines_list import MachinesList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = machines_api.MachinesApi(api_client)
    project_id = "projectId_example" # str | 
    offset = 0 # int | With which item to start (0 based). (optional) if omitted the server will use the default value of 0
    limit = 1500 # int | A number specifying how many entries to return. (optional) if omitted the server will use the default value of 1500
    all = False # bool | When set to false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status. machines are consuming/ have consumed licenses.  Note that some license types are transferable and therefore once you remove the and set to true false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status.  (optional) if omitted the server will use the default value of False
    types = "types_example" # str | Use this url query param to control which machines are returned when doing GET.  If you do not include the \\\"types\\\" query param, you will only get source machines  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Machines
        api_response = api_instance.projects_project_id_machines_get(project_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling MachinesApi->projects_project_id_machines_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Machines
        api_response = api_instance.projects_project_id_machines_get(project_id, offset=offset, limit=limit, all=all, types=types)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling MachinesApi->projects_project_id_machines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **offset** | **int**| With which item to start (0 based). | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| A number specifying how many entries to return. | [optional] if omitted the server will use the default value of 1500
 **all** | **bool**| When set to false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status. machines are consuming/ have consumed licenses.  Note that some license types are transferable and therefore once you remove the and set to true false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status.  | [optional] if omitted the server will use the default value of False
 **types** | **str**| Use this url query param to control which machines are returned when doing GET.  If you do not include the \\\&quot;types\\\&quot; query param, you will only get source machines  | [optional]

### Return type

[**MachinesList**](MachinesList.md)

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

# **projects_project_id_machines_machine_id_delete**
> projects_project_id_machines_machine_id_delete(project_id, machine_id)

Uninstall agent

Stops replication and removes the cloudendure agent from this machine. All cloud artifacts associated with those machines with the exception of launched target machine are deleted.

### Example

```python
import time
import cloudendure
from cloudendure.api import machines_api
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = machines_api.MachinesApi(api_client)
    project_id = "projectId_example" # str | 
    machine_id = "machineId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Uninstall agent
        api_instance.projects_project_id_machines_machine_id_delete(project_id, machine_id)
    except cloudendure.ApiException as e:
        print("Exception when calling MachinesApi->projects_project_id_machines_machine_id_delete: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Machine removed from CloudEndure service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_machines_machine_id_get**
> Machine projects_project_id_machines_machine_id_get(project_id, machine_id)

Get a specific machine.

### Example

```python
import time
import cloudendure
from cloudendure.api import machines_api
from cloudendure.model.machine import Machine
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = machines_api.MachinesApi(api_client)
    project_id = "projectId_example" # str | 
    machine_id = "machineId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a specific machine.
        api_response = api_instance.projects_project_id_machines_machine_id_get(project_id, machine_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling MachinesApi->projects_project_id_machines_machine_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |

### Return type

[**Machine**](Machine.md)

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

# **projects_project_id_machines_machine_id_patch**
> Machine projects_project_id_machines_machine_id_patch(project_id, machine_id, machine)

Update a machine. Accepts only Launch time updates.

### Example

```python
import time
import cloudendure
from cloudendure.api import machines_api
from cloudendure.model.machine import Machine
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = machines_api.MachinesApi(api_client)
    project_id = "projectId_example" # str | 
    machine_id = "machineId_example" # str | 
    machine = Machine(
        original_source_cloud_id="original_source_cloud_id_example",
        source_properties=MachineSourceProperties(
            name="name_example",
            installed_applications=MachineSourcePropertiesInstalledApplications(
                items=[
                    MachineSourcePropertiesInstalledApplicationsItems(
                        application_name="application_name_example",
                    ),
                ],
                last_updated_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            disks=[
                MachineSourcePropertiesDisks(
                    is_protected=True,
                    name="name_example",
                    size=1,
                ),
            ],
            machine_cloud_state="machine_cloud_state_example",
            public_ips=[
                "public_ips_example",
            ],
            memory=1,
            os="os_example",
            cpu=[
                MachineSourcePropertiesCpu(
                    cores=1,
                    model_name="model_name_example",
                ),
            ],
            running_services=MachineSourcePropertiesRunningServices(
                items=[
                    MachineSourcePropertiesRunningServicesItems(
                        service_name="service_name_example",
                    ),
                ],
                last_updated_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            machine_cloud_id="machine_cloud_id_example",
        ),
        replication_info=MachineReplicationInfo(
            rescanned_storage_bytes=1,
            backlogged_storage_bytes=1,
            failback_client_last_seen_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_consistency_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            next_consistency_estimated_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            total_storage_bytes=1,
            initiation_states=MachineReplicationInfoInitiationStates(
                items=[
                    MachineReplicationInfoInitiationStatesItems(
                        steps=[
                            InitializationStep(
                                status="NOT_STARTED",
                                message="message_example",
                                update_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                name="WAITING_TO_INITIATE_REPLICATION",
                            ),
                        ],
                        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ],
                estimated_next_attempt_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            replicated_storage_bytes=1,
            last_seen_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_scan_start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        license=MachineLicense(
            start_of_use_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            license_id="license_id_example",
        ),
        tags=[
            "tags_example",
        ],
        restore_servers=[
            "restore_servers_example",
        ],
        from_point_in_time=PointInTime(
            id="id_example",
            date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        replication_status="STOPPED",
        replica="replica_example",
        id="id_example",
        replication_configuration=MachineReplicationConfiguration(
            volume_encryption_key="volume_encryption_key_example",
            replication_tags=[
                ReplicationConfigurationReplicationTags(
                    key="key_example",
                    value="value_example",
                ),
            ],
            disable_public_ip=True,
            cost_optimized_burst_balance_delta_threshold=1,
            subnet_host_project="subnet_host_project_example",
            no_rescan=True,
            replication_software_download_source="replication_software_download_source_example",
            cost_optimized_sc1_volumes_throughput_window_size_minutes=1,
            replication_server_type="replication_server_type_example",
            cost_optimized_burst_balance_window_size_minutes=1,
            use_low_cost_disks=True,
            compute_location_id="compute_location_id_example",
            subnet_id="subnet_id_example",
            logical_location_id="logical_location_id_example",
            cost_optimized_default_volumes_throughput_window_size_minutes=1,
            bandwidth_throttling=1,
            cost_optimized_burst_balance_threshold=1,
            use_dedicated_server=True,
            zone="zone_example",
            replicator_security_group_ids=[
                "replicator_security_group_ids_example",
            ],
            use_private_ip=True,
            auto_disk_detection=True,
            failback_client_id="failback_client_id_example",
            proxy_url="proxy_url_example",
            volume_encryption_allowed=True,
            object_storage_location="object_storage_location_example",
            archiving_enabled=True,
            converter_type="converter_type_example",
            storage_location_id="storage_location_id_example",
            use_cost_optimized_disk_type=True,
            staging_disks=[
                DiskConfig(
                    actual_type="actual_type_example",
                    type="DEFAULT",
                    iops=0,
                    throughput=0,
                    name="name_example",
                ),
            ],
        ),
        life_cycle=MachineLifeCycle(
            last_test_launch_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_recovery_job_id="last_recovery_job_id_example",
            last_recovery_launch_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_target_health_checks_passed_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            connection_established_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            agent_installation_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_target_health_checks_passed_job_id="last_target_health_checks_passed_job_id_example",
            last_cutover_job_id="last_cutover_job_id_example",
            last_test_launch_job_id="last_test_launch_job_id_example",
            last_cutover_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        is_agent_installed=True,
    ) # Machine | 

    # example passing only required values which don't have defaults set
    try:
        # Update a machine. Accepts only Launch time updates.
        api_response = api_instance.projects_project_id_machines_machine_id_patch(project_id, machine_id, machine)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling MachinesApi->projects_project_id_machines_machine_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machine_id** | **str**|  |
 **machine** | [**Machine**](Machine.md)|  |

### Return type

[**Machine**](Machine.md)

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

# **projects_project_id_machines_patch**
> MachinesList projects_project_id_machines_patch(project_id, machines_list)

Batch-update multiple machines

### Example

```python
import time
import cloudendure
from cloudendure.api import machines_api
from cloudendure.model.machines_list import MachinesList
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = machines_api.MachinesApi(api_client)
    project_id = "projectId_example" # str | 
    machines_list = MachinesList(
        items=[
            Machine(
                original_source_cloud_id="original_source_cloud_id_example",
                source_properties=MachineSourceProperties(
                    name="name_example",
                    installed_applications=MachineSourcePropertiesInstalledApplications(
                        items=[
                            MachineSourcePropertiesInstalledApplicationsItems(
                                application_name="application_name_example",
                            ),
                        ],
                        last_updated_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                    disks=[
                        MachineSourcePropertiesDisks(
                            is_protected=True,
                            name="name_example",
                            size=1,
                        ),
                    ],
                    machine_cloud_state="machine_cloud_state_example",
                    public_ips=[
                        "public_ips_example",
                    ],
                    memory=1,
                    os="os_example",
                    cpu=[
                        MachineSourcePropertiesCpu(
                            cores=1,
                            model_name="model_name_example",
                        ),
                    ],
                    running_services=MachineSourcePropertiesRunningServices(
                        items=[
                            MachineSourcePropertiesRunningServicesItems(
                                service_name="service_name_example",
                            ),
                        ],
                        last_updated_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                    machine_cloud_id="machine_cloud_id_example",
                ),
                replication_info=MachineReplicationInfo(
                    rescanned_storage_bytes=1,
                    backlogged_storage_bytes=1,
                    failback_client_last_seen_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    last_consistency_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    next_consistency_estimated_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    total_storage_bytes=1,
                    initiation_states=MachineReplicationInfoInitiationStates(
                        items=[
                            MachineReplicationInfoInitiationStatesItems(
                                steps=[
                                    InitializationStep(
                                        status="NOT_STARTED",
                                        message="message_example",
                                        update_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                        name="WAITING_TO_INITIATE_REPLICATION",
                                    ),
                                ],
                                start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            ),
                        ],
                        estimated_next_attempt_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                    replicated_storage_bytes=1,
                    last_seen_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    last_scan_start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
                license=MachineLicense(
                    start_of_use_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    license_id="license_id_example",
                ),
                tags=[
                    "tags_example",
                ],
                restore_servers=[
                    "restore_servers_example",
                ],
                from_point_in_time=PointInTime(
                    id="id_example",
                    date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
                replication_status="STOPPED",
                replica="replica_example",
                id="id_example",
                replication_configuration=MachineReplicationConfiguration(
                    volume_encryption_key="volume_encryption_key_example",
                    replication_tags=[
                        ReplicationConfigurationReplicationTags(
                            key="key_example",
                            value="value_example",
                        ),
                    ],
                    disable_public_ip=True,
                    cost_optimized_burst_balance_delta_threshold=1,
                    subnet_host_project="subnet_host_project_example",
                    no_rescan=True,
                    replication_software_download_source="replication_software_download_source_example",
                    cost_optimized_sc1_volumes_throughput_window_size_minutes=1,
                    replication_server_type="replication_server_type_example",
                    cost_optimized_burst_balance_window_size_minutes=1,
                    use_low_cost_disks=True,
                    compute_location_id="compute_location_id_example",
                    subnet_id="subnet_id_example",
                    logical_location_id="logical_location_id_example",
                    cost_optimized_default_volumes_throughput_window_size_minutes=1,
                    bandwidth_throttling=1,
                    cost_optimized_burst_balance_threshold=1,
                    use_dedicated_server=True,
                    zone="zone_example",
                    replicator_security_group_ids=[
                        "replicator_security_group_ids_example",
                    ],
                    use_private_ip=True,
                    auto_disk_detection=True,
                    failback_client_id="failback_client_id_example",
                    proxy_url="proxy_url_example",
                    volume_encryption_allowed=True,
                    object_storage_location="object_storage_location_example",
                    archiving_enabled=True,
                    converter_type="converter_type_example",
                    storage_location_id="storage_location_id_example",
                    use_cost_optimized_disk_type=True,
                    staging_disks=[
                        DiskConfig(
                            actual_type="actual_type_example",
                            type="DEFAULT",
                            iops=0,
                            throughput=0,
                            name="name_example",
                        ),
                    ],
                ),
                life_cycle=MachineLifeCycle(
                    last_test_launch_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    last_recovery_job_id="last_recovery_job_id_example",
                    last_recovery_launch_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    last_target_health_checks_passed_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    connection_established_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    agent_installation_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    last_target_health_checks_passed_job_id="last_target_health_checks_passed_job_id_example",
                    last_cutover_job_id="last_cutover_job_id_example",
                    last_test_launch_job_id="last_test_launch_job_id_example",
                    last_cutover_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
                is_agent_installed=True,
            ),
        ],
    ) # MachinesList | 

    # example passing only required values which don't have defaults set
    try:
        # Batch-update multiple machines
        api_response = api_instance.projects_project_id_machines_patch(project_id, machines_list)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling MachinesApi->projects_project_id_machines_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **machines_list** | [**MachinesList**](MachinesList.md)|  |

### Return type

[**MachinesList**](MachinesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of modified machines (All must succeed or fail). |  -  |
**400** | Bad request.  The server cannot process the request due to an apparent client error. The response body may include an error code and message.  - Error code tagLengthError means that one or more of the tags did not meet the tag length limits of  between 1 and 127 Unicode characters.  - Error code tagLimitReached means that processing the request would have resulted in one or more of  the machines exceeding the 50-tags-per-machine limit.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_replicas_replica_id_get**
> Replica projects_project_id_replicas_replica_id_get(project_id, replica_id)

Get Target Machine

### Example

```python
import time
import cloudendure
from cloudendure.api import machines_api
from cloudendure.model.error import Error
from cloudendure.model.replica import Replica
from pprint import pprint
# Defining the host is optional and defaults to https://console.cloudendure.com/api/latest
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudendure.Configuration(
    host = "https://console.cloudendure.com/api/latest"
)


# Enter a context with an instance of the API client
with cloudendure.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = machines_api.MachinesApi(api_client)
    project_id = "projectId_example" # str | 
    replica_id = "replicaId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Target Machine
        api_response = api_instance.projects_project_id_replicas_replica_id_get(project_id, replica_id)
        pprint(api_response)
    except cloudendure.ApiException as e:
        print("Exception when calling MachinesApi->projects_project_id_replicas_replica_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **replica_id** | **str**|  |

### Return type

[**Replica**](Replica.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully. |  -  |
**404** | Replica ID not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

