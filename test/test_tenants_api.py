"""
    Lagrello API

    API specification for Lagrello, a simple to use authentication service  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lagrello.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import lagrello_client
from lagrello_client.api.tenants_api import TenantsApi  # noqa: E501


class TestTenantsApi(unittest.TestCase):
    """TenantsApi unit test stubs"""

    def setUp(self):
        self.api = TenantsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tenant_update(self):
        """Test case for tenant_update

        Updates tenant information  # noqa: E501
        """
        pass

    def test_tenants_activate(self):
        """Test case for tenants_activate

        Activates the tenant, checks that all necessary information to activate a tenant is included  # noqa: E501
        """
        pass

    def test_tenants_create(self):
        """Test case for tenants_create

        Creates new tenant  # noqa: E501
        """
        pass

    def test_tenants_create_0(self):
        """Test case for tenants_create_0

        Deletes tenant caller is part of, will send verification email before deleting tenant  # noqa: E501
        """
        pass

    def test_tenants_get(self):
        """Test case for tenants_get

        Returns the tenant information the caller is part of  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()