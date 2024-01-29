import unittest
import sys
import importlib
import os

from parent_test import ParentTest

filename = "12-roman_to_int.py"
module = "12-main.py"


class TestTask12(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a return val as expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("12-roman_to_int")
        roman_number = "IV"
        expected = 4

        result = module.roman_to_int(roman_number)

        self.assertEqual(result, expected)

    def test_return_value2(self):
        """ Testing a roman_number order is weird. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("12-roman_to_int")
        roman_number = "XXDIV"
        expected = 524

        result = module.roman_to_int(roman_number)

        self.assertEqual(result, expected)

    def test_return_value3(self):
        """ Testing a roman_number is None. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("12-roman_to_int")
        roman_number = None
        expected = 0

        result = module.roman_to_int(roman_number)

        self.assertEqual(result, expected)

    def test_return_value4(self):
        """ Testing a roman_number is not string. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("12-roman_to_int")
        roman_number = 90
        expected = 0

        result = module.roman_to_int(roman_number)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
