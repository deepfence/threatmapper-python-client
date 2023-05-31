<a id="__pageTop"></a>
# threatmapper.apis.tags.compliance_api.ComplianceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_results_compliance_scan**](#count_results_compliance_scan) | **post** /deepfence/scan/results/count/compliance | Get Compliance Scans Results
[**ingest_compliances**](#ingest_compliances) | **post** /deepfence/ingest/compliance | Ingest Compliances
[**list_compliance_scan**](#list_compliance_scan) | **post** /deepfence/scan/list/compliance | Get Compliance Scans List
[**results_compliance_scan**](#results_compliance_scan) | **post** /deepfence/scan/results/compliance | Get Compliance Scans Results
[**start_compliance_scan**](#start_compliance_scan) | **post** /deepfence/scan/start/compliance | Start Compliance Scan
[**status_compliance_scan**](#status_compliance_scan) | **post** /deepfence/scan/status/compliance | Get Compliance Scan Status
[**stop_compliance_scan**](#stop_compliance_scan) | **post** /deepfence/scan/stop/compliance | Stop Compliance Scan

# **count_results_compliance_scan**
<a id="count_results_compliance_scan"></a>
> SearchSearchCountResp count_results_compliance_scan()

Get Compliance Scans Results

Get Compliance Scans results on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import compliance_api
from threatmapper.model.model_scan_results_req import ModelScanResultsReq
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
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only optional values
    body = ModelScanResultsReq(
        fields_filter=ReportersFieldsFilters(
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
        scan_id="scan_id_example",
        window=ModelFetchWindow(
            offset=1,
            size=1,
        ),
    )
    try:
        # Get Compliance Scans Results
        api_response = api_instance.count_results_compliance_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling ComplianceApi->count_results_compliance_scan: %s\n" % e)
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
[**ModelScanResultsReq**](../../models/ModelScanResultsReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_results_compliance_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_results_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_results_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_results_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_results_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_results_compliance_scan.ApiResponseFor500) | Internal Server Error

#### count_results_compliance_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_results_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_results_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_results_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_results_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_results_compliance_scan.ApiResponseFor500
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

# **ingest_compliances**
<a id="ingest_compliances"></a>
> ingest_compliances()

Ingest Compliances

Ingest compliance issues found while scanning the agent

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import compliance_api
from threatmapper.model.ingesters_compliance import IngestersCompliance
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
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only optional values
    body = [
        IngestersCompliance(
            timestamp="timestamp_example",
            compliance_check_type="compliance_check_type_example",
            description="description_example",
            masked=True,
            node_id="node_id_example",
            node_type="node_type_example",
            remediation_ansible="remediation_ansible_example",
            remediation_puppet="remediation_puppet_example",
            remediation_script="remediation_script_example",
            resource="resource_example",
            scan_id="scan_id_example",
            status="status_example",
            test_category="test_category_example",
            test_desc="test_desc_example",
            test_number="test_number_example",
            test_rationale="test_rationale_example",
            test_severity="test_severity_example",
            type="type_example",
        )
    ]
    try:
        # Ingest Compliances
        api_response = api_instance.ingest_compliances(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling ComplianceApi->ingest_compliances: %s\n" % e)
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
[**IngestersCompliance**]({{complexTypePrefix}}IngestersCompliance.md) | [**IngestersCompliance**]({{complexTypePrefix}}IngestersCompliance.md) | [**IngestersCompliance**]({{complexTypePrefix}}IngestersCompliance.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ingest_compliances.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#ingest_compliances.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#ingest_compliances.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#ingest_compliances.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#ingest_compliances.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#ingest_compliances.ApiResponseFor500) | Internal Server Error

#### ingest_compliances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_compliances.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### ingest_compliances.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_compliances.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_compliances.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### ingest_compliances.ApiResponseFor500
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

# **list_compliance_scan**
<a id="list_compliance_scan"></a>
> ModelScanListResp list_compliance_scan()

Get Compliance Scans List

Get Compliance Scans list on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import compliance_api
from threatmapper.model.model_scan_list_req import ModelScanListReq
from threatmapper.model.model_scan_list_resp import ModelScanListResp
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
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only optional values
    body = ModelScanListReq(
        fields_filter=ReportersFieldsFilters(
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
        node_ids=[
            ModelNodeIdentifier(
                node_id="node_id_example",
                node_type="image",
            )
        ],
        window=ModelFetchWindow(
            offset=1,
            size=1,
        ),
    )
    try:
        # Get Compliance Scans List
        api_response = api_instance.list_compliance_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling ComplianceApi->list_compliance_scan: %s\n" % e)
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
[**ModelScanListReq**](../../models/ModelScanListReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_compliance_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_compliance_scan.ApiResponseFor500) | Internal Server Error

#### list_compliance_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelScanListResp**](../../models/ModelScanListResp.md) |  | 


#### list_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### list_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### list_compliance_scan.ApiResponseFor500
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

# **results_compliance_scan**
<a id="results_compliance_scan"></a>
> ModelComplianceScanResult results_compliance_scan()

Get Compliance Scans Results

Get Compliance Scans results on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import compliance_api
from threatmapper.model.model_compliance_scan_result import ModelComplianceScanResult
from threatmapper.model.model_scan_results_req import ModelScanResultsReq
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
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only optional values
    body = ModelScanResultsReq(
        fields_filter=ReportersFieldsFilters(
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
        scan_id="scan_id_example",
        window=ModelFetchWindow(
            offset=1,
            size=1,
        ),
    )
    try:
        # Get Compliance Scans Results
        api_response = api_instance.results_compliance_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling ComplianceApi->results_compliance_scan: %s\n" % e)
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
[**ModelScanResultsReq**](../../models/ModelScanResultsReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#results_compliance_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#results_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#results_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#results_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#results_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#results_compliance_scan.ApiResponseFor500) | Internal Server Error

#### results_compliance_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelComplianceScanResult**](../../models/ModelComplianceScanResult.md) |  | 


#### results_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### results_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### results_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### results_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### results_compliance_scan.ApiResponseFor500
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

# **start_compliance_scan**
<a id="start_compliance_scan"></a>
> ModelScanTriggerResp start_compliance_scan()

Start Compliance Scan

Start Compliance Scan on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import compliance_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_compliance_scan_trigger_req import ModelComplianceScanTriggerReq
from threatmapper.model.model_scan_trigger_resp import ModelScanTriggerResp
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
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only optional values
    body = ModelComplianceScanTriggerReq(
        benchmark_types=[
            "benchmark_types_example"
        ],
        filters=ModelScanFilter(
            cloud_account_scan_filter=ReportersContainsFilter(
                filter_in=dict(
                    "key": [
                        None
                    ],
                ),
            ),
            container_scan_filter=ReportersContainsFilter(),
            host_scan_filter=ReportersContainsFilter(),
            image_scan_filter=ReportersContainsFilter(),
            kubernetes_cluster_scan_filter=ReportersContainsFilter(),
        ),
        node_ids=[
            ModelNodeIdentifier(
                node_id="node_id_example",
                node_type="image",
            )
        ],
    )
    try:
        # Start Compliance Scan
        api_response = api_instance.start_compliance_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling ComplianceApi->start_compliance_scan: %s\n" % e)
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
[**ModelComplianceScanTriggerReq**](../../models/ModelComplianceScanTriggerReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#start_compliance_scan.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#start_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#start_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#start_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#start_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#start_compliance_scan.ApiResponseFor500) | Internal Server Error

#### start_compliance_scan.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelScanTriggerResp**](../../models/ModelScanTriggerResp.md) |  | 


#### start_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### start_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### start_compliance_scan.ApiResponseFor500
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

# **status_compliance_scan**
<a id="status_compliance_scan"></a>
> ModelScanStatusResp status_compliance_scan()

Get Compliance Scan Status

Get Compliance Scan Status on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import compliance_api
from threatmapper.model.model_scan_status_resp import ModelScanStatusResp
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_scan_status_req import ModelScanStatusReq
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
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only optional values
    body = ModelScanStatusReq(
        bulk_scan_id="bulk_scan_id_example",
        scan_ids=[
            "scan_ids_example"
        ],
    )
    try:
        # Get Compliance Scan Status
        api_response = api_instance.status_compliance_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling ComplianceApi->status_compliance_scan: %s\n" % e)
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
[**ModelScanStatusReq**](../../models/ModelScanStatusReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#status_compliance_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#status_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#status_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#status_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#status_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#status_compliance_scan.ApiResponseFor500) | Internal Server Error

#### status_compliance_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelScanStatusResp**](../../models/ModelScanStatusResp.md) |  | 


#### status_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### status_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### status_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### status_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### status_compliance_scan.ApiResponseFor500
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

# **stop_compliance_scan**
<a id="stop_compliance_scan"></a>
> stop_compliance_scan()

Stop Compliance Scan

Stop Compliance Scan on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import compliance_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_compliance_scan_trigger_req import ModelComplianceScanTriggerReq
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
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only optional values
    body = ModelComplianceScanTriggerReq(
        benchmark_types=[
            "benchmark_types_example"
        ],
        filters=ModelScanFilter(
            cloud_account_scan_filter=ReportersContainsFilter(
                filter_in=dict(
                    "key": [
                        None
                    ],
                ),
            ),
            container_scan_filter=ReportersContainsFilter(),
            host_scan_filter=ReportersContainsFilter(),
            image_scan_filter=ReportersContainsFilter(),
            kubernetes_cluster_scan_filter=ReportersContainsFilter(),
        ),
        node_ids=[
            ModelNodeIdentifier(
                node_id="node_id_example",
                node_type="image",
            )
        ],
    )
    try:
        # Stop Compliance Scan
        api_response = api_instance.stop_compliance_scan(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling ComplianceApi->stop_compliance_scan: %s\n" % e)
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
[**ModelComplianceScanTriggerReq**](../../models/ModelComplianceScanTriggerReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#stop_compliance_scan.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#stop_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#stop_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#stop_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#stop_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#stop_compliance_scan.ApiResponseFor500) | Internal Server Error

#### stop_compliance_scan.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### stop_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### stop_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### stop_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### stop_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### stop_compliance_scan.ApiResponseFor500
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

