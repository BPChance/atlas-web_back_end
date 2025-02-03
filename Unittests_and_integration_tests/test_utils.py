#!/usr/bin/env python3
""" utils.py testing """


import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ test for access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test that result is as expected """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ test access nested map with exception """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected)


class TestGetJson(unittest.TestCase):
    """ test that it returns expected results """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ test get_json """
        # create mock response
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        # assertions
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test that when calling a_property twice, the correct result is
    returned but a_method is only called once using assert_called_once
    """
    def test_memoize(self):
        # test class inside test method
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # mocking
        with patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            obj = TestClass()
            # calls method
            self.assertEqual(obj.a_property, 42)
            # use cached result
            self.assertEqual(obj.a_property, 42)
            # make sure it only calls once
            mock_a_method.assert_called_once()
