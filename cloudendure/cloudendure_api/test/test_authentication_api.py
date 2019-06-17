# coding: utf-8
from __future__ import absolute_import

import unittest

from cloudendure import cloudendure_api
from cloudendure.cloudendure_api.rest import ApiException

from ..api.authentication_api import AuthenticationApi  # noqa: E501


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login_post(self):
        """Test case for login_post

        Login  # noqa: E501
        """
        pass

    def test_logout_post(self):
        """Test case for logout_post

        Logout  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
