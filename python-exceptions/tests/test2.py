import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "2-safe_print_list_integers.py"
module = "2-main.py"


class TestTask2(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("2-safe_print_list_integers")
        list = [1, 2, 3, "School", 4, 5, [1, 2, 3], 90, "o", None]
        expected = 6

        result = module.safe_print_list_integers(list, 9)

        self.assertEqual(result, expected)
    
    def test_error_handle(self):
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        list = [1, 2, 3, "School", 4, 5, [1, 2, 3], 90, "o", None]
        module = importlib.import_module("2-safe_print_list_integers")
        error_type = IndexError
        with self.assertRaises(error_type):
            module.safe_print_list_integers(list, 90)

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
