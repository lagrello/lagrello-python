# lagrello_client.TokensApi

All URIs are relative to *https://api.lagrello.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokens_create**](TokensApi.md#tokens_create) | **POST** /v1/tokens | Creates new token
[**tokens_delete**](TokensApi.md#tokens_delete) | **DELETE** /v1/tokens/{id} | Deletes specifed access token
[**tokens_list**](TokensApi.md#tokens_list) | **GET** /v1/tokens | Returns a list of all active tokens in tenant


# **tokens_create**
> Token tokens_create()

Creates new token

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import tokens_api
from lagrello_client.model.create_token_request import CreateTokenRequest
from lagrello_client.model.token import Token
from pprint import pprint
# Defining the host is optional and defaults to https://api.lagrello.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lagrello_client.Configuration(
    host = "https://api.lagrello.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = lagrello_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with lagrello_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tokens_api.TokensApi(api_client)
    create_token_request = CreateTokenRequest(
        token_name="token_name_example",
        permissions=[
            "permissions_example",
        ],
    ) # CreateTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates new token
        api_response = api_instance.tokens_create(create_token_request=create_token_request)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling TokensApi->tokens_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_token_request** | [**CreateTokenRequest**](CreateTokenRequest.md)|  | [optional]

### Return type

[**Token**](Token.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the newly created token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_delete**
> tokens_delete(token_id)

Deletes specifed access token

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import tokens_api
from lagrello_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.lagrello.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lagrello_client.Configuration(
    host = "https://api.lagrello.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = lagrello_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with lagrello_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tokens_api.TokensApi(api_client)
    token_id = "ffd12fb4-da5b-4751-a9f6-d3214b418139" # str | Id of the token you want to delete

    # example passing only required values which don't have defaults set
    try:
        # Deletes specifed access token
        api_instance.tokens_delete(token_id)
    except lagrello_client.ApiException as e:
        print("Exception when calling TokensApi->tokens_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| Id of the token you want to delete |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted specified token |  -  |
**403** | The access token used to access resource is wrong |  -  |
**404** | token could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_list**
> TokenList tokens_list()

Returns a list of all active tokens in tenant

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import tokens_api
from lagrello_client.model.token_list import TokenList
from pprint import pprint
# Defining the host is optional and defaults to https://api.lagrello.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lagrello_client.Configuration(
    host = "https://api.lagrello.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = lagrello_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with lagrello_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tokens_api.TokensApi(api_client)
    size = 1 # int | Maximum of results per page (optional)
    page = 1 # int | The page you want to see (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of all active tokens in tenant
        api_response = api_instance.tokens_list(size=size, page=page)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling TokensApi->tokens_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Maximum of results per page | [optional]
 **page** | **int**| The page you want to see | [optional]

### Return type

[**TokenList**](TokenList.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paginated list of tokens |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

