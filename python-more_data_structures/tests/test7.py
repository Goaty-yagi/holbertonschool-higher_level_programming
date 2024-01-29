import unittest
import sys
import importlib
import os

from parent_test import ParentTest

filename = "7-update_dictionary.py"
module = "7-main.py"


class TestTask7(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a case, update. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("7-update_dictionary")
        set_1 = {"1": "a", "2": "b", "3": "ko"}
        key = "1"
        val = "A"
        expected = {"1": "A", "2": "b", "3": "ko"}

        result = module.update_dictionary(set_1, key, val)

        self.assertEqual(result, expected)

    def test_return_value2(self):
        """ Testing a case, new pair. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("7-update_dictionary")
        set_1 = {"1": "a", "2": "b", "3": "ko"}
        key = "4"
        val = "P"
        expected = {"1": "a", "2": "b", "3": "ko", "4": "P"}

        result = module.update_dictionary(set_1, key, val)

        self.assertEqual(result, expected)

    def test_count_import(self):
        """ Testing if import is not used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
