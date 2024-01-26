import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "7-add_tuple.py"


class TestTask7(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("7-add_tuple")
        tuple_a = (20, 50, 100)
        tuple_b = (100,)
        expected = (120, 50)

        result = module.add_tuple(tuple_a, tuple_b)

        self.assertEqual(result, expected)

    def test_return_value2(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("7-add_tuple")
        tuple_a = ()
        tuple_b = (100,)
        expected = (100, 0)

        result = module.add_tuple(tuple_a, tuple_b)

        self.assertEqual(result, expected)

    def test_script_output(self):
        """ Testing without index should return original list. """

        expected_output = "(89, 100)\n(2, 89)\n(1, 89)"
        self.script_output_expected("7-main.py", expected_output)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
