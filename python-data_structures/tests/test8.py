import unittest
import importlib
import sys
import os

from parent_test import ParentTest

filename = "8-multiple_returns.py"


class TestTask8(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("8-multiple_returns")
        sentence = "test"
        expected = (4, 't')

        result = module.multiple_returns(sentence)

        self.assertEqual(result, expected)

    def test_return_value2(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("8-multiple_returns")
        sentence = ""
        expected = (0, None)

        result = module.multiple_returns(sentence)

        self.assertEqual(result, expected)

    def test_script_output(self):
        """ Testing without index should return original list. """

        expected_output = "Length: 22 - First character: A"
        self.script_output_expected("8-main.py", expected_output)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
