# lagrello_client.UsersApi

All URIs are relative to *https://api.lagrello.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create**](UsersApi.md#users_create) | **POST** /v1/users | Creates a user in tenant, tenant is determined from the token
[**users_delete**](UsersApi.md#users_delete) | **DELETE** /v1/users/{userId} | Deletes specified user
[**users_get**](UsersApi.md#users_get) | **GET** /v1/users/{userId} | Returns specified user
[**users_update**](UsersApi.md#users_update) | **PATCH** /v1/users/{userId} | Updates specified user


# **users_create**
> User users_create()

Creates a user in tenant, tenant is determined from the token

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import users_api
from lagrello_client.model.user import User
from lagrello_client.model.create_user_request import CreateUserRequest
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
    api_instance = users_api.UsersApi(api_client)
    create_user_request = CreateUserRequest(
        email="email_example",
        user_id="user_id_example",
    ) # CreateUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a user in tenant, tenant is determined from the token
        api_response = api_instance.users_create(create_user_request=create_user_request)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling UsersApi->users_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)|  | [optional]

### Return type

[**User**](User.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new user |  -  |
**403** | The access token used to access resource is wrong |  -  |
**409** | Returned when user already exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete**
> users_delete(user_id)

Deletes specified user

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | Id of the user you want to delete

    # example passing only required values which don't have defaults set
    try:
        # Deletes specified user
        api_instance.users_delete(user_id)
    except lagrello_client.ApiException as e:
        print("Exception when calling UsersApi->users_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user you want to delete |

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
**204** | Successfully deleted specified user |  -  |
**403** | The access token used to access resource is wrong |  -  |
**404** | user could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> User users_get(user_id)

Returns specified user

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | userId of user you want to fetch information about

    # example passing only required values which don't have defaults set
    try:
        # Returns specified user
        api_response = api_instance.users_get(user_id)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling UsersApi->users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId of user you want to fetch information about |

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
**200** | Returns user data for specified user |  -  |
**403** | The access token used to access resource is wrong |  -  |
**404** | user could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update**
> User users_update(user_id)

Updates specified user

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import users_api
from lagrello_client.model.update_user_request import UpdateUserRequest
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | Id of the user you want to update
    update_user_request = UpdateUserRequest(
        email="email_example",
    ) # UpdateUserRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates specified user
        api_response = api_instance.users_update(user_id)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling UsersApi->users_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates specified user
        api_response = api_instance.users_update(user_id, update_user_request=update_user_request)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling UsersApi->users_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Id of the user you want to update |
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | [optional]

### Return type

[**User**](User.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated specified user |  -  |
**403** | The access token used to access resource is wrong |  -  |
**404** | user could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

