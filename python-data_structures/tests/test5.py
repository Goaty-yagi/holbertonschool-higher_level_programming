import unittest, importlib, sys, os

from parent_test import ParentTest

filename = "5-no_c.py"

class TestTask5(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("5-no_c")
        string = "abcdABCD"
        expected = "abdABD"

        result = module.no_c(string)
        
        self.assertEqual(result, expected)


    def test_script_output(self):
        """ Testing without index should return original list. """

        expected_output = "Best Shool\nhiago\n is fun!"
        self.script_output_expected("5-main.py", expected_output)

    def test_count_import(self):
        """ Testing if import is used in the file. """
        
        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_count_try_except(self):
        """ Testing if try and except is used in the file. """

        target_construct = "try"
        self.construct_in_use(filename, target_construct)

        target_construct = "except"
        self.construct_in_use(filename, target_construct)
    
    def test_replace_not_in_use(self):
        method = "replace"
        self.method_not_in_use(filename, method)

        

if __name__ == "__main__":
    unittest.main()
