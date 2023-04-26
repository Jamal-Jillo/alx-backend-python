#!/usr/bin/env python3
"""Unit tests for the client.py"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class."""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_json):
        """Test that GithubOrgClient.org returns the correct value."""

        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_json.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name))


if __name__ == '__main__':
    unittest.main()
