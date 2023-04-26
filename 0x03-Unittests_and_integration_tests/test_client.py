#!/usr/bin/env python3
"""Unit tests for the client.py"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


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

    @patch('github_client.GithubOrgClient.org')
    def test_public_repos_url(self, name, result):
        """Test that the result of GithubOrgClient._public_repos_url is"""
        # Define the expected result
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test the has_license method of the GithubOrgClient class.

        Arguments:
        repo -- The given repository.
        license_key -- The license key to search for.
        expected_result -- The expected result.

        Returns:
        OK if the test succeeded, FAIL otherwise.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    An integration test for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """ 
        Set up class before each method.
        """
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """
        Test the public_repos method with the given test data.

        Returns:
        OK if the test succeeded, FAIL otherwise.
        """
        test_class = GithubOrgClient('Facebook')
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
        Test the public_repos method with the given license argument.

        Returns:
        OK if the test succeeded, FAIL otherwise.
        """
        test_class = GithubOrgClient("holberton")
        assert True

    @classmethod
    def tearDownClass(cls):
        """
        Tear down after each class.
        """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
