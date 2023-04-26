#!/usr/bin/env python3
"""Test utils module."""

import unittest
from unittest import mock
from unittest.mock import patch
from typing import Dict
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
import requests


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""

    #def test_access_nested_map(self):
    #    """Test access_nested_map function."""
    #    nested_map = {"a": {"b": {"c": 1}}}
    #    path = ["a", "b", "c"]
    #    self.assertEqual(access_nested_map(nested_map, path), 1)

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map function."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json function."""
        # mock the get_json function to return test_payload
        # when called with test_url
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test memoize decorator."""

    def test_memoize(self):
        """Test memoize decorator."""
        class TestClass:
            """Test class."""

            def a_method(self):
                """A method."""
                return 42

            @memoize
            def a_property(self):
                """A property."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test = TestClass()
            test.a_property
            test.a_property
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
