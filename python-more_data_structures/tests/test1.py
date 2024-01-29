import unittest, importlib

from parent_test import ParentTest

filename = "1-search_replace.py"
module = "1-main.py"

class TestTask1(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing a line in the file is modified and output is expected. """

        expected_output = "[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]\n[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]" 
        
        self.script_output_expected(module, expected_output)

    def test_count_import(self):
        """ Testing if import is not used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)
        

if __name__ == "__main__":
    unittest.main()
