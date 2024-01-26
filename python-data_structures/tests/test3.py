import unittest, importlib

from parent_test import ParentTest

filename = "3-print_reversed_list_integer.py"
module = "3-main.py"

class TestTask3(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing a line in the file is modified and output is expected. """

        line = 'my_list = [1, 4, 5, 8, 9]\n'
        line_num = 4
        expected = "9\n8\n5\n4\n1" 
        
        self.replace_line_test(module, expected, line, line_num)

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
