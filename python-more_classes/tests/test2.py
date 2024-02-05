import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "2-rectangle.py"
module = "2-main.py"

sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

class TestTask2(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("1-rectangle")

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        """ Testing class doc exists. """

        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("2-rectangle")

        self.assertTrue(module.Rectangle.__doc__)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_area(self):

        module = importlib.import_module("2-rectangle")
        instance = module.Rectangle(10, 20)
        return_value = instance.area()
        expected_area = 200

        self.assertEqual(return_value, expected_area)

    def test_area_with_zero(self):

        module = importlib.import_module("2-rectangle")
        instance = module.Rectangle(20)
        return_value = instance.area()
        expected_area = 0

        self.assertEqual(return_value, expected_area)

    def test_perimeter(self):

        module = importlib.import_module("2-rectangle")
        instance = module.Rectangle(10, 20)
        return_value = instance.perimeter()
        expected_area = 60

        self.assertEqual(return_value, expected_area)

    def test_perimeter_with_zero(self):

        module = importlib.import_module("2-rectangle")
        instance = module.Rectangle()
        return_value = instance.perimeter()
        expected_area = 0

        self.assertEqual(return_value, expected_area)


if __name__ == "__main__":
    unittest.main()
