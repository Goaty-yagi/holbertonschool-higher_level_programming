import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "10-divisible_by_2.py"


class TestTask10(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("10-divisible_by_2")
        list = [900, 43, 3, 2]
        expected = [True, False, False, True]

        result = module.divisible_by_2(list)

        self.assertEqual(result, expected)

    def test_return_value2(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("9-max_integer")
        list = []
        expected = None

        result = module.max_integer(list)

        self.assertEqual(result, expected)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def max_not_in_use(self):
        method = "max"
        self.method_not_in_use(filename, method)


if __name__ == "__main__":
    unittest.main()
