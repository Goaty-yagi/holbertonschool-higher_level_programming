import unittest
import sys
import importlib
import os

from parent_test import ParentTest

filename = "10-best_score.py"
module = "10-main.py"


class TestTask10(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_return_value(self):
        """ Testing a case, update. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))

        module = importlib.import_module("10-best_score")
        set_1 = {"1": 40, "2": 5, "3": 32}
        expected = "1"

        result = module.best_score(set_1)

        self.assertEqual(result, expected)

    def test_count_import(self):
        """ Testing if import is not used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
