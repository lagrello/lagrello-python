# lagrello_client.ImagesApi

All URIs are relative to *https://api.lagrello.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_totp**](ImagesApi.md#images_totp) | **GET** /v1/images/totp | Returns a generated QR code


# **images_totp**
> file_type images_totp()

Returns a generated QR code

This endpoint does not do any lookups of any sort. It will just generate a QR code from the parameters supplied to it.

### Example

```python
import time
import lagrello_client
from lagrello_client.api import images_api
from lagrello_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.lagrello.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lagrello_client.Configuration(
    host = "https://api.lagrello.com"
)


# Enter a context with an instance of the API client
with lagrello_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = images_api.ImagesApi(api_client)
    tenant_name = "tenantName_example" # str | The company name you your users to see in their TOTP application (optional)
    user_id = "userId_example" # str | The userId of the user you want to create the TOTP QR image for (optional)
    user_secret = "userSecret_example" # str | The TOTP secret for the specified user (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a generated QR code
        api_response = api_instance.images_totp(tenant_name=tenant_name, user_id=user_id, user_secret=user_secret)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling ImagesApi->images_totp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The company name you your users to see in their TOTP application | [optional]
 **user_id** | **str**| The userId of the user you want to create the TOTP QR image for | [optional]
 **user_secret** | **str**| The TOTP secret for the specified user | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gives back the QR code as an image |  -  |
**400** | The payload of the request is not valid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

