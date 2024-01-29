import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "0-safe_print_list.py"
module = "0-main.py"


class TestTask0(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing a line in the file is modified and output is expected. """

        expected_output = "12\nnb_print: 2\n12345\nnb_print: 5\n12345\nnb_print: 5"

        self.script_output_expected(module, expected_output)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("0-safe_print_list")
        my_list = [2, 3, 45, "ko"]
        x = 90
        expected = 4

        result = module.safe_print_list(my_list, x)

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
    
    def test_len_not_used(self):
        target_construct = "len"
        self.function_not_used(filename, target_construct)
        

if __name__ == "__main__":
    unittest.main()
