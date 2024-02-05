import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "8-rectangle.py"
module = "8-main.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask8(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("8-rectangle")

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        """ Testing class doc exists. """

        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("8-rectangle")

        self.assertTrue(module.Rectangle.__doc__)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_bigger_or_equal(self):

        module = importlib.import_module("8-rectangle")
        instance1 = module.Rectangle(2, 4)
        instance2 = module.Rectangle(6, 4)
        return_instance = instance2.bigger_or_equal(instance1, instance2)
        expected_instance = instance2

        self.assertEqual(return_instance, expected_instance)

    def test_bigger_or_equal_with_not_isntance1(self):

        module = importlib.import_module("8-rectangle")
        instance = module.Rectangle(2, 4)

        with self.assertRaises(TypeError):
            instance.bigger_or_equal(instance, 900)

    def test_bigger_or_equal_with_not_isntance2(self):

        module = importlib.import_module("8-rectangle")
        instance = module.Rectangle(2, 4)

        with self.assertRaises(TypeError):
            instance.bigger_or_equal(90, instance)


if __name__ == "__main__":
    unittest.main()
