<a id="__pageTop"></a>
# threatmapper.apis.tags.topology_api.TopologyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_containers_topology_graph**](#get_containers_topology_graph) | **post** /deepfence/graph/topology/containers | Get Containers Topology Graph
[**get_hosts_topology_graph**](#get_hosts_topology_graph) | **post** /deepfence/graph/topology/hosts | Get Hosts Topology Graph
[**get_kubernetes_topology_graph**](#get_kubernetes_topology_graph) | **post** /deepfence/graph/topology/kubernetes | Get Kubernetes Topology Graph
[**get_pods_topology_graph**](#get_pods_topology_graph) | **post** /deepfence/graph/topology/pods | Get Pods Topology Graph
[**get_topology_graph**](#get_topology_graph) | **post** /deepfence/graph/topology/ | Get Topology Graph
[**ingest_agent_report**](#ingest_agent_report) | **post** /deepfence/ingest/report | Ingest Topology Data
[**ingest_sync_agent_report**](#ingest_sync_agent_report) | **post** /deepfence/ingest/sync-report | Ingest Topology Data

# **get_containers_topology_graph**
<a id="get_containers_topology_graph"></a>
> ApiDocsGraphResult get_containers_topology_graph()

Get Containers Topology Graph

Retrieve the full topology graph associated with the account from Containers

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import topology_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.graph_topology_filters import GraphTopologyFilters
from threatmapper.model.api_docs_graph_result import ApiDocsGraphResult
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
    api_instance = topology_api.TopologyApi(api_client)

    # example passing only optional values
    body = GraphTopologyFilters(
        cloud_filter=[
            "cloud_filter_example"
        ],
,
        field_filters=ReportersFieldsFilters(
            compare_filter=[
                ReportersCompareFilter(
                    field_name="field_name_example",
                    field_value=None,
                    greater_than=True,
                )
            ],
            contains_filter=ReportersContainsFilter(
                filter_in=dict(
                    "key": [
                        None
                    ],
                ),
            ),
            match_filter=ReportersMatchFilter(
                filter_in=dict(),
            ),
            not_contains_filter=ReportersContainsFilter(),
            order_filter=ReportersOrderFilter(
                order_fields=[
                    ReportersOrderSpec(
                        descending=True,
                        field_name="field_name_example",
                        size=1,
                    )
                ],
            ),
        ),
,
,
,
,
    )
    try:
        # Get Containers Topology Graph
        api_response = api_instance.get_containers_topology_graph(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling TopologyApi->get_containers_topology_graph: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphTopologyFilters**](../../models/GraphTopologyFilters.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_containers_topology_graph.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_containers_topology_graph.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_containers_topology_graph.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_containers_topology_graph.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_containers_topology_graph.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_containers_topology_graph.ApiResponseFor500) | Internal Server Error

#### get_containers_topology_graph.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsGraphResult**](../../models/ApiDocsGraphResult.md) |  | 


#### get_containers_topology_graph.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### get_containers_topology_graph.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_containers_topology_graph.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_containers_topology_graph.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### get_containers_topology_graph.ApiResponseFor500
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

# **get_hosts_topology_graph**
<a id="get_hosts_topology_graph"></a>
> ApiDocsGraphResult get_hosts_topology_graph()

Get Hosts Topology Graph

Retrieve the full topology graph associated with the account from Hosts

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import topology_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.graph_topology_filters import GraphTopologyFilters
from threatmapper.model.api_docs_graph_result import ApiDocsGraphResult
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
    api_instance = topology_api.TopologyApi(api_client)

    # example passing only optional values
    body = GraphTopologyFilters(
        cloud_filter=[
            "cloud_filter_example"
        ],
,
        field_filters=ReportersFieldsFilters(
            compare_filter=[
                ReportersCompareFilter(
                    field_name="field_name_example",
                    field_value=None,
                    greater_than=True,
                )
            ],
            contains_filter=ReportersContainsFilter(
                filter_in=dict(
                    "key": [
                        None
                    ],
                ),
            ),
            match_filter=ReportersMatchFilter(
                filter_in=dict(),
            ),
            not_contains_filter=ReportersContainsFilter(),
            order_filter=ReportersOrderFilter(
                order_fields=[
                    ReportersOrderSpec(
                        descending=True,
                        field_name="field_name_example",
                        size=1,
                    )
                ],
            ),
        ),
,
,
,
,
    )
    try:
        # Get Hosts Topology Graph
        api_response = api_instance.get_hosts_topology_graph(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling TopologyApi->get_hosts_topology_graph: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphTopologyFilters**](../../models/GraphTopologyFilters.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_hosts_topology_graph.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_hosts_topology_graph.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_hosts_topology_graph.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_hosts_topology_graph.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_hosts_topology_graph.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_hosts_topology_graph.ApiResponseFor500) | Internal Server Error

#### get_hosts_topology_graph.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsGraphResult**](../../models/ApiDocsGraphResult.md) |  | 


#### get_hosts_topology_graph.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### get_hosts_topology_graph.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_hosts_topology_graph.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_hosts_topology_graph.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### get_hosts_topology_graph.ApiResponseFor500
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

# **get_kubernetes_topology_graph**
<a id="get_kubernetes_topology_graph"></a>
> ApiDocsGraphResult get_kubernetes_topology_graph()

Get Kubernetes Topology Graph

Retrieve the full topology graph associated with the account from Kubernetes

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import topology_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.graph_topology_filters import GraphTopologyFilters
from threatmapper.model.api_docs_graph_result import ApiDocsGraphResult
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
    api_instance = topology_api.TopologyApi(api_client)

    # example passing only optional values
    body = GraphTopologyFilters(
        cloud_filter=[
            "cloud_filter_example"
        ],
,
        field_filters=ReportersFieldsFilters(
            compare_filter=[
                ReportersCompareFilter(
                    field_name="field_name_example",
                    field_value=None,
                    greater_than=True,
                )
            ],
            contains_filter=ReportersContainsFilter(
                filter_in=dict(
                    "key": [
                        None
                    ],
                ),
            ),
            match_filter=ReportersMatchFilter(
                filter_in=dict(),
            ),
            not_contains_filter=ReportersContainsFilter(),
            order_filter=ReportersOrderFilter(
                order_fields=[
                    ReportersOrderSpec(
                        descending=True,
                        field_name="field_name_example",
                        size=1,
                    )
                ],
            ),
        ),
,
,
,
,
    )
    try:
        # Get Kubernetes Topology Graph
        api_response = api_instance.get_kubernetes_topology_graph(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling TopologyApi->get_kubernetes_topology_graph: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphTopologyFilters**](../../models/GraphTopologyFilters.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_kubernetes_topology_graph.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_kubernetes_topology_graph.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_kubernetes_topology_graph.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_kubernetes_topology_graph.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_kubernetes_topology_graph.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_kubernetes_topology_graph.ApiResponseFor500) | Internal Server Error

#### get_kubernetes_topology_graph.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsGraphResult**](../../models/ApiDocsGraphResult.md) |  | 


#### get_kubernetes_topology_graph.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### get_kubernetes_topology_graph.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_topology_graph.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_kubernetes_topology_graph.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### get_kubernetes_topology_graph.ApiResponseFor500
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

# **get_pods_topology_graph**
<a id="get_pods_topology_graph"></a>
> ApiDocsGraphResult get_pods_topology_graph()

Get Pods Topology Graph

Retrieve the full topology graph associated with the account from Pods

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import topology_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.graph_topology_filters import GraphTopologyFilters
from threatmapper.model.api_docs_graph_result import ApiDocsGraphResult
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
    api_instance = topology_api.TopologyApi(api_client)

    # example passing only optional values
    body = GraphTopologyFilters(
        cloud_filter=[
            "cloud_filter_example"
        ],
,
        field_filters=ReportersFieldsFilters(
            compare_filter=[
                ReportersCompareFilter(
                    field_name="field_name_example",
                    field_value=None,
                    greater_than=True,
                )
            ],
            contains_filter=ReportersContainsFilter(
                filter_in=dict(
                    "key": [
                        None
                    ],
                ),
            ),
            match_filter=ReportersMatchFilter(
                filter_in=dict(),
            ),
            not_contains_filter=ReportersContainsFilter(),
            order_filter=ReportersOrderFilter(
                order_fields=[
                    ReportersOrderSpec(
                        descending=True,
                        field_name="field_name_example",
                        size=1,
                    )
                ],
            ),
        ),
,
,
,
,
    )
    try:
        # Get Pods Topology Graph
        api_response = api_instance.get_pods_topology_graph(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling TopologyApi->get_pods_topology_graph: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphTopologyFilters**](../../models/GraphTopologyFilters.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pods_topology_graph.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pods_topology_graph.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_pods_topology_graph.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_pods_topology_graph.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_pods_topology_graph.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_pods_topology_graph.ApiResponseFor500) | Internal Server Error

#### get_pods_topology_graph.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsGraphResult**](../../models/ApiDocsGraphResult.md) |  | 


#### get_pods_topology_graph.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### get_pods_topology_graph.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pods_topology_graph.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pods_topology_graph.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### get_pods_topology_graph.ApiResponseFor500
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

# **get_topology_graph**
<a id="get_topology_graph"></a>
> ApiDocsGraphResult get_topology_graph()

Get Topology Graph

Retrieve the full topology graph associated with the account

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import topology_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.graph_topology_filters import GraphTopologyFilters
from threatmapper.model.api_docs_graph_result import ApiDocsGraphResult
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
    api_instance = topology_api.TopologyApi(api_client)

    # example passing only optional values
    body = GraphTopologyFilters(
        cloud_filter=[
            "cloud_filter_example"
        ],
,
        field_filters=ReportersFieldsFilters(
            compare_filter=[
                ReportersCompareFilter(
                    field_name="field_name_example",
                    field_value=None,
                    greater_than=True,
                )
            ],
            contains_filter=ReportersContainsFilter(
                filter_in=dict(
                    "key": [
                        None
                    ],
                ),
            ),
            match_filter=ReportersMatchFilter(),
            not_contains_filter=ReportersContainsFilter(),
            order_filter=ReportersOrderFilter(
                order_fields=[
                    ReportersOrderSpec(
                        descending=True,
                        field_name="field_name_example",
                        size=1,
                    )
                ],
            ),
        ),
,
,
,
,
    )
    try:
        # Get Topology Graph
        api_response = api_instance.get_topology_graph(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling TopologyApi->get_topology_graph: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**GraphTopologyFilters**](../../models/GraphTopologyFilters.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_topology_graph.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_topology_graph.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_topology_graph.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_topology_graph.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_topology_graph.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_topology_graph.ApiResponseFor500) | Internal Server Error

#### get_topology_graph.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsGraphResult**](../../models/ApiDocsGraphResult.md) |  | 


#### get_topology_graph.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### get_topology_graph.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_topology_graph.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_topology_graph.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### get_topology_graph.ApiResponseFor500
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

# **ingest_agent_report**
<a id="ingest_agent_report"></a>
> ingest_agent_report()

Ingest Topology Data

Ingest data reported by one Agent

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import topology_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.report_raw_report import ReportRawReport
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
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
    api_instance = topology_api.TopologyApi(api_client)

    # example passing only optional values
    body = ReportRawReport(
        payload="payload_example",
    )
    try:
        # Ingest Topology Data
        api_response = api_instance.ingest_agent_report(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling TopologyApi->ingest_agent_report: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**ReportRawReport**](../../models/ReportRawReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ingest_agent_report.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#ingest_agent_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#ingest_agent_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#ingest_agent_report.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#ingest_agent_report.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#ingest_agent_report.ApiResponseFor500) | Internal Server Error

#### ingest_agent_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_agent_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### ingest_agent_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_agent_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_agent_report.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### ingest_agent_report.ApiResponseFor500
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

# **ingest_sync_agent_report**
<a id="ingest_sync_agent_report"></a>
> ingest_sync_agent_report()

Ingest Topology Data

Ingest data reported by one Agent

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import topology_api
from threatmapper.model.ingesters_report_ingestion_data import IngestersReportIngestionData
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
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
    api_instance = topology_api.TopologyApi(api_client)

    # example passing only optional values
    body = IngestersReportIngestionData(
        container_batch=[
            dict(
                "key": None,
            )
        ],
,
,
,
,
,
,
,
,
,
        num_merged=1,
,
,
,
,
,
    )
    try:
        # Ingest Topology Data
        api_response = api_instance.ingest_sync_agent_report(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling TopologyApi->ingest_sync_agent_report: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**IngestersReportIngestionData**](../../models/IngestersReportIngestionData.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ingest_sync_agent_report.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#ingest_sync_agent_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#ingest_sync_agent_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#ingest_sync_agent_report.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#ingest_sync_agent_report.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#ingest_sync_agent_report.ApiResponseFor500) | Internal Server Error

#### ingest_sync_agent_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_sync_agent_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### ingest_sync_agent_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_sync_agent_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_sync_agent_report.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### ingest_sync_agent_report.ApiResponseFor500
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

