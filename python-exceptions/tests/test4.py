import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "4-list_division.py"
module = "4-main.py"


class TestTask4(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("4-list_division")
        list_1 = [20,"h", 80, 0.5]
        list_2 = ["h", 3, "2", 2, "ko", None]
        length = 10
        expected = [0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0]

        result = module.list_division(list_1, list_2, length)

        self.assertEqual(result, expected)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_try_in_use(self):
        target_construct = "try"
        self.construct_not_in_use(filename, target_construct)

    def test_except_in_use(self):
        target_construct = "except"
        self.construct_not_in_use(filename, target_construct)

    def test_fainally_in_use(self):
        target_construct = "finally"
        self.construct_not_in_use(filename, target_construct)
        

if __name__ == "__main__":
    unittest.main()
