# lagrello_client.TenantsApi

All URIs are relative to *https://api.lagrello.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenant_update**](TenantsApi.md#tenant_update) | **PATCH** /v1/tenant | Updates tenant information
[**tenants_activate**](TenantsApi.md#tenants_activate) | **POST** /v1/tenant/activate | Activates the tenant, checks that all necessary information to activate a tenant is included
[**tenants_create**](TenantsApi.md#tenants_create) | **POST** /v1/tenant | Creates new tenant
[**tenants_create_0**](TenantsApi.md#tenants_create_0) | **DELETE** /v1/tenant | Deletes tenant caller is part of, will send verification email before deleting tenant
[**tenants_get**](TenantsApi.md#tenants_get) | **GET** /v1/tenant | Returns the tenant information the caller is part of


# **tenant_update**
> Tenant tenant_update()

Updates tenant information

This endpoint is used to update certain information about your tenant. For example if you want to update your tenant's callback URL you will do that here.

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import tenants_api
from lagrello_client.model.tenant import Tenant
from lagrello_client.model.update_tenant_request import UpdateTenantRequest
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
    api_instance = tenants_api.TenantsApi(api_client)
    update_tenant_request = UpdateTenantRequest(
        callback_url="https://api.example.com/users/login/{}",
    ) # UpdateTenantRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates tenant information
        api_response = api_instance.tenant_update(update_tenant_request=update_tenant_request)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling TenantsApi->tenant_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tenant_request** | [**UpdateTenantRequest**](UpdateTenantRequest.md)|  | [optional]

### Return type

[**Tenant**](Tenant.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated tenant |  -  |
**403** | The access token used to access resource is wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_activate**
> Tenant tenants_activate()

Activates the tenant, checks that all necessary information to activate a tenant is included

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import tenants_api
from lagrello_client.model.tenant import Tenant
from lagrello_client.model.activate_tenant_request import ActivateTenantRequest
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
    api_instance = tenants_api.TenantsApi(api_client)
    activate_tenant_request = ActivateTenantRequest(
        company_name="company_name_example",
        company_address="company_address_example",
        company_city="company_city_example",
        company_postal_code="company_postal_code_example",
        company_country="company_country_example",
        company_org_number="company_org_number_example",
        company_vat_number="company_vat_number_example",
    ) # ActivateTenantRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Activates the tenant, checks that all necessary information to activate a tenant is included
        api_response = api_instance.tenants_activate(activate_tenant_request=activate_tenant_request)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling TenantsApi->tenants_activate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_tenant_request** | [**ActivateTenantRequest**](ActivateTenantRequest.md)|  | [optional]

### Return type

[**Tenant**](Tenant.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns tenant information about the newly activated tenant. |  -  |
**400** | The payload of the request is not valid |  -  |
**403** | The access token used to access resource is wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_create**
> Tenant tenants_create()

Creates new tenant

### Example

```python
import time
import lagrello_client
from lagrello_client.api import tenants_api
from lagrello_client.model.tenant import Tenant
from lagrello_client.model.create_tenant_request import CreateTenantRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.lagrello.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lagrello_client.Configuration(
    host = "https://api.lagrello.com"
)


# Enter a context with an instance of the API client
with lagrello_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tenants_api.TenantsApi(api_client)
    create_tenant_request = CreateTenantRequest(
        tenant_name="Example Company",
        admin_email="admin@example.com",
    ) # CreateTenantRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates new tenant
        api_response = api_instance.tenants_create(create_tenant_request=create_tenant_request)
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling TenantsApi->tenants_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_request** | [**CreateTenantRequest**](CreateTenantRequest.md)|  | [optional]

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns information about the newly created tenant |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_create_0**
> Tenant tenants_create_0()

Deletes tenant caller is part of, will send verification email before deleting tenant

This endpoint will delete your tenant. Will send an email to the admin email address of the tenant confirming that you want to delete your tenant before deletion.

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import tenants_api
from lagrello_client.model.tenant import Tenant
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
    api_instance = tenants_api.TenantsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Deletes tenant caller is part of, will send verification email before deleting tenant
        api_response = api_instance.tenants_create_0()
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling TenantsApi->tenants_create_0: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Tenant**](Tenant.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Sucess, will send verification email before deleting |  -  |
**403** | The access token used to access resource is wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_get**
> Tenant tenants_get()

Returns the tenant information the caller is part of

### Example

* Bearer Authentication (token):
```python
import time
import lagrello_client
from lagrello_client.api import tenants_api
from lagrello_client.model.tenant import Tenant
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
    api_instance = tenants_api.TenantsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the tenant information the caller is part of
        api_response = api_instance.tenants_get()
        pprint(api_response)
    except lagrello_client.ApiException as e:
        print("Exception when calling TenantsApi->tenants_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Tenant**](Tenant.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gives back the tenant call is part of |  -  |
**403** | The access token used to access resource is wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

