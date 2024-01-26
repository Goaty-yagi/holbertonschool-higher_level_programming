import unittest

from parent_test import ParentTest



filename = "3-infinite_add.py"


class TestTask3(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)


    def test_imported_script(self):
        module = "3-infinite_add"
        path = self.path
        self.imported_script(module, path)

    def test_count_star(self):
        """ Testing if import * is used in the file. """

        target_construct = "import *"
        self.construct_in_use(filename, target_construct)

    def test_format_in_use(self):
        """ Testing the format method is used in the file. """

        method_name = "format"
        self.method_in_use(filename, method_name)

    def test_script_output(self):
        """ Testing a specific file output is expected. """
        
        args = ["79", "10",  "-40", "-300", "89"]
        expected_output = "-162"
        self.script_output_expected(filename, expected_output, args)

    def test_no_arg(self):
        """ Testing a specific file output without arg. """

        expected_output = "0"
        self.script_output_expected(filename, expected_output)

    def test_one_arg(self):
        """ Testing a specific file output with 1 arg. """

        args = ["9"]
        expected_output = "9"
        self.script_output_expected(filename, expected_output, args)


if __name__ == "__main__":
    unittest.main()
