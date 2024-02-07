import unittest
import importlib
import os
import sys

from parent_test import ParentTest

filename = "9-rectangle.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask9(ParentTest):
    module = "9-rectangle"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """
        module = importlib.import_module(TestTask9
                                         .module)

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        module = importlib.import_module(TestTask9
                                         .module)

        self.assertTrue(module.Rectangle.__doc__)

    def test_type_error(self):
        module = importlib.import_module(TestTask9
                                         .module)
        instance = module.Rectangle(5, 6)
        actual_value = instance.area()
        expected_value = 30

        self.assertEqual(actual_value, expected_value)


if __name__ == "__main__":
    unittest.main()
