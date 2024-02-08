import unittest
import importlib
import sys
import os
from io import StringIO

from parent_test import ParentTest

filename = "7-add_item.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask7(ParentTest):
    module = "7-add_item"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        module = importlib.import_module(TestTask7.module)

        self.assertTrue(module.__doc__)


if __name__ == "__main__":
    unittest.main()
