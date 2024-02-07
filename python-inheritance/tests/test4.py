import unittest
import importlib
import os
import sys

from parent_test import ParentTest

filename = "4-inherits_from.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask4(ParentTest):
    module = "4-inherits_from"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """
        module = importlib.import_module(TestTask4
                                         .module)

        self.assertTrue(module.__doc__)

    def test_func_doc(self):
        module = importlib.import_module(TestTask4
                                         .module)

        self.assertTrue(module.inherits_from.__doc__)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
