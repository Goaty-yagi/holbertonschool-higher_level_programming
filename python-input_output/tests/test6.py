import unittest
import importlib
import sys
import os
from io import StringIO

from parent_test import ParentTest

filename = "6-load_from_json_file.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask6(ParentTest):
    module = "6-load_from_json_file"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        module = importlib.import_module(TestTask6.module)

        self.assertTrue(module.__doc__)

    def test_func_doc(self):
        """ Testing func doc exists. """

        module = importlib.import_module(TestTask6.module)

        self.assertTrue(module.load_from_json_file.__doc__)


if __name__ == "__main__":
    unittest.main()
