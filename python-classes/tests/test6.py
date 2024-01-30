import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "6-square.py"
module = "6-main.py"


class TestTask6(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    # def test_method_output(self):
    #     """ Testing a method print is expected """

    #     sys.path.append(os.path.abspath(
    #         os.path.join(os.path.dirname(__file__), "..")))

    #     module = importlib.import_module("5-square")
    #     instance = module.Square(2)
    #     result = instance.area()
    #     expected = 2500
    #     expected_output = "##\n##" 
        
    #     self.script_output_expected(module, expected_output)
    
    # I will figure it out later

    def test_module_doc(self):
        """ Testing module doc exists. """

        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("6-square")

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        """ Testing class doc exists. """

        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("6-square")

        self.assertTrue(module.Square.__doc__)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
