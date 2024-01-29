import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "3-safe_print_division.py"
module = "3-main.py"


class TestTask3(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("3-safe_print_division")
        a = 50
        b = 0
        expected = None

        result = module.safe_print_division(a, b)

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

    def test_fainally_in_use(self):
        target_construct = "finally"
        self.construct_not_in_use(filename, target_construct)
    
    def test_format_used(self):
        target_construct = "format"
        self.method_in_use(filename, target_construct)
        

if __name__ == "__main__":
    unittest.main()
