"""
    Lagrello API

    API specification for Lagrello, a simple to use authentication service  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lagrello.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import lagrello_client
from lagrello_client.api.tokens_api import TokensApi  # noqa: E501


class TestTokensApi(unittest.TestCase):
    """TokensApi unit test stubs"""

    def setUp(self):
        self.api = TokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tokens_create(self):
        """Test case for tokens_create

        Creates new token  # noqa: E501
        """
        pass

    def test_tokens_delete(self):
        """Test case for tokens_delete

        Deletes specifed access token  # noqa: E501
        """
        pass

    def test_tokens_list(self):
        """Test case for tokens_list

        Returns a list of all active tokens in tenant  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
