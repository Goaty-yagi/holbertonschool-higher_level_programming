import unittest
import importlib
import sys
import os
from io import StringIO

from parent_test import ParentTest

filename = "2-append_write.py"

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


class TestTask2(ParentTest):
    module = "2-append_write"

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        module = importlib.import_module(TestTask2.module)

        self.assertTrue(module.__doc__)

    def test_func_doc(self):
        """ Testing func doc exists. """

        module = importlib.import_module(TestTask2.module)

        self.assertTrue(module.append_write.__doc__)

    def test_output(self):
        module = importlib.import_module(TestTask2.module)
        captured_output = StringIO()
        sys.stdout = captured_output

        filename = "file_append.txt"
        text = "!"
        count = module.append_write(filename, text)
        self.assertEqual(count, len(text))

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        self.construct_in_use(filename, target_construct)

    def test_with_in_use(self):

        target_construct = "with"
        self.construct_not_in_use(filename, target_construct)


if __name__ == "__main__":
    unittest.main()
