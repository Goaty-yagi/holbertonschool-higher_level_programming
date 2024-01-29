import unittest
import sys
import importlib
import os

from parent_test import ParentTest

filename = "3-common_elements.py"
module = "3-main.py"


class TestTask3(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_script_output(self):
        """ Testing a line in the file is modified and output is expected. """

        expected_output = "['C']"

        self.script_output_expected(module, expected_output)

    def test_return_value(self):
        """ Testing a return value is expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("3-common_elements")
        set_1 = {"a", "b", "ko"}
        set_2 = {"c", "ko", "KO"}
        expected = {"ko"}

        result = module.common_elements(set_1, set_2)

        self.assertEqual(result, expected)

    def test_count_import(self):
        """ Testing if import is not used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
