import unittest

from parent_test import ParentTest

filename = "1-calculation.py"


class TestTask1(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing a specific file output is expected. """

        expected_output = "10 + 5 = 15\n10 - 5 = 5\n10 * 5 = 50\n10 / 5 = 2"
        self.script_output_expected(filename, expected_output)

    def test_imported_script(self):
        module = "1-calculation"
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
