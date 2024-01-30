import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "5-raise_exception.py"
module = "5-main.py"


class TestTask5(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_error_handle(self):
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("5-raise_exception")
        error_type = TypeError
        with self.assertRaises(error_type):
            module.raise_exception()


    
        

if __name__ == "__main__":
    unittest.main()
