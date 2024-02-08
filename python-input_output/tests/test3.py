import unittest
import importlib
import sys
import os
from io import StringIO

from parent_test import ParentTest

filename = "3-to_json_string.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask3(ParentTest):
    module = "3-to_json_string"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        module = importlib.import_module(TestTask3.module)

        self.assertTrue(module.__doc__)

    def test_func_doc(self):
        """ Testing func doc exists. """

        module = importlib.import_module(TestTask3.module)

        self.assertTrue(module.to_json_string.__doc__)


if __name__ == "__main__":
    unittest.main()
