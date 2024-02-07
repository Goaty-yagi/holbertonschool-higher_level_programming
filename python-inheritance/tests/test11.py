import unittest
import importlib
import os
import sys

from parent_test import ParentTest

filename = "11-square.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask11(ParentTest):
    module = "11-square"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """
        module = importlib.import_module(TestTask11
                                         .module)

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        module = importlib.import_module(TestTask11
                                         .module)

        self.assertTrue(module.Square.__doc__)

    def test_print_instance(self):
        module = importlib.import_module(TestTask11
                                         .module)
        instance = module.Square(6)
        actual_value = instance.__str__()
        expected_value = "[Square] 6/6"

        self.assertEqual(actual_value, expected_value)


if __name__ == "__main__":
    unittest.main()
