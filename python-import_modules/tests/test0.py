import unittest

from parent_test import ParentTest

filename = "0-add.py"

class TestTask0(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing a specific file output is expected. """

        expected_output = "1 + 2 = 3"
        self.script_output_expected(filename, expected_output)

    def test_imported_script(self):
        module = "0-add"
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

if __name__ == "__main__":
    unittest.main()
