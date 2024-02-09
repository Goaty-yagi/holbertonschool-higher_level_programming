import unittest
import importlib
import sys
import os
from io import StringIO

from parent_test import ParentTest

filename = "9-student.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask9(ParentTest):
    module = "9-student"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        module = importlib.import_module(TestTask9.module)

        self.assertTrue(module.__doc__)

    def test_class_doc(self):
        """ Testing func doc exists. """

        module = importlib.import_module(TestTask9.module)

        self.assertTrue(module.Student.__doc__)

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
