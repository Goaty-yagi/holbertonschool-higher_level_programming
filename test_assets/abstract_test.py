import unittest
import os
import sys
import io
import importlib

from .utils import use_function,is_format_method_used_with_specifier, count_constructs, get_original_line, run_script, run_pycodestyle, use_method, replace_line

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))


class AbstractTest(unittest.TestCase):
    def file_exist(self, path):
        """ Testing the target file exists. """

        self.assertTrue(os.path.exists(path),
                        f"File '{path}' does not exist")

    def file_is_executable(self, path):
        """ Testing the target file is executable. """

        is_executable = os.access(path, os.X_OK)
        self.assertTrue(is_executable, f"{path} should be executable")

    def file_has_contents(self, path):
        """ Testing README.md exists in the current dir, and has contents. """

        with open(path, 'r') as script_file:
            script_content = script_file.read()

        self.assertTrue(len(script_content),
                        f"File '{path}' does not have contents")

    def meet_pycode_style(self, path):
        """ Testing  a specific file meet pep8 requirements """

        result = run_pycodestyle(path)
        # Check if pycodestyle result is successful (exit code 0)
        self.assertEqual(result.returncode, 0,
                         f"pycodestyle check failed:\n{result.stdout}")

    def line_content_expected(self, path, expected, line_num):
        """ Testing the first line of a specific file is expected. """

        first_line = get_original_line(path, line_num)
        self.assertEqual(first_line, expected)

    def common_test(self, filename):
        """  testing file exists, file is executable, README.md exists and has contents,
        firts line is expected, meet pycode_style.
        """
        readme = "README.md"
        shebang = "#!/usr/bin/python3\n"
        self.file_exist(filename)
        self.file_is_executable(filename)
        self.file_exist(readme)
        self.file_has_contents(readme)
        self.line_content_expected(filename, shebang, 1)
        self.meet_pycode_style(filename)

    def script_output_expected(self, path, expected, args=[]):
        """ Testing a specific file output is expected. """

        script_output = run_script(path, args)
        self.assertEqual(script_output, expected)

    def imported_script(self, module, path, expected=""):
        """ Testing a case the file is imported. no return expected as default.
        case __name__ = "__main__"

        the module should be in the package
        """

        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", path)))
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            # Import the script dynamically
            module_name = module
            importlib.import_module(module_name)
            self.assertEqual(captured_output.getvalue(), expected)

        finally:
            # Restore sys.stdout to its original value
            sys.stdout = sys.__stdout__

    def construct_in_use(self, path, target):
        """ Testing number of construct in use in the file. """

        count_obj = count_constructs(path, [target])
        
        self.assertEqual(count_obj[target], 0,
                         f"There shouldn't be <{target}> statement in use.")

    def construct_not_in_use(self, path, target):
        """ Testing number of construct in use in the file. """

        count_obj = count_constructs(path, [target])
        self.assertGreaterEqual(count_obj[target], 1,
                                f"There shouldn be <{target}> statement in use.")

    def method_in_use(self, path, method_name):
        """ Testing the format method is used in the file. """

        has_format_method = use_method(path, method_name)
        expected = True
        self.assertEqual(has_format_method, expected,
                         f"The method '{method_name}' is not used in the script.")

    def method_not_in_use(self, path, method_name):
        """ Testing the format method is used in the file. """

        has_format_method = use_method(path, method_name)
        expected = False
        self.assertEqual(has_format_method, expected,
                         f"The method '{method_name}' is used in the script.")

    def replace_line_test(self, path, expected, line, line_num):
        """ Testing the behavior of a script(mainly for script not function) 
        when a specific line in the script file is modified, still print as expected. """

        original_line = get_original_line(path, line_num)

        replace_line(path, line_num, line)
        script_output = run_script(path)
        self.assertEqual(script_output, expected)
        replace_line(path, line_num, original_line)

    def line_count(self, path, expected):
        """ Testing line number of the file is expected. """

        with open(path, 'r') as file:
            script_content = file.readlines()

        # Count the lines using splitlines() method
        total_lines = len(script_content)

        # Assert that the actual line count matches the expected line count
        self.assertEqual(total_lines, expected,
                         "Line count mismatch")

    def function_used(self, path, function_name):
        result = use_function(path, function_name)

        self.assertTrue(result, f"function {function_name} is not used.")

    def function_not_used(self, path, function_name):
        result = use_function(path, function_name)

        self.assertFalse(result, f"function {function_name} is used.")

    def format_with_specifier_used(self, path, specifier):
        result = is_format_method_used_with_specifier(path, specifier)

        self.assertFalse(result, f"function {specifier} is not used.")

    def error_handling(self, function, error_type):
        # Testing that the function raises expected error
        with self.assertRaises(error_type):
            function()

