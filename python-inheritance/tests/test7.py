import unittest
import importlib
import os
import sys

from parent_test import ParentTest

filename = "7-base_geometry.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask7(ParentTest):
    module = "7-base_geometry"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """
        module = importlib.import_module(TestTask7
                                         .module)

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        module = importlib.import_module(TestTask7
                                         .module)

        self.assertTrue(module.BaseGeometry.__doc__)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_type_error(self):
        module = importlib.import_module(TestTask7
                                         .module)
        instance = module.BaseGeometry()
        error_type = TypeError

        with self.assertRaises(error_type):
            instance.integer_validator("name", "value")

    def test_value_error(self):
        module = importlib.import_module(TestTask7
                                         .module)
        instance = module.BaseGeometry()
        error_type = ValueError

        with self.assertRaises(error_type):
            instance.integer_validator("name", 0)




if __name__ == "__main__":
    unittest.main()
