"""
    Lagrello API

    API specification for Lagrello, a simple to use authentication service  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lagrello.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import lagrello_client
from lagrello_client.model.tenant_company_info import TenantCompanyInfo
globals()['TenantCompanyInfo'] = TenantCompanyInfo
from lagrello_client.model.tenant import Tenant


class TestTenant(unittest.TestCase):
    """Tenant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTenant(self):
        """Test Tenant"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Tenant()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
