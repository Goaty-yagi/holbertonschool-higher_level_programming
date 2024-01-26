import unittest

from parent_test import ParentTest

filename = "4-hidden_discovery.py"
module_name = "4-hidden_discovery"


class TestTask4(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_imported_script(self):
        module = module_name
        path = self.path
        self.imported_script(module, path)

    def test_count_star(self):
        """ Testing if import * is used in the file. """

        target_construct = "import *"
        self.construct_in_use(filename, target_construct)

    def test_script_output(self):
        """ Testing a specific file output is expected. """

        expected_output = "my_secret_santa\nprint_hidden\nprint_school"
        self.script_output_expected(filename, expected_output)

    def test_script_output2(self):
        """ Testing a line in the file is modified and output is expected. """
        
        line = "    with open('hidden_4_bis.pyc', 'rb') as f:\n"
        line_num = 6
        expected_output = "my_secret_santa\nprint_hidden\nprint_school\ntest_betty"
        self.replace_line_test(filename, expected_output, line, line_num)

    def test_script_output3(self):
        """ Testing a line in the file is modified and output is expected. """
        
        line = "    with open('hidden_4_empty.pyc', 'rb') as f:\n"
        line_num = 6
        expected_output = ""
        self.replace_line_test(filename, expected_output, line, line_num)


if __name__ == "__main__":
    unittest.main()
