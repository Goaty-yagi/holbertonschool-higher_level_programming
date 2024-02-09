import unittest
import importlib
import sys
import os
from io import StringIO

from parent_test import ParentTest

filename = "11-student.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask11(ParentTest):
    module = "11-student"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        module = importlib.import_module(TestTask11.module)

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        """ Testing func doc exists. """

        module = importlib.import_module(TestTask11.module)

        self.assertTrue(module.Student.__doc__)

    def test_reload_from_json_method(self):
        module = importlib.import_module(TestTask11.module)
        instance = module.Student("test", "last_test", 99)

        my_dict = {"first_name": "te", "last_name": "st", "age": 80}
        instance.reload_from_json(my_dict)
        actual_value = instance.age
        exected = 80
        self.assertEqual(actual_value, exected)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
