import unittest

from parent_test import ParentTest

filename = "5-variable_load.py"
module_name = "5-variable_load"


class TestTask5(ParentTest):
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
        
        expected_output = "98"
        self.script_output_expected(filename, expected_output)

    def test_script_output2(self):
        """ Testing a line in the file is modified and output is expected. """

        line = 'a = 2999\n'
        line_num = 2
        expected = "2999"
        
        self.replace_line_test(filename, expected, line, line_num)



if __name__ == "__main__":
    unittest.main()
