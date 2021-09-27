# lagrello_client.InternalApi

All URIs are relative to *https://api.lagrello.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenants_cardtoken**](InternalApi.md#tenants_cardtoken) | **GET** /v1/tenant/cardtoken | Returns token that is used by stripe to save card number.


# **tenants_cardtoken**
> str tenants_cardtoken()

Returns token that is used by stripe to save card number.

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import internal_api
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
    api_instance = internal_api.InternalApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns token that is used by stripe to save card number.
        api_response = api_instance.tenants_cardtoken()
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling InternalApi->tenants_cardtoken: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the token as a string |  -  |
**403** | The access token used to access resource is wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

