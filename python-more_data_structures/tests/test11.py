import unittest
import sys
import importlib
import os

from parent_test import ParentTest

filename = "11-multiply_list_map.py"
module = "11-main.py"


class TestTask11(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return val as expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("11-multiply_list_map")
        list = [4, 6, 9, 10]
        number = 9
        expected = [36, 54, 81, 90]

        result = module.multiply_list_map(list, number)

        self.assertEqual(result, expected)

    def test_return_value2(self):
        """ Testing a return val is none. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("11-multiply_list_map")
        list = [4, 6, 9, 10]
        expected = [0, 0, 0, 0]

        result = module.multiply_list_map(list)

        self.assertEqual(result, expected)

    def test_count_import(self):
        """ Testing if import is not used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_line_count(self):
        expected_line = 3

        self.line_count(filename, expected_line)

if __name__ == "__main__":
    unittest.main()
