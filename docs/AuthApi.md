# lagrello_client.AuthApi

All URIs are relative to *https://api.lagrello.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_email_auth**](AuthApi.md#users_email_auth) | **GET** /v1/users/email | Gives back user data for the magic link token
[**users_email_send**](AuthApi.md#users_email_send) | **POST** /v1/users/{userId}/email | This endpoint will be used when you want to send a magic login link to specified user
[**users_totp_auth**](AuthApi.md#users_totp_auth) | **GET** /v1/users/{userId}/totp | Verify users TOTP token
[**users_totp_toggle**](AuthApi.md#users_totp_toggle) | **POST** /v1/users/{userId}/totp | Enables or disables Time-based One-Time Password authentication method for specified user


# **users_email_auth**
> User users_email_auth(payload)

Gives back user data for the magic link token

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import auth_api
from lagrello_client.model.user import User
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
    api_instance = auth_api.AuthApi(api_client)
    payload = "payload_example" # str | The magic link token the user sent

    # example passing only required values which don't have defaults set
    try:
        # Gives back user data for the magic link token
        api_response = api_instance.users_email_auth(payload)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling AuthApi->users_email_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | **str**| The magic link token the user sent |

### Return type

[**User**](User.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user data for authenticated user |  -  |
**401** | End users token is wrong, DO NOT authenticate user |  -  |
**403** | The access token used to access resource is wrong |  -  |
**404** | user could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_email_send**
> users_email_send(user_id)

This endpoint will be used when you want to send a magic login link to specified user

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import auth_api
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
    api_instance = auth_api.AuthApi(api_client)
    user_id = "userId_example" # str | Id of the user you want to send magic link to

    # example passing only required values which don't have defaults set
    try:
        # This endpoint will be used when you want to send a magic login link to specified user
        api_instance.users_email_send(user_id)
    except lagrello_client.ApiException as e:
        print("Exception when calling AuthApi->users_email_send: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user you want to send magic link to |

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
**204** | Email to user has been sent successfully. |  -  |
**400** | The payload of the request is not valid |  -  |
**403** | The access token used to access resource is wrong |  -  |
**404** | user could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_totp_auth**
> User users_totp_auth(user_id, payload)

Verify users TOTP token

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import auth_api
from lagrello_client.model.user import User
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
    api_instance = auth_api.AuthApi(api_client)
    user_id = "userId_example" # str | Id of the user you want to verify TOTP code for
    payload = "payload_example" # str | The totp token the user sent

    # example passing only required values which don't have defaults set
    try:
        # Verify users TOTP token
        api_response = api_instance.users_totp_auth(user_id, payload)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling AuthApi->users_totp_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user you want to verify TOTP code for |
 **payload** | **str**| The totp token the user sent |

### Return type

[**User**](User.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - Returns the user information if the totp token is correct |  -  |
**401** | End users token is wrong, DO NOT authenticate user |  -  |
**403** | The access token used to access resource is wrong |  -  |
**404** | user could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_totp_toggle**
> TotpEnableResponse users_totp_toggle(user_id)

Enables or disables Time-based One-Time Password authentication method for specified user

When you want your users to be able to use TOTP authentication you need to send enable set to true as payload to this endpoint. To turn off TOTP set enable to false. When enabling you will recieve the secret key and a QR code link. The QR code you need to show your user for them to scan.

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import auth_api
from lagrello_client.model.totp_enable_response import TotpEnableResponse
from lagrello_client.model.error import Error
from lagrello_client.model.totp_enable_request import TotpEnableRequest
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
    api_instance = auth_api.AuthApi(api_client)
    user_id = "userId_example" # str | Id of the user you want to enable TOTP for
    totp_enable_request = TotpEnableRequest(
        enable=True,
    ) # TotpEnableRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Enables or disables Time-based One-Time Password authentication method for specified user
        api_response = api_instance.users_totp_toggle(user_id)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling AuthApi->users_totp_toggle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enables or disables Time-based One-Time Password authentication method for specified user
        api_response = api_instance.users_totp_toggle(user_id, totp_enable_request=totp_enable_request)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling AuthApi->users_totp_toggle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user you want to enable TOTP for |
 **totp_enable_request** | [**TotpEnableRequest**](TotpEnableRequest.md)|  | [optional]

### Return type

[**TotpEnableResponse**](TotpEnableResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Will return user&#39;s secret key and a url where QR-code image can be found |  -  |
**204** | Success when disabling TOTP for user |  -  |
**403** | The access token used to access resource is wrong |  -  |
**404** | user could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

