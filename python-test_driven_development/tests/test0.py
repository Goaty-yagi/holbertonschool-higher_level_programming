import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "0-add_integer.py"
module = "0-main.py"


class TestTask0(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("0-add_integer")

        self.assertTrue(module.__doc__)

    def test_func_doc(self):
        """ Testing class doc exists. """
        
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("0-add_integer")

        self.assertTrue(module.add_integer.__doc__)
        

if __name__ == "__main__":
    unittest.main()
