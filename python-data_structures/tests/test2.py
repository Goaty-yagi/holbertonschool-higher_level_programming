import unittest, importlib, sys, os

from parent_test import ParentTest

filename = "2-replace_in_list.py"

class TestTask2(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("2-replace_in_list")
        list = [5,3,7,6,5]
        index = 4
        new_val = 90
        expected = [5,3,7,6,90]

        result = module.replace_in_list(list, index, new_val)
        
        self.assertEqual(result, expected)

    def test_script_output2(self):
        """ Testing with negative num should return original list. """

        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("2-replace_in_list")
        list = [5,3,7,6,5]
        index = -4
        new_val = 90
        expected = [5,3,7,6,5]

        result = module.replace_in_list(list, index, new_val)
        
        self.assertEqual(result, expected)

    def test_script_output2(self):
        """ Testing with out of index should return original list. """
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("2-replace_in_list")
        list = [5,3,7,6,5]
        index = 90
        new_val = 90
        expected = [5,3,7,6,5]

        result = module.replace_in_list(list, index, new_val)
        
        self.assertEqual(result, expected)

    def test_count_star(self):
        """ Testing if import is used in the file. """
        
        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_count_try_except(self):
        """ Testing if try and except is used in the file. """

        target_construct = "try"
        self.construct_in_use(filename, target_construct)

        target_construct = "except"
        self.construct_in_use(filename, target_construct)

        

if __name__ == "__main__":
    unittest.main()
