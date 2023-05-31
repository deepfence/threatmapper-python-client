<a id="__pageTop"></a>
# threatmapper.apis.tags.diagnosis_api.DiagnosisApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnostic_notification**](#diagnostic_notification) | **get** /deepfence/diagnosis/notification | Get Diagnostic Notification
[**generate_agent_diagnostic_logs**](#generate_agent_diagnostic_logs) | **post** /deepfence/diagnosis/agent-logs | Generate Agent Diagnostic Logs
[**generate_console_diagnostic_logs**](#generate_console_diagnostic_logs) | **post** /deepfence/diagnosis/console-logs | Generate Console Diagnostic Logs
[**get_diagnostic_logs**](#get_diagnostic_logs) | **get** /deepfence/diagnosis/diagnostic-logs | Get Diagnostic Logs
[**update_agent_diagnostic_logs_status**](#update_agent_diagnostic_logs_status) | **put** /deepfence/diagnosis/agent-logs/status/{node_id} | Update Agent Diagnostic Logs Status

# **diagnostic_notification**
<a id="diagnostic_notification"></a>
> [DiagnosisDiagnosticNotification] diagnostic_notification()

Get Diagnostic Notification

Get Diagnostic Notification

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import diagnosis_api
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.diagnosis_diagnostic_notification import DiagnosisDiagnosticNotification
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
    api_instance = diagnosis_api.DiagnosisApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Diagnostic Notification
        api_response = api_instance.diagnostic_notification()
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling DiagnosisApi->diagnostic_notification: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#diagnostic_notification.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#diagnostic_notification.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#diagnostic_notification.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#diagnostic_notification.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#diagnostic_notification.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#diagnostic_notification.ApiResponseFor500) | Internal Server Error

#### diagnostic_notification.ApiResponseFor200
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
[**DiagnosisDiagnosticNotification**]({{complexTypePrefix}}DiagnosisDiagnosticNotification.md) | [**DiagnosisDiagnosticNotification**]({{complexTypePrefix}}DiagnosisDiagnosticNotification.md) | [**DiagnosisDiagnosticNotification**]({{complexTypePrefix}}DiagnosisDiagnosticNotification.md) |  | 

#### diagnostic_notification.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### diagnostic_notification.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### diagnostic_notification.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### diagnostic_notification.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### diagnostic_notification.ApiResponseFor500
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

# **generate_agent_diagnostic_logs**
<a id="generate_agent_diagnostic_logs"></a>
> generate_agent_diagnostic_logs()

Generate Agent Diagnostic Logs

Generate Agent Diagnostic Logs

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import diagnosis_api
from threatmapper.model.diagnosis_generate_agent_diagnostic_logs_request import DiagnosisGenerateAgentDiagnosticLogsRequest
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
    api_instance = diagnosis_api.DiagnosisApi(api_client)

    # example passing only optional values
    body = DiagnosisGenerateAgentDiagnosticLogsRequest(
        node_ids=[
            DiagnosisNodeIdentifier(
                node_id="node_id_example",
                node_type="host",
            )
        ],
        tail=1,
    )
    try:
        # Generate Agent Diagnostic Logs
        api_response = api_instance.generate_agent_diagnostic_logs(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling DiagnosisApi->generate_agent_diagnostic_logs: %s\n" % e)
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
[**DiagnosisGenerateAgentDiagnosticLogsRequest**](../../models/DiagnosisGenerateAgentDiagnosticLogsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_agent_diagnostic_logs.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_agent_diagnostic_logs.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_agent_diagnostic_logs.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_agent_diagnostic_logs.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#generate_agent_diagnostic_logs.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#generate_agent_diagnostic_logs.ApiResponseFor500) | Internal Server Error

#### generate_agent_diagnostic_logs.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### generate_agent_diagnostic_logs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### generate_agent_diagnostic_logs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### generate_agent_diagnostic_logs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### generate_agent_diagnostic_logs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### generate_agent_diagnostic_logs.ApiResponseFor500
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

# **generate_console_diagnostic_logs**
<a id="generate_console_diagnostic_logs"></a>
> generate_console_diagnostic_logs()

Generate Console Diagnostic Logs

Generate Console Diagnostic Logs

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import diagnosis_api
from threatmapper.model.diagnosis_generate_console_diagnostic_logs_request import DiagnosisGenerateConsoleDiagnosticLogsRequest
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
    api_instance = diagnosis_api.DiagnosisApi(api_client)

    # example passing only optional values
    body = DiagnosisGenerateConsoleDiagnosticLogsRequest(
        tail=1,
    )
    try:
        # Generate Console Diagnostic Logs
        api_response = api_instance.generate_console_diagnostic_logs(
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling DiagnosisApi->generate_console_diagnostic_logs: %s\n" % e)
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
[**DiagnosisGenerateConsoleDiagnosticLogsRequest**](../../models/DiagnosisGenerateConsoleDiagnosticLogsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_console_diagnostic_logs.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_console_diagnostic_logs.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_console_diagnostic_logs.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_console_diagnostic_logs.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#generate_console_diagnostic_logs.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#generate_console_diagnostic_logs.ApiResponseFor500) | Internal Server Error

#### generate_console_diagnostic_logs.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### generate_console_diagnostic_logs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### generate_console_diagnostic_logs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### generate_console_diagnostic_logs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### generate_console_diagnostic_logs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### generate_console_diagnostic_logs.ApiResponseFor500
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

# **get_diagnostic_logs**
<a id="get_diagnostic_logs"></a>
> DiagnosisGetDiagnosticLogsResponse get_diagnostic_logs()

Get Diagnostic Logs

Get diagnostic logs download url links

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import diagnosis_api
from threatmapper.model.diagnosis_get_diagnostic_logs_response import DiagnosisGetDiagnosticLogsResponse
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
    api_instance = diagnosis_api.DiagnosisApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Diagnostic Logs
        api_response = api_instance.get_diagnostic_logs()
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling DiagnosisApi->get_diagnostic_logs: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_diagnostic_logs.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_diagnostic_logs.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_diagnostic_logs.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_diagnostic_logs.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_diagnostic_logs.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_diagnostic_logs.ApiResponseFor500) | Internal Server Error

#### get_diagnostic_logs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DiagnosisGetDiagnosticLogsResponse**](../../models/DiagnosisGetDiagnosticLogsResponse.md) |  | 


#### get_diagnostic_logs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### get_diagnostic_logs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_diagnostic_logs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_diagnostic_logs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### get_diagnostic_logs.ApiResponseFor500
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

# **update_agent_diagnostic_logs_status**
<a id="update_agent_diagnostic_logs_status"></a>
> update_agent_diagnostic_logs_status(node_id)

Update Agent Diagnostic Logs Status

Update agent diagnostic logs status

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import diagnosis_api
from threatmapper.model.diagnosis_diagnostic_logs_status import DiagnosisDiagnosticLogsStatus
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
    api_instance = diagnosis_api.DiagnosisApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': "node_id_example",
    }
    try:
        # Update Agent Diagnostic Logs Status
        api_response = api_instance.update_agent_diagnostic_logs_status(
            path_params=path_params,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling DiagnosisApi->update_agent_diagnostic_logs_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'node_id': "node_id_example",
    }
    body = DiagnosisDiagnosticLogsStatus(
        message="message_example",
        status="status_example",
    )
    try:
        # Update Agent Diagnostic Logs Status
        api_response = api_instance.update_agent_diagnostic_logs_status(
            path_params=path_params,
            body=body,
        )
    except threatmapper.ApiException as e:
        print("Exception when calling DiagnosisApi->update_agent_diagnostic_logs_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DiagnosisDiagnosticLogsStatus**](../../models/DiagnosisDiagnosticLogsStatus.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
node_id | NodeIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_agent_diagnostic_logs_status.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#update_agent_diagnostic_logs_status.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_agent_diagnostic_logs_status.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#update_agent_diagnostic_logs_status.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_agent_diagnostic_logs_status.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#update_agent_diagnostic_logs_status.ApiResponseFor500) | Internal Server Error

#### update_agent_diagnostic_logs_status.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_agent_diagnostic_logs_status.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### update_agent_diagnostic_logs_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_agent_diagnostic_logs_status.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_agent_diagnostic_logs_status.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### update_agent_diagnostic_logs_status.ApiResponseFor500
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

