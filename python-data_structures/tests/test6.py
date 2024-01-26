import unittest, importlib

from parent_test import ParentTest

filename = "6-print_matrix_integer.py"
module = "6-main.py"

class TestTask6(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing without index should return original list. """

        expected_output = "1 2 3\n4 5 6\n7 8 9\n--"
        self.script_output_expected("6-main.py", expected_output)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_format_in_use(self):
        """ Testing the format method is used with :d in the file. """

        method_name = "format"
        self.method_in_use(filename, method_name)
        

if __name__ == "__main__":
    unittest.main()
