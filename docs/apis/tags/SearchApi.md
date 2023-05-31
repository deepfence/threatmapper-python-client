<a id="__pageTop"></a>
# threatmapper.apis.tags.search_api.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_cloud_accounts**](#count_cloud_accounts) | **post** /deepfence/search/count/cloud-accounts | Count Cloud Nodes
[**count_cloud_compliance_scans**](#count_cloud_compliance_scans) | **post** /deepfence/search/count/cloud-compliance/scans | Count Cloud Compliance Scan results
[**count_cloud_compliances**](#count_cloud_compliances) | **post** /deepfence/search/count/cloud-compliances | Count Cloud compliances
[**count_cloud_resources**](#count_cloud_resources) | **post** /deepfence/search/count/cloud-resources | Count Cloud resources
[**count_compliance_scans**](#count_compliance_scans) | **post** /deepfence/search/count/compliance/scans | Count Compliance Scan results
[**count_compliances**](#count_compliances) | **post** /deepfence/search/count/compliances | Count Compliances
[**count_container_images**](#count_container_images) | **post** /deepfence/search/count/images | Count Container images
[**count_containers**](#count_containers) | **post** /deepfence/search/count/containers | Count Containers data
[**count_hosts**](#count_hosts) | **post** /deepfence/search/count/hosts | Count hosts
[**count_kubernetes_clusters**](#count_kubernetes_clusters) | **post** /deepfence/search/count/kubernetes-clusters | Count Kubernetes clusters
[**count_malware_scans**](#count_malware_scans) | **post** /deepfence/search/count/malware/scans | Count Malware Scan results
[**count_malwares**](#count_malwares) | **post** /deepfence/search/count/malwares | Count Malwares
[**count_nodes**](#count_nodes) | **get** /deepfence/search/count/nodes | Count nodes
[**count_pods**](#count_pods) | **post** /deepfence/search/count/pods | Count Pods
[**count_secrets**](#count_secrets) | **post** /deepfence/search/count/secrets | Count Secrets
[**count_secrets_scans**](#count_secrets_scans) | **post** /deepfence/search/count/secret/scans | Count Secret Scan results
[**count_vulnerabilities**](#count_vulnerabilities) | **post** /deepfence/search/count/vulnerabilities | Count Vulnerabilities
[**count_vulnerability_scans**](#count_vulnerability_scans) | **post** /deepfence/search/count/vulnerability/scans | Count Vulnerability Scan results
[**get_cloud_compliance_filters**](#get_cloud_compliance_filters) | **post** /deepfence/filters/cloud-compliance | Get Cloud Compliance Filters
[**get_compliance_filters**](#get_compliance_filters) | **post** /deepfence/filters/compliance | Get Compliance Filters
[**search_cloud_accounts**](#search_cloud_accounts) | **post** /deepfence/search/cloud-accounts | Search Cloud Nodes
[**search_cloud_compliance_scans**](#search_cloud_compliance_scans) | **post** /deepfence/search/cloud-compliance/scans | Search Cloud Compliance Scan results
[**search_cloud_compliances**](#search_cloud_compliances) | **post** /deepfence/search/cloud-compliances | Search Cloud compliances
[**search_cloud_resources**](#search_cloud_resources) | **post** /deepfence/search/cloud-resources | Search Cloud Resources
[**search_compliance_scans**](#search_compliance_scans) | **post** /deepfence/search/compliance/scans | Search Compliance Scan results
[**search_compliances**](#search_compliances) | **post** /deepfence/search/compliances | Search Compliances
[**search_container_images**](#search_container_images) | **post** /deepfence/search/images | Search Container images
[**search_containers**](#search_containers) | **post** /deepfence/search/containers | Search Containers data
[**search_hosts**](#search_hosts) | **post** /deepfence/search/hosts | Search hosts
[**search_kubernetes_clusters**](#search_kubernetes_clusters) | **post** /deepfence/search/kubernetes-clusters | Search Kuberenetes Clusters
[**search_malware_scans**](#search_malware_scans) | **post** /deepfence/search/malware/scans | Search Malware Scan results
[**search_malwares**](#search_malwares) | **post** /deepfence/search/malwares | Search Malwares
[**search_pods**](#search_pods) | **post** /deepfence/search/pods | Search Pods
[**search_secrets**](#search_secrets) | **post** /deepfence/search/secrets | Search Secrets
[**search_secrets_scans**](#search_secrets_scans) | **post** /deepfence/search/secret/scans | Search Secrets Scan results
[**search_vulnerabilities**](#search_vulnerabilities) | **post** /deepfence/search/vulnerabilities | Search Vulnerabilities
[**search_vulnerability_scans**](#search_vulnerability_scans) | **post** /deepfence/search/vulnerability/scans | Search Vulnerability Scan results

# **count_cloud_accounts**
<a id="count_cloud_accounts"></a>
> SearchSearchCountResp count_cloud_accounts()

Count Cloud Nodes

Search across all the data associated with cloud nodes

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Cloud Nodes
        api_response = api_instance.count_cloud_accounts(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_cloud_accounts: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_cloud_accounts.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_cloud_accounts.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_cloud_accounts.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_cloud_accounts.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_cloud_accounts.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_cloud_accounts.ApiResponseFor500) | Internal Server Error

#### count_cloud_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_cloud_accounts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_cloud_accounts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_cloud_accounts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_cloud_accounts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_cloud_accounts.ApiResponseFor500
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

# **count_cloud_compliance_scans**
<a id="count_cloud_compliance_scans"></a>
> SearchSearchCountResp count_cloud_compliance_scans()

Count Cloud Compliance Scan results

Count across all the data associated with cloud-compliance scans

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Count Cloud Compliance Scan results
        api_response = api_instance.count_cloud_compliance_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_cloud_compliance_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_cloud_compliance_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_cloud_compliance_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_cloud_compliance_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_cloud_compliance_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_cloud_compliance_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_cloud_compliance_scans.ApiResponseFor500) | Internal Server Error

#### count_cloud_compliance_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_cloud_compliance_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_cloud_compliance_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_cloud_compliance_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_cloud_compliance_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_cloud_compliance_scans.ApiResponseFor500
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

# **count_cloud_compliances**
<a id="count_cloud_compliances"></a>
> SearchSearchCountResp count_cloud_compliances()

Count Cloud compliances

Count across all the data ssociated with cloud compliances

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Cloud compliances
        api_response = api_instance.count_cloud_compliances(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_cloud_compliances: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_cloud_compliances.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_cloud_compliances.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_cloud_compliances.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_cloud_compliances.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_cloud_compliances.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_cloud_compliances.ApiResponseFor500) | Internal Server Error

#### count_cloud_compliances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_cloud_compliances.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_cloud_compliances.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_cloud_compliances.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_cloud_compliances.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_cloud_compliances.ApiResponseFor500
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

# **count_cloud_resources**
<a id="count_cloud_resources"></a>
> SearchSearchCountResp count_cloud_resources()

Count Cloud resources

Count across all the data ssociated with cloud resources

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Cloud resources
        api_response = api_instance.count_cloud_resources(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_cloud_resources: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_cloud_resources.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_cloud_resources.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_cloud_resources.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_cloud_resources.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_cloud_resources.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_cloud_resources.ApiResponseFor500) | Internal Server Error

#### count_cloud_resources.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_cloud_resources.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_cloud_resources.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_cloud_resources.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_cloud_resources.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_cloud_resources.ApiResponseFor500
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

# **count_compliance_scans**
<a id="count_compliance_scans"></a>
> SearchSearchCountResp count_compliance_scans()

Count Compliance Scan results

Count across all the data associated with compliance scans

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Count Compliance Scan results
        api_response = api_instance.count_compliance_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_compliance_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_compliance_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_compliance_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_compliance_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_compliance_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_compliance_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_compliance_scans.ApiResponseFor500) | Internal Server Error

#### count_compliance_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_compliance_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_compliance_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_compliance_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_compliance_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_compliance_scans.ApiResponseFor500
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

# **count_compliances**
<a id="count_compliances"></a>
> SearchSearchCountResp count_compliances()

Count Compliances

Count across all the data associated with compliances

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Compliances
        api_response = api_instance.count_compliances(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_compliances: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_compliances.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_compliances.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_compliances.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_compliances.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_compliances.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_compliances.ApiResponseFor500) | Internal Server Error

#### count_compliances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_compliances.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_compliances.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_compliances.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_compliances.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_compliances.ApiResponseFor500
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

# **count_container_images**
<a id="count_container_images"></a>
> SearchSearchCountResp count_container_images()

Count Container images

Count across all the data associated with container images

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Container images
        api_response = api_instance.count_container_images(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_container_images: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_container_images.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_container_images.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_container_images.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_container_images.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_container_images.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_container_images.ApiResponseFor500) | Internal Server Error

#### count_container_images.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_container_images.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_container_images.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_container_images.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_container_images.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_container_images.ApiResponseFor500
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

# **count_containers**
<a id="count_containers"></a>
> SearchSearchCountResp count_containers()

Count Containers data

Count across all the data associated with containers

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Containers data
        api_response = api_instance.count_containers(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_containers: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_containers.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_containers.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_containers.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_containers.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_containers.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_containers.ApiResponseFor500) | Internal Server Error

#### count_containers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_containers.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_containers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_containers.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_containers.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_containers.ApiResponseFor500
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

# **count_hosts**
<a id="count_hosts"></a>
> SearchSearchCountResp count_hosts()

Count hosts

Count across all the data associated with hosts

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count hosts
        api_response = api_instance.count_hosts(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_hosts: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_hosts.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_hosts.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_hosts.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_hosts.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_hosts.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_hosts.ApiResponseFor500) | Internal Server Error

#### count_hosts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_hosts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_hosts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_hosts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_hosts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_hosts.ApiResponseFor500
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

# **count_kubernetes_clusters**
<a id="count_kubernetes_clusters"></a>
> SearchSearchCountResp count_kubernetes_clusters()

Count Kubernetes clusters

Count across all the data ssociated with kubernetes clusters

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Kubernetes clusters
        api_response = api_instance.count_kubernetes_clusters(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_kubernetes_clusters: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_kubernetes_clusters.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_kubernetes_clusters.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_kubernetes_clusters.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_kubernetes_clusters.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_kubernetes_clusters.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_kubernetes_clusters.ApiResponseFor500) | Internal Server Error

#### count_kubernetes_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_kubernetes_clusters.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_kubernetes_clusters.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_kubernetes_clusters.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_kubernetes_clusters.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_kubernetes_clusters.ApiResponseFor500
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

# **count_malware_scans**
<a id="count_malware_scans"></a>
> SearchSearchCountResp count_malware_scans()

Count Malware Scan results

Count across all the data associated with malware scans

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Count Malware Scan results
        api_response = api_instance.count_malware_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_malware_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_malware_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_malware_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_malware_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_malware_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_malware_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_malware_scans.ApiResponseFor500) | Internal Server Error

#### count_malware_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_malware_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_malware_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_malware_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_malware_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_malware_scans.ApiResponseFor500
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

# **count_malwares**
<a id="count_malwares"></a>
> SearchSearchCountResp count_malwares()

Count Malwares

Count across all the data associated with malwares

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Malwares
        api_response = api_instance.count_malwares(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_malwares: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_malwares.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_malwares.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_malwares.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_malwares.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_malwares.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_malwares.ApiResponseFor500) | Internal Server Error

#### count_malwares.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_malwares.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_malwares.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_malwares.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_malwares.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_malwares.ApiResponseFor500
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

# **count_nodes**
<a id="count_nodes"></a>
> SearchNodeCountResp count_nodes()

Count nodes

Count hosts, containers, pods, k8s clusters, images

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.search_node_count_resp import SearchNodeCountResp
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
    api_instance = search_api.SearchApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Count nodes
        api_response = api_instance.count_nodes()
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_nodes: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_nodes.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_nodes.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_nodes.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_nodes.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_nodes.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_nodes.ApiResponseFor500) | Internal Server Error

#### count_nodes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchNodeCountResp**](../../models/SearchNodeCountResp.md) |  | 


#### count_nodes.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_nodes.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_nodes.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_nodes.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_nodes.ApiResponseFor500
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

# **count_pods**
<a id="count_pods"></a>
> SearchSearchCountResp count_pods()

Count Pods

Count across all the data associated with pods

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Pods
        api_response = api_instance.count_pods(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_pods: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_pods.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_pods.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_pods.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_pods.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_pods.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_pods.ApiResponseFor500) | Internal Server Error

#### count_pods.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_pods.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_pods.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_pods.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_pods.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_pods.ApiResponseFor500
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

# **count_secrets**
<a id="count_secrets"></a>
> SearchSearchCountResp count_secrets()

Count Secrets

Count across all the data associated with secrets

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Secrets
        api_response = api_instance.count_secrets(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_secrets: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_secrets.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_secrets.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_secrets.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_secrets.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_secrets.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_secrets.ApiResponseFor500) | Internal Server Error

#### count_secrets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_secrets.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_secrets.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_secrets.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_secrets.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_secrets.ApiResponseFor500
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

# **count_secrets_scans**
<a id="count_secrets_scans"></a>
> SearchSearchCountResp count_secrets_scans()

Count Secret Scan results

Count across all the data associated with secret scans

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Count Secret Scan results
        api_response = api_instance.count_secrets_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_secrets_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_secrets_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_secrets_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_secrets_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_secrets_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_secrets_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_secrets_scans.ApiResponseFor500) | Internal Server Error

#### count_secrets_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_secrets_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_secrets_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_secrets_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_secrets_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_secrets_scans.ApiResponseFor500
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

# **count_vulnerabilities**
<a id="count_vulnerabilities"></a>
> SearchSearchCountResp count_vulnerabilities()

Count Vulnerabilities

Search across all the data associated with vulnerabilities

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Count Vulnerabilities
        api_response = api_instance.count_vulnerabilities(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_vulnerabilities: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_vulnerabilities.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_vulnerabilities.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_vulnerabilities.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_vulnerabilities.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_vulnerabilities.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_vulnerabilities.ApiResponseFor500) | Internal Server Error

#### count_vulnerabilities.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_vulnerabilities.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_vulnerabilities.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_vulnerabilities.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_vulnerabilities.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_vulnerabilities.ApiResponseFor500
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

# **count_vulnerability_scans**
<a id="count_vulnerability_scans"></a>
> SearchSearchCountResp count_vulnerability_scans()

Count Vulnerability Scan results

Count across all the data associated with vulnerability scans

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
from threatmapper.model.search_search_count_resp import SearchSearchCountResp
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Count Vulnerability Scan results
        api_response = api_instance.count_vulnerability_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->count_vulnerability_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_vulnerability_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_vulnerability_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_vulnerability_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_vulnerability_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_vulnerability_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_vulnerability_scans.ApiResponseFor500) | Internal Server Error

#### count_vulnerability_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_vulnerability_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_vulnerability_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_vulnerability_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_vulnerability_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_vulnerability_scans.ApiResponseFor500
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

# **get_cloud_compliance_filters**
<a id="get_cloud_compliance_filters"></a>
> ModelFiltersResult get_cloud_compliance_filters()

Get Cloud Compliance Filters

Get all applicable filter values for cloud compliance

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_filters_result import ModelFiltersResult
from threatmapper.model.model_filters_req import ModelFiltersReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = ModelFiltersReq(
        filters=[
            "filters_example"
        ],
        having=dict(
            "key": None,
        ),
    )
    try:
        # Get Cloud Compliance Filters
        api_response = api_instance.get_cloud_compliance_filters(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->get_cloud_compliance_filters: %s\n" % e)
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
[**ModelFiltersReq**](../../models/ModelFiltersReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_cloud_compliance_filters.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_cloud_compliance_filters.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_cloud_compliance_filters.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_cloud_compliance_filters.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_cloud_compliance_filters.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_cloud_compliance_filters.ApiResponseFor500) | Internal Server Error

#### get_cloud_compliance_filters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelFiltersResult**](../../models/ModelFiltersResult.md) |  | 


#### get_cloud_compliance_filters.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### get_cloud_compliance_filters.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_cloud_compliance_filters.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_cloud_compliance_filters.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### get_cloud_compliance_filters.ApiResponseFor500
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

# **get_compliance_filters**
<a id="get_compliance_filters"></a>
> ModelFiltersResult get_compliance_filters()

Get Compliance Filters

Get all applicable filter values for compliance

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_filters_result import ModelFiltersResult
from threatmapper.model.model_filters_req import ModelFiltersReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = ModelFiltersReq(
        filters=[
            "filters_example"
        ],
        having=dict(
            "key": None,
        ),
    )
    try:
        # Get Compliance Filters
        api_response = api_instance.get_compliance_filters(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->get_compliance_filters: %s\n" % e)
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
[**ModelFiltersReq**](../../models/ModelFiltersReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_compliance_filters.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_compliance_filters.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_compliance_filters.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_compliance_filters.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_compliance_filters.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_compliance_filters.ApiResponseFor500) | Internal Server Error

#### get_compliance_filters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelFiltersResult**](../../models/ModelFiltersResult.md) |  | 


#### get_compliance_filters.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### get_compliance_filters.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_compliance_filters.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_compliance_filters.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### get_compliance_filters.ApiResponseFor500
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

# **search_cloud_accounts**
<a id="search_cloud_accounts"></a>
> [ModelCloudNodeAccountInfo] search_cloud_accounts()

Search Cloud Nodes

Search across all the data associated with cloud nodes

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_cloud_node_account_info import ModelCloudNodeAccountInfo
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Cloud Nodes
        api_response = api_instance.search_cloud_accounts(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_cloud_accounts: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_cloud_accounts.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_cloud_accounts.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_cloud_accounts.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_cloud_accounts.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_cloud_accounts.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_cloud_accounts.ApiResponseFor500) | Internal Server Error

#### search_cloud_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelCloudNodeAccountInfo**]({{complexTypePrefix}}ModelCloudNodeAccountInfo.md) | [**ModelCloudNodeAccountInfo**]({{complexTypePrefix}}ModelCloudNodeAccountInfo.md) | [**ModelCloudNodeAccountInfo**]({{complexTypePrefix}}ModelCloudNodeAccountInfo.md) |  | 

#### search_cloud_accounts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_cloud_accounts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_cloud_accounts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_cloud_accounts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_cloud_accounts.ApiResponseFor500
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

# **search_cloud_compliance_scans**
<a id="search_cloud_compliance_scans"></a>
> [ModelScanInfo] search_cloud_compliance_scans()

Search Cloud Compliance Scan results

Search across all the data associated with cloud-compliance scan

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_scan_info import ModelScanInfo
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Search Cloud Compliance Scan results
        api_response = api_instance.search_cloud_compliance_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_cloud_compliance_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_cloud_compliance_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_cloud_compliance_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_cloud_compliance_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_cloud_compliance_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_cloud_compliance_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_cloud_compliance_scans.ApiResponseFor500) | Internal Server Error

#### search_cloud_compliance_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) |  | 

#### search_cloud_compliance_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_cloud_compliance_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_cloud_compliance_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_cloud_compliance_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_cloud_compliance_scans.ApiResponseFor500
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

# **search_cloud_compliances**
<a id="search_cloud_compliances"></a>
> [ModelCloudCompliance] search_cloud_compliances()

Search Cloud compliances

Search across all the data associated with cloud-compliances

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
from threatmapper.model.model_cloud_compliance import ModelCloudCompliance
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Cloud compliances
        api_response = api_instance.search_cloud_compliances(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_cloud_compliances: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_cloud_compliances.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_cloud_compliances.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_cloud_compliances.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_cloud_compliances.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_cloud_compliances.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_cloud_compliances.ApiResponseFor500) | Internal Server Error

#### search_cloud_compliances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelCloudCompliance**]({{complexTypePrefix}}ModelCloudCompliance.md) | [**ModelCloudCompliance**]({{complexTypePrefix}}ModelCloudCompliance.md) | [**ModelCloudCompliance**]({{complexTypePrefix}}ModelCloudCompliance.md) |  | 

#### search_cloud_compliances.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_cloud_compliances.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_cloud_compliances.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_cloud_compliances.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_cloud_compliances.ApiResponseFor500
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

# **search_cloud_resources**
<a id="search_cloud_resources"></a>
> [ModelCloudResource] search_cloud_resources()

Search Cloud Resources

Search across all data associated with CloudResources

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_cloud_resource import ModelCloudResource
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Cloud Resources
        api_response = api_instance.search_cloud_resources(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_cloud_resources: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_cloud_resources.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_cloud_resources.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_cloud_resources.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_cloud_resources.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_cloud_resources.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_cloud_resources.ApiResponseFor500) | Internal Server Error

#### search_cloud_resources.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelCloudResource**]({{complexTypePrefix}}ModelCloudResource.md) | [**ModelCloudResource**]({{complexTypePrefix}}ModelCloudResource.md) | [**ModelCloudResource**]({{complexTypePrefix}}ModelCloudResource.md) |  | 

#### search_cloud_resources.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_cloud_resources.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_cloud_resources.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_cloud_resources.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_cloud_resources.ApiResponseFor500
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

# **search_compliance_scans**
<a id="search_compliance_scans"></a>
> [ModelScanInfo] search_compliance_scans()

Search Compliance Scan results

Search across all the data associated with compliance scan

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_scan_info import ModelScanInfo
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Search Compliance Scan results
        api_response = api_instance.search_compliance_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_compliance_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_compliance_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_compliance_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_compliance_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_compliance_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_compliance_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_compliance_scans.ApiResponseFor500) | Internal Server Error

#### search_compliance_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) |  | 

#### search_compliance_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_compliance_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_compliance_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_compliance_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_compliance_scans.ApiResponseFor500
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

# **search_compliances**
<a id="search_compliances"></a>
> [ModelCompliance] search_compliances()

Search Compliances

Search across all the data associated with compliances

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_compliance import ModelCompliance
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Compliances
        api_response = api_instance.search_compliances(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_compliances: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_compliances.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_compliances.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_compliances.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_compliances.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_compliances.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_compliances.ApiResponseFor500) | Internal Server Error

#### search_compliances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelCompliance**]({{complexTypePrefix}}ModelCompliance.md) | [**ModelCompliance**]({{complexTypePrefix}}ModelCompliance.md) | [**ModelCompliance**]({{complexTypePrefix}}ModelCompliance.md) |  | 

#### search_compliances.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_compliances.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_compliances.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_compliances.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_compliances.ApiResponseFor500
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

# **search_container_images**
<a id="search_container_images"></a>
> [ModelContainerImage] search_container_images()

Search Container images

Search across all the data associated with container images

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_container_image import ModelContainerImage
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Container images
        api_response = api_instance.search_container_images(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_container_images: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_container_images.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_container_images.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_container_images.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_container_images.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_container_images.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_container_images.ApiResponseFor500) | Internal Server Error

#### search_container_images.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelContainerImage**]({{complexTypePrefix}}ModelContainerImage.md) | [**ModelContainerImage**]({{complexTypePrefix}}ModelContainerImage.md) | [**ModelContainerImage**]({{complexTypePrefix}}ModelContainerImage.md) |  | 

#### search_container_images.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_container_images.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_container_images.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_container_images.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_container_images.ApiResponseFor500
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

# **search_containers**
<a id="search_containers"></a>
> [ModelContainer] search_containers()

Search Containers data

Search across all data associated with containers

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_container import ModelContainer
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Containers data
        api_response = api_instance.search_containers(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_containers: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_containers.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_containers.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_containers.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_containers.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_containers.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_containers.ApiResponseFor500) | Internal Server Error

#### search_containers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelContainer**]({{complexTypePrefix}}ModelContainer.md) | [**ModelContainer**]({{complexTypePrefix}}ModelContainer.md) | [**ModelContainer**]({{complexTypePrefix}}ModelContainer.md) |  | 

#### search_containers.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_containers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_containers.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_containers.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_containers.ApiResponseFor500
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

# **search_hosts**
<a id="search_hosts"></a>
> [ModelHost] search_hosts()

Search hosts

Search across all data associated with hosts

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_host import ModelHost
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search hosts
        api_response = api_instance.search_hosts(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_hosts: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_hosts.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_hosts.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_hosts.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_hosts.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_hosts.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_hosts.ApiResponseFor500) | Internal Server Error

#### search_hosts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelHost**]({{complexTypePrefix}}ModelHost.md) | [**ModelHost**]({{complexTypePrefix}}ModelHost.md) | [**ModelHost**]({{complexTypePrefix}}ModelHost.md) |  | 

#### search_hosts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_hosts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_hosts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_hosts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_hosts.ApiResponseFor500
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

# **search_kubernetes_clusters**
<a id="search_kubernetes_clusters"></a>
> [ModelKubernetesCluster] search_kubernetes_clusters()

Search Kuberenetes Clusters

Search across all data associated with kuberentes clusters

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.model_kubernetes_cluster import ModelKubernetesCluster
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Kuberenetes Clusters
        api_response = api_instance.search_kubernetes_clusters(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_kubernetes_clusters: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_kubernetes_clusters.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_kubernetes_clusters.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_kubernetes_clusters.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_kubernetes_clusters.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_kubernetes_clusters.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_kubernetes_clusters.ApiResponseFor500) | Internal Server Error

#### search_kubernetes_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelKubernetesCluster**]({{complexTypePrefix}}ModelKubernetesCluster.md) | [**ModelKubernetesCluster**]({{complexTypePrefix}}ModelKubernetesCluster.md) | [**ModelKubernetesCluster**]({{complexTypePrefix}}ModelKubernetesCluster.md) |  | 

#### search_kubernetes_clusters.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_kubernetes_clusters.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_kubernetes_clusters.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_kubernetes_clusters.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_kubernetes_clusters.ApiResponseFor500
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

# **search_malware_scans**
<a id="search_malware_scans"></a>
> [ModelScanInfo] search_malware_scans()

Search Malware Scan results

Search across all the data associated with malwares scan

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_scan_info import ModelScanInfo
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Search Malware Scan results
        api_response = api_instance.search_malware_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_malware_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_malware_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_malware_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_malware_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_malware_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_malware_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_malware_scans.ApiResponseFor500) | Internal Server Error

#### search_malware_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) |  | 

#### search_malware_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_malware_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_malware_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_malware_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_malware_scans.ApiResponseFor500
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

# **search_malwares**
<a id="search_malwares"></a>
> [ModelMalware] search_malwares()

Search Malwares

Search across all the data associated with malwares

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_malware import ModelMalware
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Malwares
        api_response = api_instance.search_malwares(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_malwares: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_malwares.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_malwares.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_malwares.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_malwares.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_malwares.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_malwares.ApiResponseFor500) | Internal Server Error

#### search_malwares.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelMalware**]({{complexTypePrefix}}ModelMalware.md) | [**ModelMalware**]({{complexTypePrefix}}ModelMalware.md) | [**ModelMalware**]({{complexTypePrefix}}ModelMalware.md) |  | 

#### search_malwares.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_malwares.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_malwares.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_malwares.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_malwares.ApiResponseFor500
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

# **search_pods**
<a id="search_pods"></a>
> [ModelPod] search_pods()

Search Pods

Search across all the data associated with pods

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_pod import ModelPod
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Pods
        api_response = api_instance.search_pods(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_pods: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_pods.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_pods.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_pods.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_pods.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_pods.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_pods.ApiResponseFor500) | Internal Server Error

#### search_pods.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelPod**]({{complexTypePrefix}}ModelPod.md) | [**ModelPod**]({{complexTypePrefix}}ModelPod.md) | [**ModelPod**]({{complexTypePrefix}}ModelPod.md) |  | 

#### search_pods.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_pods.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_pods.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_pods.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_pods.ApiResponseFor500
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

# **search_secrets**
<a id="search_secrets"></a>
> [ModelSecret] search_secrets()

Search Secrets

Search across all the data associated with secrets

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_secret import ModelSecret
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Secrets
        api_response = api_instance.search_secrets(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_secrets: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_secrets.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_secrets.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_secrets.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_secrets.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_secrets.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_secrets.ApiResponseFor500) | Internal Server Error

#### search_secrets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelSecret**]({{complexTypePrefix}}ModelSecret.md) | [**ModelSecret**]({{complexTypePrefix}}ModelSecret.md) | [**ModelSecret**]({{complexTypePrefix}}ModelSecret.md) |  | 

#### search_secrets.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_secrets.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_secrets.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_secrets.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_secrets.ApiResponseFor500
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

# **search_secrets_scans**
<a id="search_secrets_scans"></a>
> [ModelScanInfo] search_secrets_scans()

Search Secrets Scan results

Search across all the data associated with secrets scan

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_scan_info import ModelScanInfo
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Search Secrets Scan results
        api_response = api_instance.search_secrets_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_secrets_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_secrets_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_secrets_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_secrets_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_secrets_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_secrets_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_secrets_scans.ApiResponseFor500) | Internal Server Error

#### search_secrets_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) |  | 

#### search_secrets_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_secrets_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_secrets_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_secrets_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_secrets_scans.ApiResponseFor500
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

# **search_vulnerabilities**
<a id="search_vulnerabilities"></a>
> [ModelVulnerability] search_vulnerabilities()

Search Vulnerabilities

Search across all the data associated with vulnerabilities

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_vulnerability import ModelVulnerability
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.search_search_node_req import SearchSearchNodeReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchNodeReq(
        node_filter=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
,
    )
    try:
        # Search Vulnerabilities
        api_response = api_instance.search_vulnerabilities(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_vulnerabilities: %s\n" % e)
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
[**SearchSearchNodeReq**](../../models/SearchSearchNodeReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_vulnerabilities.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_vulnerabilities.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_vulnerabilities.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_vulnerabilities.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_vulnerabilities.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_vulnerabilities.ApiResponseFor500) | Internal Server Error

#### search_vulnerabilities.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelVulnerability**]({{complexTypePrefix}}ModelVulnerability.md) | [**ModelVulnerability**]({{complexTypePrefix}}ModelVulnerability.md) | [**ModelVulnerability**]({{complexTypePrefix}}ModelVulnerability.md) |  | 

#### search_vulnerabilities.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_vulnerabilities.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_vulnerabilities.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_vulnerabilities.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_vulnerabilities.ApiResponseFor500
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

# **search_vulnerability_scans**
<a id="search_vulnerability_scans"></a>
> [ModelScanInfo] search_vulnerability_scans()

Search Vulnerability Scan results

Search across all the data associated with vulnerability scan

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import search_api
from threatmapper.model.model_scan_info import ModelScanInfo
from threatmapper.model.search_search_scan_req import SearchSearchScanReq
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
    api_instance = search_api.SearchApi(api_client)

    # example passing only optional values
    body = SearchSearchScanReq(
        node_filters=SearchSearchFilter(
            filters=ReportersFieldsFilters(
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
            in_field_filter=[
                "in_field_filter_example"
            ],
            window=ModelFetchWindow(
                offset=1,
                size=1,
            ),
        ),
        scan_filters=SearchSearchFilter(),
,
    )
    try:
        # Search Vulnerability Scan results
        api_response = api_instance.search_vulnerability_scans(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SearchApi->search_vulnerability_scans: %s\n" % e)
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
[**SearchSearchScanReq**](../../models/SearchSearchScanReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_vulnerability_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#search_vulnerability_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#search_vulnerability_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_vulnerability_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_vulnerability_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#search_vulnerability_scans.ApiResponseFor500) | Internal Server Error

#### search_vulnerability_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) | [**ModelScanInfo**]({{complexTypePrefix}}ModelScanInfo.md) |  | 

#### search_vulnerability_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### search_vulnerability_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_vulnerability_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### search_vulnerability_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### search_vulnerability_scans.ApiResponseFor500
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

