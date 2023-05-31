<a id="__pageTop"></a>
# threatmapper.apis.tags.cloud_resources_api.CloudResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_cloud_resources**](#ingest_cloud_resources) | **post** /deepfence/ingest/cloud-resources | Ingest Cloud resources

# **ingest_cloud_resources**
<a id="ingest_cloud_resources"></a>
> ingest_cloud_resources()

Ingest Cloud resources

Ingest Clouds Resources found while scanning cloud provider

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import cloud_resources_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.ingesters_cloud_resource import IngestersCloudResource
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = threatmapper.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer_token
configuration = threatmapper.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with threatmapper.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_resources_api.CloudResourcesApi(api_client)

    # example passing only optional values
    body = [
        IngestersCloudResource(
            access_level="access_level_example",
            account_id="account_id_example",
            action="action_example",
            allow_blob_public_access=True,
            arn="arn_example",
            attached_policy_arns=None,
            block_public_acls=True,
            block_public_policy=True,
            bucket_policy_is_public=True,
            cidr_ipv4="cidr_ipv4_example",
            cloud_provider="cloud_provider_example",
            container_definitions=None,
            containers=None,
            create_date="create_date_example",
            db_cluster_identifier="db_cluster_identifier_example",
            description="description_example",
            event_notification_configuration=None,
            group_id="group_id_example",
            groups=None,
            host_name="host_name_example",
            iam_instance_profile_arn="iam_instance_profile_arn_example",
            iam_instance_profile_id="iam_instance_profile_id_example",
            iam_policy=None,
            id="id_example",
            ignore_public_acls=True,
            ingress_settings="ingress_settings_example",
            inline_policies=None,
            instance_id="instance_id_example",
            instance_profile_arns=None,
            instances=None,
            ip_configuration=None,
            is_egress=True,
            name="name_example",
            network_configuration=None,
            network_interfaces=None,
            network_mode="network_mode_example",
            organization_id="organization_id_example",
            organization_master_account_arn="organization_master_account_arn_example",
            organization_master_account_email="organization_master_account_email_example",
            path="path_example",
            policy=None,
            policy_std=None,
            privilege="privilege_example",
            public_access="public_access_example",
            public_ip_address="public_ip_address_example",
            public_ips=None,
            public_network_access="public_network_access_example",
            region="region_example",
            resource_id="resource_id_example",
            resource_vpc_config=None,
            resources_vpc_config=None,
            restrict_public_buckets=True,
            scheme="scheme_example",
            security_groups=None,
            service_name="service_name_example",
            storage_account_name="storage_account_name_example",
            target_group_arn="target_group_arn_example",
            target_health_descriptions=None,
            task_definition=None,
            task_definition_arn="task_definition_arn_example",
            user_groups=None,
            user_id="user_id_example",
            users=None,
            vpc_id="vpc_id_example",
            vpc_options=None,
            vpc_security_group_ids=None,
            vpc_security_groups=None,
        )
    ]
    try:
        # Ingest Cloud resources
        api_response = api_instance.ingest_cloud_resources(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling CloudResourcesApi->ingest_cloud_resources: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IngestersCloudResource**]({{complexTypePrefix}}IngestersCloudResource.md) | [**IngestersCloudResource**]({{complexTypePrefix}}IngestersCloudResource.md) | [**IngestersCloudResource**]({{complexTypePrefix}}IngestersCloudResource.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ingest_cloud_resources.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#ingest_cloud_resources.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#ingest_cloud_resources.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#ingest_cloud_resources.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#ingest_cloud_resources.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#ingest_cloud_resources.ApiResponseFor500) | Internal Server Error

#### ingest_cloud_resources.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_cloud_resources.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### ingest_cloud_resources.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_cloud_resources.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_cloud_resources.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### ingest_cloud_resources.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


### Authorization

[bearer_token](../../../README.md#bearer_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

