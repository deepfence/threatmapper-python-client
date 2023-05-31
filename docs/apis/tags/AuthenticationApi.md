<a id="__pageTop"></a>
# threatmapper.apis.tags.authentication_api.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_token**](#auth_token) | **post** /deepfence/auth/token | Get Access Token for API Token
[**auth_token_refresh**](#auth_token_refresh) | **post** /deepfence/auth/token/refresh | Refresh access token
[**login**](#login) | **post** /deepfence/user/login | Login API
[**logout**](#logout) | **post** /deepfence/user/logout | Logout API

# **auth_token**
<a id="auth_token"></a>
> ModelResponseAccessToken auth_token()

Get Access Token for API Token

Get access token for programmatic API access, by providing API Token

### Example

```python
import threatmapper
from threatmapper.apis.tags import authentication_api
from threatmapper.model.model_response_access_token import ModelResponseAccessToken
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_api_auth_request import ModelApiAuthRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = threatmapper.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with threatmapper.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = ModelApiAuthRequest(
        api_token="api_token_example",
    )
    try:
        # Get Access Token for API Token
        api_response = api_instance.auth_token(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling AuthenticationApi->auth_token: %s\n" % e)
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
[**ModelApiAuthRequest**](../../models/ModelApiAuthRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_token.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#auth_token.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#auth_token.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#auth_token.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#auth_token.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#auth_token.ApiResponseFor500) | Internal Server Error

#### auth_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelResponseAccessToken**](../../models/ModelResponseAccessToken.md) |  | 


#### auth_token.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### auth_token.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### auth_token.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### auth_token.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### auth_token.ApiResponseFor500
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_token_refresh**
<a id="auth_token_refresh"></a>
> ModelResponseAccessToken auth_token_refresh()

Refresh access token

Reissue access token using refresh token

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import authentication_api
from threatmapper.model.model_response_access_token import ModelResponseAccessToken
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Refresh access token
        api_response = api_instance.auth_token_refresh()
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling AuthenticationApi->auth_token_refresh: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_token_refresh.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#auth_token_refresh.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#auth_token_refresh.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#auth_token_refresh.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#auth_token_refresh.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#auth_token_refresh.ApiResponseFor500) | Internal Server Error

#### auth_token_refresh.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelResponseAccessToken**](../../models/ModelResponseAccessToken.md) |  | 


#### auth_token_refresh.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### auth_token_refresh.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### auth_token_refresh.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### auth_token_refresh.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### auth_token_refresh.ApiResponseFor500
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

# **login**
<a id="login"></a>
> ModelLoginResponse login()

Login API

Login API

### Example

```python
import threatmapper
from threatmapper.apis.tags import authentication_api
from threatmapper.model.model_login_request import ModelLoginRequest
from threatmapper.model.api_docs_bad_request_response import ApiDocsBadRequestResponse
from threatmapper.model.api_docs_failure_response import ApiDocsFailureResponse
from threatmapper.model.model_login_response import ModelLoginResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = threatmapper.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with threatmapper.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = ModelLoginRequest(
        email="email_example",
        password="password_example",
    )
    try:
        # Login API
        api_response = api_instance.login(
            body=body,
        )
        pprint(api_response)
    except threatmapper.ApiException as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
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
[**ModelLoginRequest**](../../models/ModelLoginRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#login.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#login.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#login.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#login.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#login.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#login.ApiResponseFor500) | Internal Server Error

#### login.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelLoginResponse**](../../models/ModelLoginResponse.md) |  | 


#### login.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### login.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### login.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### login.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### login.ApiResponseFor500
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

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **logout**
<a id="logout"></a>
> logout()

Logout API

Logout API

### Example

* Bearer (JWT) Authentication (bearer_token):
```python
import threatmapper
from threatmapper.apis.tags import authentication_api
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
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Logout API
        api_response = api_instance.logout()
    except threatmapper.ApiException as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#logout.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#logout.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#logout.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#logout.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#logout.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#logout.ApiResponseFor500) | Internal Server Error

#### logout.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### logout.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsBadRequestResponse**](../../models/ApiDocsBadRequestResponse.md) |  | 


#### logout.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### logout.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### logout.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDocsFailureResponse**](../../models/ApiDocsFailureResponse.md) |  | 


#### logout.ApiResponseFor500
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

