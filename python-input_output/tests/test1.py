import unittest
import importlib
import sys
import os
from io import StringIO

from parent_test import ParentTest

filename = "1-write_file.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask1(ParentTest):
    module = "1-write_file"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        module = importlib.import_module(TestTask1.module)

        self.assertTrue(module.__doc__)

    def test_func_doc(self):
        """ Testing func doc exists. """

        module = importlib.import_module(TestTask1.module)

        self.assertTrue(module.write_file.__doc__)

    def test_output(self):
        module = importlib.import_module(TestTask1.module)
        captured_output = StringIO()
        sys.stdout = captured_output

        filename = "my_first_file.txt"
        expected = "We offer a truly innovative approach to education:\nfocus\n"
        count = module.write_file(filename, expected)
        self.assertEqual(count, len(expected))

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_with_in_use(self):

        target_construct = "with"
        self.construct_not_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
