import unittest

from parent_test import ParentTest

filename = "12-switch.py"


class TestTask12(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing script output is expected. """

        expected_output = "a=10 - b=89"
        self.script_output_expected(filename, expected_output)

    def test_line_count(self):
        """ Testing a line num is expected. """
        expected_line_num = 5
        self.line_count(filename, expected_line_num)


if __name__ == "__main__":
    unittest.main()
