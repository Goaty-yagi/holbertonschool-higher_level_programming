import unittest
import importlib
import sys
import os
from io import StringIO

from parent_test import ParentTest

filename = "5-save_to_json_file.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask5(ParentTest):
    module = "5-save_to_json_file"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        module = importlib.import_module(TestTask5.module)

        self.assertTrue(module.__doc__)

    def test_func_doc(self):
        """ Testing func doc exists. """

        module = importlib.import_module(TestTask5.module)

        self.assertTrue(module.save_to_json_file.__doc__)


if __name__ == "__main__":
    unittest.main()
