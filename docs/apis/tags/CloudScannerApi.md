<a id="__pageTop"></a>
# threatmapper.apis.tags.cloud_scanner_api.CloudScannerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_results_cloud_compliance_scan**](#count_results_cloud_compliance_scan) | **post** /deepfence/scan/results/count/cloud-compliance | Get Cloud Compliance Scan Results
[**ingest_cloud_compliance_scan_status**](#ingest_cloud_compliance_scan_status) | **post** /deepfence/ingest/cloud-compliance-scan-status | Ingest Cloud Compliances
[**ingest_cloud_compliances**](#ingest_cloud_compliances) | **post** /deepfence/ingest/cloud-compliance | Ingest Cloud Compliances
[**list_cloud_compliance_scan**](#list_cloud_compliance_scan) | **post** /deepfence/scan/list/cloud-compliance | Get Cloud Compliance Scans List
[**results_cloud_compliance_scan**](#results_cloud_compliance_scan) | **post** /deepfence/scan/results/cloud-compliance | Get Cloud Compliance Scan Results
[**status_cloud_compliance_scan**](#status_cloud_compliance_scan) | **post** /deepfence/scan/status/cloud-compliance | Get Cloud Compliance Scan Status

# **count_results_cloud_compliance_scan**
<a id="count_results_cloud_compliance_scan"></a>
> SearchSearchCountResp count_results_cloud_compliance_scan()

Get Cloud Compliance Scan Results

Get Cloud Compliance Scan results for cloud node

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import cloud_scanner_api
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
    api_instance = cloud_scanner_api.CloudScannerApi(api_client)

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
        # Get Cloud Compliance Scan Results
        api_response = api_instance.count_results_cloud_compliance_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling CloudScannerApi->count_results_cloud_compliance_scan: %s\n" % e)
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
200 | [ApiResponseFor200](#count_results_cloud_compliance_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_results_cloud_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_results_cloud_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_results_cloud_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_results_cloud_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_results_cloud_compliance_scan.ApiResponseFor500) | Internal Server Error

#### count_results_cloud_compliance_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_results_cloud_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_results_cloud_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_results_cloud_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_results_cloud_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_results_cloud_compliance_scan.ApiResponseFor500
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

# **ingest_cloud_compliance_scan_status**
<a id="ingest_cloud_compliance_scan_status"></a>
> ingest_cloud_compliance_scan_status()

Ingest Cloud Compliances

Ingest Cloud compliances found while scanning cloud provider

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import cloud_scanner_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.ingesters_cloud_compliance import IngestersCloudCompliance
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
    api_instance = cloud_scanner_api.CloudScannerApi(api_client)

    # example passing only optional values
    body = [
        IngestersCloudCompliance(
            timestamp="timestamp_example",
            account_id="account_id_example",
            cloud_provider="cloud_provider_example",
            compliance_check_type="compliance_check_type_example",
            control_id="control_id_example",
            count=1,
            description="description_example",
            doc_id="doc_id_example",
            group="group_example",
            masked=True,
            reason="reason_example",
            region="region_example",
            resource="resource_example",
            scan_id="scan_id_example",
            service="service_example",
            severity="severity_example",
            status="status_example",
            title="title_example",
            type="type_example",
        )
    ]
    try:
        # Ingest Cloud Compliances
        api_response = api_instance.ingest_cloud_compliance_scan_status(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling CloudScannerApi->ingest_cloud_compliance_scan_status: %s\n" % e)
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
[**IngestersCloudCompliance**]({{complexTypePrefix}}IngestersCloudCompliance.md) | [**IngestersCloudCompliance**]({{complexTypePrefix}}IngestersCloudCompliance.md) | [**IngestersCloudCompliance**]({{complexTypePrefix}}IngestersCloudCompliance.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ingest_cloud_compliance_scan_status.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#ingest_cloud_compliance_scan_status.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#ingest_cloud_compliance_scan_status.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#ingest_cloud_compliance_scan_status.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#ingest_cloud_compliance_scan_status.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#ingest_cloud_compliance_scan_status.ApiResponseFor500) | Internal Server Error

#### ingest_cloud_compliance_scan_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_cloud_compliance_scan_status.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### ingest_cloud_compliance_scan_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_cloud_compliance_scan_status.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_cloud_compliance_scan_status.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### ingest_cloud_compliance_scan_status.ApiResponseFor500
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

# **ingest_cloud_compliances**
<a id="ingest_cloud_compliances"></a>
> ingest_cloud_compliances()

Ingest Cloud Compliances

Ingest Cloud compliances found while scanning cloud provider

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import cloud_scanner_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.ingesters_cloud_compliance import IngestersCloudCompliance
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
    api_instance = cloud_scanner_api.CloudScannerApi(api_client)

    # example passing only optional values
    body = [
        IngestersCloudCompliance(
            timestamp="timestamp_example",
            account_id="account_id_example",
            cloud_provider="cloud_provider_example",
            compliance_check_type="compliance_check_type_example",
            control_id="control_id_example",
            count=1,
            description="description_example",
            doc_id="doc_id_example",
            group="group_example",
            masked=True,
            reason="reason_example",
            region="region_example",
            resource="resource_example",
            scan_id="scan_id_example",
            service="service_example",
            severity="severity_example",
            status="status_example",
            title="title_example",
            type="type_example",
        )
    ]
    try:
        # Ingest Cloud Compliances
        api_response = api_instance.ingest_cloud_compliances(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling CloudScannerApi->ingest_cloud_compliances: %s\n" % e)
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
[**IngestersCloudCompliance**]({{complexTypePrefix}}IngestersCloudCompliance.md) | [**IngestersCloudCompliance**]({{complexTypePrefix}}IngestersCloudCompliance.md) | [**IngestersCloudCompliance**]({{complexTypePrefix}}IngestersCloudCompliance.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ingest_cloud_compliances.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#ingest_cloud_compliances.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#ingest_cloud_compliances.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#ingest_cloud_compliances.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#ingest_cloud_compliances.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#ingest_cloud_compliances.ApiResponseFor500) | Internal Server Error

#### ingest_cloud_compliances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_cloud_compliances.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### ingest_cloud_compliances.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_cloud_compliances.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_cloud_compliances.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### ingest_cloud_compliances.ApiResponseFor500
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

# **list_cloud_compliance_scan**
<a id="list_cloud_compliance_scan"></a>
> ModelScanListResp list_cloud_compliance_scan()

Get Cloud Compliance Scans List

Get Cloud Compliance Scans list for cloud node

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import cloud_scanner_api
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
    api_instance = cloud_scanner_api.CloudScannerApi(api_client)

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
        # Get Cloud Compliance Scans List
        api_response = api_instance.list_cloud_compliance_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling CloudScannerApi->list_cloud_compliance_scan: %s\n" % e)
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
200 | [ApiResponseFor200](#list_cloud_compliance_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_cloud_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_cloud_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_cloud_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_cloud_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_cloud_compliance_scan.ApiResponseFor500) | Internal Server Error

#### list_cloud_compliance_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelScanListResp**](../../models/ModelScanListResp.md) |  | 


#### list_cloud_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### list_cloud_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_cloud_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_cloud_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### list_cloud_compliance_scan.ApiResponseFor500
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

# **results_cloud_compliance_scan**
<a id="results_cloud_compliance_scan"></a>
> ModelCloudComplianceScanResult results_cloud_compliance_scan()

Get Cloud Compliance Scan Results

Get Cloud Compliance Scan results for cloud node

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import cloud_scanner_api
from threatmapper.model.model_scan_results_req import ModelScanResultsReq
from threatmapper.model.model_cloud_compliance_scan_result import ModelCloudComplianceScanResult
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
    api_instance = cloud_scanner_api.CloudScannerApi(api_client)

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
        # Get Cloud Compliance Scan Results
        api_response = api_instance.results_cloud_compliance_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling CloudScannerApi->results_cloud_compliance_scan: %s\n" % e)
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
200 | [ApiResponseFor200](#results_cloud_compliance_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#results_cloud_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#results_cloud_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#results_cloud_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#results_cloud_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#results_cloud_compliance_scan.ApiResponseFor500) | Internal Server Error

#### results_cloud_compliance_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelCloudComplianceScanResult**](../../models/ModelCloudComplianceScanResult.md) |  | 


#### results_cloud_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### results_cloud_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### results_cloud_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### results_cloud_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### results_cloud_compliance_scan.ApiResponseFor500
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

# **status_cloud_compliance_scan**
<a id="status_cloud_compliance_scan"></a>
> ModelComplianceScanStatusResp status_cloud_compliance_scan()

Get Cloud Compliance Scan Status

Get Cloud Compliance Scan Status on cloud node

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import cloud_scanner_api
from threatmapper.model.model_compliance_scan_status_resp import ModelComplianceScanStatusResp
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
    api_instance = cloud_scanner_api.CloudScannerApi(api_client)

    # example passing only optional values
    body = ModelScanStatusReq(
        bulk_scan_id="bulk_scan_id_example",
        scan_ids=[
            "scan_ids_example"
        ],
    )
    try:
        # Get Cloud Compliance Scan Status
        api_response = api_instance.status_cloud_compliance_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling CloudScannerApi->status_cloud_compliance_scan: %s\n" % e)
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
200 | [ApiResponseFor200](#status_cloud_compliance_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#status_cloud_compliance_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#status_cloud_compliance_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#status_cloud_compliance_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#status_cloud_compliance_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#status_cloud_compliance_scan.ApiResponseFor500) | Internal Server Error

#### status_cloud_compliance_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelComplianceScanStatusResp**](../../models/ModelComplianceScanStatusResp.md) |  | 


#### status_cloud_compliance_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### status_cloud_compliance_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### status_cloud_compliance_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### status_cloud_compliance_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### status_cloud_compliance_scan.ApiResponseFor500
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

