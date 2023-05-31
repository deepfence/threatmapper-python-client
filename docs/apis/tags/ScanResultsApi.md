<a id="__pageTop"></a>
# threatmapper.apis.tags.scan_results_api.ScanResultsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_scans**](#bulk_delete_scans) | **post** /deepfence/scans/bulk/delete | Bulk Delete Scans
[**delete_scan_result**](#delete_scan_result) | **patch** /deepfence/scan/results/action/delete | Delete selected scan results
[**delete_scan_results_for_scan_id**](#delete_scan_results_for_scan_id) | **delete** /deepfence/scan/{scan_type}/{scan_id} | Delete all scan results for a scan id
[**download_scan_results**](#download_scan_results) | **get** /deepfence/scan/{scan_type}/{scan_id}/download | Download Scans Results
[**get_all_nodes_in_scan_results**](#get_all_nodes_in_scan_results) | **post** /deepfence/scan/nodes-in-result | Get all nodes in given scan result ids
[**mask_scan_result**](#mask_scan_result) | **post** /deepfence/scan/results/action/mask | Mask Scans Results
[**notify_scan_result**](#notify_scan_result) | **post** /deepfence/scan/results/action/notify | Notify Scans Results
[**unmask_scan_result**](#unmask_scan_result) | **post** /deepfence/scan/results/action/unmask | Unmask Scans Results

# **bulk_delete_scans**
<a id="bulk_delete_scans"></a>
> bulk_delete_scans()

Bulk Delete Scans

Bulk delete scans along with their results for a particular scan type

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import scan_results_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_bulk_delete_scans_request import ModelBulkDeleteScansRequest
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
    api_instance = scan_results_api.ScanResultsApi(api_client)

    # example passing only optional values
    body = ModelBulkDeleteScansRequest(
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
        scan_type="Secret",
    )
    try:
        # Bulk Delete Scans
        api_response = api_instance.bulk_delete_scans(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling ScanResultsApi->bulk_delete_scans: %s\n" % e)
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
[**ModelBulkDeleteScansRequest**](../../models/ModelBulkDeleteScansRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#bulk_delete_scans.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#bulk_delete_scans.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#bulk_delete_scans.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#bulk_delete_scans.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#bulk_delete_scans.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#bulk_delete_scans.ApiResponseFor500) | Internal Server Error

#### bulk_delete_scans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### bulk_delete_scans.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### bulk_delete_scans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### bulk_delete_scans.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### bulk_delete_scans.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### bulk_delete_scans.ApiResponseFor500
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

# **delete_scan_result**
<a id="delete_scan_result"></a>
> delete_scan_result()

Delete selected scan results

Delete selected scan results

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import scan_results_api
from threatmapper.model.model_scan_results_action_request import ModelScanResultsActionRequest
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
    api_instance = scan_results_api.ScanResultsApi(api_client)

    # example passing only optional values
    body = ModelScanResultsActionRequest(
        result_ids=[
            "result_ids_example"
        ],
        scan_id="scan_id_example",
        scan_type="SecretScan",
    )
    try:
        # Delete selected scan results
        api_response = api_instance.delete_scan_result(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling ScanResultsApi->delete_scan_result: %s\n" % e)
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
[**ModelScanResultsActionRequest**](../../models/ModelScanResultsActionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_scan_result.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_scan_result.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_scan_result.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#delete_scan_result.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_scan_result.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#delete_scan_result.ApiResponseFor500) | Internal Server Error

#### delete_scan_result.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_scan_result.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### delete_scan_result.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_scan_result.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_scan_result.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### delete_scan_result.ApiResponseFor500
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

# **delete_scan_results_for_scan_id**
<a id="delete_scan_results_for_scan_id"></a>
> delete_scan_results_for_scan_id(scan_idscan_type)

Delete all scan results for a scan id

Delete all scan results for a scan id

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import scan_results_api
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
    api_instance = scan_results_api.ScanResultsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scan_id': "scan_id_example",
        'scan_type': "SecretScan",
    }
    try:
        # Delete all scan results for a scan id
        api_response = api_instance.delete_scan_results_for_scan_id(
            path_params=path_params,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling ScanResultsApi->delete_scan_results_for_scan_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scan_id | ScanIdSchema | | 
scan_type | ScanTypeSchema | | 

# ScanIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ScanTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["SecretScan", "VulnerabilityScan", "MalwareScan", "ComplianceScan", "CloudComplianceScan", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_scan_results_for_scan_id.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_scan_results_for_scan_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_scan_results_for_scan_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#delete_scan_results_for_scan_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_scan_results_for_scan_id.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#delete_scan_results_for_scan_id.ApiResponseFor500) | Internal Server Error

#### delete_scan_results_for_scan_id.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_scan_results_for_scan_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### delete_scan_results_for_scan_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_scan_results_for_scan_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_scan_results_for_scan_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### delete_scan_results_for_scan_id.ApiResponseFor500
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

# **download_scan_results**
<a id="download_scan_results"></a>
> ModelDownloadScanResultsResponse download_scan_results(scan_idscan_type)

Download Scans Results

Download scan results

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import scan_results_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.model_download_scan_results_response import ModelDownloadScanResultsResponse
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
    api_instance = scan_results_api.ScanResultsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'scan_id': "scan_id_example",
        'scan_type': "SecretScan",
    }
    try:
        # Download Scans Results
        api_response = api_instance.download_scan_results(
            path_params=path_params,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling ScanResultsApi->download_scan_results: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scan_id | ScanIdSchema | | 
scan_type | ScanTypeSchema | | 

# ScanIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ScanTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["SecretScan", "VulnerabilityScan", "MalwareScan", "ComplianceScan", "CloudComplianceScan", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#download_scan_results.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#download_scan_results.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#download_scan_results.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#download_scan_results.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#download_scan_results.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#download_scan_results.ApiResponseFor500) | Internal Server Error

#### download_scan_results.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelDownloadScanResultsResponse**](../../models/ModelDownloadScanResultsResponse.md) |  | 


#### download_scan_results.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### download_scan_results.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### download_scan_results.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### download_scan_results.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### download_scan_results.ApiResponseFor500
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

# **get_all_nodes_in_scan_results**
<a id="get_all_nodes_in_scan_results"></a>
> [ModelScanResultBasicNode] get_all_nodes_in_scan_results()

Get all nodes in given scan result ids

Get all nodes in given scan result ids

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import scan_results_api
from threatmapper.model.model_scan_result_basic_node import ModelScanResultBasicNode
from threatmapper.model.model_nodes_in_scan_result_request import ModelNodesInScanResultRequest
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
    api_instance = scan_results_api.ScanResultsApi(api_client)

    # example passing only optional values
    body = ModelNodesInScanResultRequest(
        result_ids=[
            "result_ids_example"
        ],
        scan_type="SecretScan",
    )
    try:
        # Get all nodes in given scan result ids
        api_response = api_instance.get_all_nodes_in_scan_results(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling ScanResultsApi->get_all_nodes_in_scan_results: %s\n" % e)
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
[**ModelNodesInScanResultRequest**](../../models/ModelNodesInScanResultRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_nodes_in_scan_results.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_all_nodes_in_scan_results.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_all_nodes_in_scan_results.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_all_nodes_in_scan_results.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_all_nodes_in_scan_results.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_all_nodes_in_scan_results.ApiResponseFor500) | Internal Server Error

#### get_all_nodes_in_scan_results.ApiResponseFor200
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
[**ModelScanResultBasicNode**]({{complexTypePrefix}}ModelScanResultBasicNode.md) | [**ModelScanResultBasicNode**]({{complexTypePrefix}}ModelScanResultBasicNode.md) | [**ModelScanResultBasicNode**]({{complexTypePrefix}}ModelScanResultBasicNode.md) |  | 

#### get_all_nodes_in_scan_results.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### get_all_nodes_in_scan_results.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_all_nodes_in_scan_results.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_all_nodes_in_scan_results.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### get_all_nodes_in_scan_results.ApiResponseFor500
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

# **mask_scan_result**
<a id="mask_scan_result"></a>
> mask_scan_result()

Mask Scans Results

Mask scan results

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import scan_results_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_scan_results_mask_request import ModelScanResultsMaskRequest
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
    api_instance = scan_results_api.ScanResultsApi(api_client)

    # example passing only optional values
    body = ModelScanResultsMaskRequest(
        mask_across_hosts_and_images=True,
        result_ids=[
            "result_ids_example"
        ],
        scan_id="scan_id_example",
        scan_type="SecretScan",
    )
    try:
        # Mask Scans Results
        api_response = api_instance.mask_scan_result(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling ScanResultsApi->mask_scan_result: %s\n" % e)
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
[**ModelScanResultsMaskRequest**](../../models/ModelScanResultsMaskRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#mask_scan_result.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#mask_scan_result.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#mask_scan_result.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#mask_scan_result.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#mask_scan_result.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#mask_scan_result.ApiResponseFor500) | Internal Server Error

#### mask_scan_result.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### mask_scan_result.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### mask_scan_result.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### mask_scan_result.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### mask_scan_result.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### mask_scan_result.ApiResponseFor500
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

# **notify_scan_result**
<a id="notify_scan_result"></a>
> notify_scan_result()

Notify Scans Results

Notify scan results in connected integration channels

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import scan_results_api
from threatmapper.model.model_scan_results_action_request import ModelScanResultsActionRequest
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
    api_instance = scan_results_api.ScanResultsApi(api_client)

    # example passing only optional values
    body = ModelScanResultsActionRequest(
        result_ids=[
            "result_ids_example"
        ],
        scan_id="scan_id_example",
        scan_type="SecretScan",
    )
    try:
        # Notify Scans Results
        api_response = api_instance.notify_scan_result(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling ScanResultsApi->notify_scan_result: %s\n" % e)
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
[**ModelScanResultsActionRequest**](../../models/ModelScanResultsActionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#notify_scan_result.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#notify_scan_result.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#notify_scan_result.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#notify_scan_result.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#notify_scan_result.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#notify_scan_result.ApiResponseFor500) | Internal Server Error

#### notify_scan_result.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### notify_scan_result.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### notify_scan_result.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### notify_scan_result.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### notify_scan_result.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### notify_scan_result.ApiResponseFor500
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

# **unmask_scan_result**
<a id="unmask_scan_result"></a>
> unmask_scan_result()

Unmask Scans Results

Unmask scan results

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import scan_results_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_scan_results_mask_request import ModelScanResultsMaskRequest
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
    api_instance = scan_results_api.ScanResultsApi(api_client)

    # example passing only optional values
    body = ModelScanResultsMaskRequest(
        mask_across_hosts_and_images=True,
        result_ids=[
            "result_ids_example"
        ],
        scan_id="scan_id_example",
        scan_type="SecretScan",
    )
    try:
        # Unmask Scans Results
        api_response = api_instance.unmask_scan_result(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling ScanResultsApi->unmask_scan_result: %s\n" % e)
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
[**ModelScanResultsMaskRequest**](../../models/ModelScanResultsMaskRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#unmask_scan_result.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#unmask_scan_result.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#unmask_scan_result.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#unmask_scan_result.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#unmask_scan_result.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#unmask_scan_result.ApiResponseFor500) | Internal Server Error

#### unmask_scan_result.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### unmask_scan_result.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### unmask_scan_result.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### unmask_scan_result.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### unmask_scan_result.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### unmask_scan_result.ApiResponseFor500
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

