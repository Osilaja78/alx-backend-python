#!/usr/bin/env python3
"""test_utils.py module"""

import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Unit test for utils.access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected_result: Union[Dict, int]
    ) -> None:
        """test for correct output"""

        self.assertEqual(access_nested_map(nested_map, path), expected_result)
