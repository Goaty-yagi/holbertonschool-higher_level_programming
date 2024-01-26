import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "11-delete_at.py"


class TestTask11(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("11-delete_at")
        list = [900, 43, 3, 2]
        index = 2
        expected = [900, 43, 2]

        result = module.delete_at(list, index)

        self.assertEqual(result, expected)

    def test_return_value2(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("11-delete_at")
        list = [900, 43, 3, 2]
        index = 90
        expected = [900, 43, 3, 2]

        result = module.delete_at(list, index)

        self.assertEqual(result, expected)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def pop_not_in_use(self):
        method = "pop"
        self.method_not_in_use(filename, method)


if __name__ == "__main__":
    unittest.main()
