import unittest
import os
import sys, io

from utils import count_constructs, get_original_line, run_script, run_pycodestyle, use_method


filename = "1-calculation.py"


class TestTask1(unittest.TestCase):
    def test_file_exist(self):
        """ Testing the target file exists. """

        self.assertTrue(os.path.exists(filename),
                        f"File '{filename}' does not exist")

    def test_is_executable(self):
        """ Testing the target file is executable. """

        is_executable = os.access(filename, os.X_OK)
        self.assertTrue(is_executable, f"{filename} should be executable")

    def test_readme_exist(self):
        """ Testing README.md exists in the current dir, and has contents. """

        readme = "README.md"
        self.assertTrue(os.path.exists(readme),
                        f"File '{readme}' does not exist")
        with open(readme, 'r') as script_file:
            script_content = script_file.read()

        self.assertTrue(len(script_content),
                        f"File '{readme}' does not have contents")

    def test_pycode_style(self):
        """ Testing  a specific file meet pep8 requirements """

        result = run_pycodestyle(filename)
        # Check if pycodestyle result is successful (exit code 0)
        self.assertEqual(result.returncode, 0,
                         f"pycodestyle check failed:\n{result.stdout}")

    def test_first_line(self):
        """ Testing the first line of a specific file is expected. """

        first_line = get_original_line(filename, 1)
        expected_line = "#!/usr/bin/python3\n"
        self.assertEqual(first_line, expected_line)

    def test_script_output(self):
        """ Testing a specific file output is expected. """

        script_output = run_script(filename)
        expected_output = "10 + 5 = 15\n10 - 5 = 5\n10 * 5 = 50\n10 / 5 = 2"
        self.assertEqual(script_output, expected_output)

    def test_imported_script(self):
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            # Import the script dynamically
            module_name = '1-calculation'
            __import__(module_name)
            # capture output

            expected_output = ""
            self.assertEqual(captured_output.getvalue(), expected_output)

        finally:
            # Restore sys.stdout to its original value
            sys.stdout = sys.__stdout__

    def test_count_star(self):
        """ Testing if import * is used in the file. """

        target_construct = "import *"
        count_obj = count_constructs(filename, [target_construct])
        expected_count = 0
        self.assertEqual(count_obj[target_construct], expected_count,
                         f"There shouldn't be <{target_construct}> statement in use.")

    def test_format_in_use(self):
        """ Testing the format method is used in the file. """

        method_name = "format"
        has_format_method = use_method(filename, method_name)
        expected = True
        self.assertEqual(has_format_method, expected,
                         f"The method '{method_name}' is not used in the script.")


if __name__ == "__main__":
    unittest.main()
