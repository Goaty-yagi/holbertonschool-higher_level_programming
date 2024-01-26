import unittest

from parent_test import ParentTest

filename = "2-args.py"


class TestTask2(ParentTest):
    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)


    def test_imported_script(self):
        module = "2-args"
        path = self.path
        self.imported_script(module, path)

    def test_count_star(self):
        """ Testing if import * is used in the file. """

        target_construct = "import *"
        self.construct_in_use(filename, target_construct)

    def test_format_in_use(self):
        """ Testing the format method is used in the file. """

        method_name = "format"
        self.method_in_use(filename, method_name)

    def test_script_output(self):
        """ Testing a specific file output is expected. """

        args = ["Hello", "Welcome", "To", "The", "Best", "School"]
        expected_output = "6 arguments:\n1: Hello\n2: Welcome\n3: To\n4: The\n5: Best\n6: School"
        self.script_output_expected(filename, expected_output, args)
    
    def test_no_arg(self):
        """ Testing a specific file output without arg. """

        expected_output = "0 arguments."
        self.script_output_expected(filename, expected_output)

    def test_one_arg(self):
        """ Testing a specific file output with 1 arg. """

        args = ["Hello"]
        expected_output = "1 argument:\n1: Hello"
        self.script_output_expected(filename, expected_output, args)



if __name__ == "__main__":
    unittest.main()
