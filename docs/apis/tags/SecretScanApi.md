<a id="__pageTop"></a>
# threatmapper.apis.tags.secret_scan_api.SecretScanApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_results_secret_scan**](#count_results_secret_scan) | **post** /deepfence/scan/results/count/secret | Get Secret Scans Results
[**group_results_secrets**](#group_results_secrets) | **get** /deepfence/scan/results/count/group/secret | Group Secret Results
[**ingest_secret_scan_status**](#ingest_secret_scan_status) | **post** /deepfence/ingest/secret-scan-logs | Ingest Secrets Scan Status
[**ingest_secrets**](#ingest_secrets) | **post** /deepfence/ingest/secrets | Ingest Secrets
[**list_secret_scan**](#list_secret_scan) | **post** /deepfence/scan/list/secret | Get Secret Scans List
[**results_rules_secret_scan**](#results_rules_secret_scan) | **post** /deepfence/scan/results/secret/rules | Get Secret Scans Result Rules
[**results_secret_scan**](#results_secret_scan) | **post** /deepfence/scan/results/secret | Get Secret Scans Results
[**start_secret_scan**](#start_secret_scan) | **post** /deepfence/scan/start/secret | Start Secret Scan
[**status_secret_scan**](#status_secret_scan) | **post** /deepfence/scan/status/secret | Get Secret Scan Status
[**stop_secret_scan**](#stop_secret_scan) | **post** /deepfence/scan/stop/secret | Stop Secret Scan

# **count_results_secret_scan**
<a id="count_results_secret_scan"></a>
> SearchSearchCountResp count_results_secret_scan()

Get Secret Scans Results

Get Secret Scans results on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

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
        # Get Secret Scans Results
        api_response = api_instance.count_results_secret_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->count_results_secret_scan: %s\n" % e)
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
200 | [ApiResponseFor200](#count_results_secret_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#count_results_secret_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#count_results_secret_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#count_results_secret_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#count_results_secret_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#count_results_secret_scan.ApiResponseFor500) | Internal Server Error

#### count_results_secret_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchSearchCountResp**](../../models/SearchSearchCountResp.md) |  | 


#### count_results_secret_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### count_results_secret_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_results_secret_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_results_secret_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### count_results_secret_scan.ApiResponseFor500
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

# **group_results_secrets**
<a id="group_results_secrets"></a>
> SearchResultGroupResp group_results_secrets()

Group Secret Results

Group Secret Scans results by severity/rule

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.search_result_group_resp import SearchResultGroupResp
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Group Secret Results
        api_response = api_instance.group_results_secrets()
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->group_results_secrets: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#group_results_secrets.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#group_results_secrets.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#group_results_secrets.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#group_results_secrets.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#group_results_secrets.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#group_results_secrets.ApiResponseFor500) | Internal Server Error

#### group_results_secrets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResultGroupResp**](../../models/SearchResultGroupResp.md) |  | 


#### group_results_secrets.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### group_results_secrets.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### group_results_secrets.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### group_results_secrets.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### group_results_secrets.ApiResponseFor500
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

# **ingest_secret_scan_status**
<a id="ingest_secret_scan_status"></a>
> ingest_secret_scan_status()

Ingest Secrets Scan Status

Ingest secrets scan status from the agent

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
from threatmapper.model.ingesters_secret_scan_status import IngestersSecretScanStatus
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

    # example passing only optional values
    body = [
        IngestersSecretScanStatus(
            timestamp="1970-01-01T00:00:00.00Z",
            scan_id="scan_id_example",
            scan_message="scan_message_example",
            scan_status="scan_status_example",
        )
    ]
    try:
        # Ingest Secrets Scan Status
        api_response = api_instance.ingest_secret_scan_status(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->ingest_secret_scan_status: %s\n" % e)
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
[**IngestersSecretScanStatus**]({{complexTypePrefix}}IngestersSecretScanStatus.md) | [**IngestersSecretScanStatus**]({{complexTypePrefix}}IngestersSecretScanStatus.md) | [**IngestersSecretScanStatus**]({{complexTypePrefix}}IngestersSecretScanStatus.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ingest_secret_scan_status.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#ingest_secret_scan_status.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#ingest_secret_scan_status.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#ingest_secret_scan_status.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#ingest_secret_scan_status.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#ingest_secret_scan_status.ApiResponseFor500) | Internal Server Error

#### ingest_secret_scan_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_secret_scan_status.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### ingest_secret_scan_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_secret_scan_status.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_secret_scan_status.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### ingest_secret_scan_status.ApiResponseFor500
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

# **ingest_secrets**
<a id="ingest_secrets"></a>
> ingest_secrets()

Ingest Secrets

Ingest secrets found while scanning the agent

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
from threatmapper.model.ingesters_secret import IngestersSecret
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

    # example passing only optional values
    body = [
        IngestersSecret(
            timestamp="1970-01-01T00:00:00.00Z",
            image_layer_id="image_layer_id_example",
            match=dict(
                full_filename="full_filename_example",
                matched_content="matched_content_example",
                relative_ending_index=1,
                relative_starting_index=1,
                starting_index=1,
            ),
            rule=dict(
                id=1,
                name="name_example",
                part="part_example",
                signature_to_match="signature_to_match_example",
            ),
            severity=dict(
                level="level_example",
                score=3.14,
            ),
            masked=True,
            scan_id="scan_id_example",
        )
    ]
    try:
        # Ingest Secrets
        api_response = api_instance.ingest_secrets(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->ingest_secrets: %s\n" % e)
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
[**IngestersSecret**]({{complexTypePrefix}}IngestersSecret.md) | [**IngestersSecret**]({{complexTypePrefix}}IngestersSecret.md) | [**IngestersSecret**]({{complexTypePrefix}}IngestersSecret.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ingest_secrets.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#ingest_secrets.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#ingest_secrets.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#ingest_secrets.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#ingest_secrets.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#ingest_secrets.ApiResponseFor500) | Internal Server Error

#### ingest_secrets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_secrets.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### ingest_secrets.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_secrets.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ingest_secrets.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### ingest_secrets.ApiResponseFor500
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

# **list_secret_scan**
<a id="list_secret_scan"></a>
> ModelScanListResp list_secret_scan()

Get Secret Scans List

Get Secret Scans list on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

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
        # Get Secret Scans List
        api_response = api_instance.list_secret_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->list_secret_scan: %s\n" % e)
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
200 | [ApiResponseFor200](#list_secret_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_secret_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_secret_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_secret_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_secret_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_secret_scan.ApiResponseFor500) | Internal Server Error

#### list_secret_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelScanListResp**](../../models/ModelScanListResp.md) |  | 


#### list_secret_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### list_secret_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_secret_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_secret_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### list_secret_scan.ApiResponseFor500
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

# **results_rules_secret_scan**
<a id="results_rules_secret_scan"></a>
> ModelSecretScanResultRules results_rules_secret_scan()

Get Secret Scans Result Rules

Get Secret Scans detected rules names

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
from threatmapper.model.model_scan_results_req import ModelScanResultsReq
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_secret_scan_result_rules import ModelSecretScanResultRules
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

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
        # Get Secret Scans Result Rules
        api_response = api_instance.results_rules_secret_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->results_rules_secret_scan: %s\n" % e)
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
200 | [ApiResponseFor200](#results_rules_secret_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#results_rules_secret_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#results_rules_secret_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#results_rules_secret_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#results_rules_secret_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#results_rules_secret_scan.ApiResponseFor500) | Internal Server Error

#### results_rules_secret_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelSecretScanResultRules**](../../models/ModelSecretScanResultRules.md) |  | 


#### results_rules_secret_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### results_rules_secret_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### results_rules_secret_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### results_rules_secret_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### results_rules_secret_scan.ApiResponseFor500
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

# **results_secret_scan**
<a id="results_secret_scan"></a>
> ModelSecretScanResult results_secret_scan()

Get Secret Scans Results

Get Secret Scans results on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
from threatmapper.model.model_scan_results_req import ModelScanResultsReq
from threatmapper.model.model_secret_scan_result import ModelSecretScanResult
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

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
        # Get Secret Scans Results
        api_response = api_instance.results_secret_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->results_secret_scan: %s\n" % e)
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
200 | [ApiResponseFor200](#results_secret_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#results_secret_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#results_secret_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#results_secret_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#results_secret_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#results_secret_scan.ApiResponseFor500) | Internal Server Error

#### results_secret_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelSecretScanResult**](../../models/ModelSecretScanResult.md) |  | 


#### results_secret_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### results_secret_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### results_secret_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### results_secret_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### results_secret_scan.ApiResponseFor500
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

# **start_secret_scan**
<a id="start_secret_scan"></a>
> ModelScanTriggerResp start_secret_scan()

Start Secret Scan

Start Secret Scan on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
from threatmapper.model.model_secret_scan_trigger_req import ModelSecretScanTriggerReq
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

    # example passing only optional values
    body = ModelSecretScanTriggerReq(
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
        # Start Secret Scan
        api_response = api_instance.start_secret_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->start_secret_scan: %s\n" % e)
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
[**ModelSecretScanTriggerReq**](../../models/ModelSecretScanTriggerReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#start_secret_scan.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#start_secret_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#start_secret_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#start_secret_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#start_secret_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#start_secret_scan.ApiResponseFor500) | Internal Server Error

#### start_secret_scan.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelScanTriggerResp**](../../models/ModelScanTriggerResp.md) |  | 


#### start_secret_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### start_secret_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_secret_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_secret_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### start_secret_scan.ApiResponseFor500
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

# **status_secret_scan**
<a id="status_secret_scan"></a>
> ModelScanStatusResp status_secret_scan()

Get Secret Scan Status

Get Secret Scan Status on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

    # example passing only optional values
    body = ModelScanStatusReq(
        bulk_scan_id="bulk_scan_id_example",
        scan_ids=[
            "scan_ids_example"
        ],
    )
    try:
        # Get Secret Scan Status
        api_response = api_instance.status_secret_scan(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->status_secret_scan: %s\n" % e)
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
200 | [ApiResponseFor200](#status_secret_scan.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#status_secret_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#status_secret_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#status_secret_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#status_secret_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#status_secret_scan.ApiResponseFor500) | Internal Server Error

#### status_secret_scan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelScanStatusResp**](../../models/ModelScanStatusResp.md) |  | 


#### status_secret_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### status_secret_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### status_secret_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### status_secret_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### status_secret_scan.ApiResponseFor500
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

# **stop_secret_scan**
<a id="stop_secret_scan"></a>
> stop_secret_scan()

Stop Secret Scan

Stop Secret Scan on agent or registry

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import secret_scan_api
from threatmapper.model.model_secret_scan_trigger_req import ModelSecretScanTriggerReq
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
    api_instance = secret_scan_api.SecretScanApi(api_client)

    # example passing only optional values
    body = ModelSecretScanTriggerReq(
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
        # Stop Secret Scan
        api_response = api_instance.stop_secret_scan(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling SecretScanApi->stop_secret_scan: %s\n" % e)
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
[**ModelSecretScanTriggerReq**](../../models/ModelSecretScanTriggerReq.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#stop_secret_scan.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#stop_secret_scan.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#stop_secret_scan.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#stop_secret_scan.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#stop_secret_scan.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#stop_secret_scan.ApiResponseFor500) | Internal Server Error

#### stop_secret_scan.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### stop_secret_scan.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### stop_secret_scan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### stop_secret_scan.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### stop_secret_scan.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### stop_secret_scan.ApiResponseFor500
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

