import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "1-square.py"
module = "1-main.py"


class TestTask1(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_obj_has_attr(self):
        """ Testing class doc exists. """
        
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("1-square")
        instance = module.Square(90)
        expected = "_Square__size"

        self.assertTrue(getattr(instance, expected))

    def test_module_doc(self):
        """ Testing module doc exists. """

        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("1-square")

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        """ Testing class doc exists. """
        
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("1-square")

        self.assertTrue(module.Square.__doc__)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)
        

if __name__ == "__main__":
    unittest.main()
