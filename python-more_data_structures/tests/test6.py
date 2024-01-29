import unittest

from parent_test import ParentTest

filename = "6-print_sorted_dictionary.py"
module = "6-main.py"


class TestTask6(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing a line in the file is modified and output is expected. """

        expected_output = "Number: 89\nids: [1, 2, 3]\nlanguage: C\ntrack: Low level"

        self.script_output_expected(module, expected_output)

    def test_count_import(self):
        """ Testing if import is not used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
