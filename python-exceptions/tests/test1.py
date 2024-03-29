import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "1-safe_print_integer.py"
module = "1-main.py"


class TestTask1(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("1-safe_print_integer")
        value = 2000
        expected = True

        result = module.safe_print_integer(value)

        self.assertEqual(result, expected)

    def test_return_value2(self):
        """ Testing value is not int. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("1-safe_print_integer")
        value = "jio"
        expected = False

        result = module.safe_print_integer(value)

        self.assertEqual(result, expected)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_try_in_use(self):
        target_construct = "try"
        self.construct_not_in_use(filename, target_construct)

    def test_except_in_use(self):
        target_construct = "except"
        self.construct_not_in_use(filename, target_construct)
    
    def test_type_not_used(self):
        target_construct = "type"
        self.function_not_used(filename, target_construct)

    def test_specifier_used(self):
        """Not working"""
        specifier = ":d"
        self.format_with_specifier_used(filename, specifier)
        

if __name__ == "__main__":
    unittest.main()
