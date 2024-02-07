import unittest
import importlib
import os
import sys

from parent_test import ParentTest

filename = "8-rectangle.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask8(ParentTest):
    module = "8-rectangle"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """
        module = importlib.import_module(TestTask8
                                         .module)

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        module = importlib.import_module(TestTask8
                                         .module)

        self.assertTrue(module.Rectangle.__doc__)


if __name__ == "__main__":
    unittest.main()
