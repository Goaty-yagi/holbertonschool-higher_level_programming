import unittest
import os
import sys
import io

from utils import count_constructs, get_original_line, run_script, run_pycodestyle, use_method, replace_line


filename = "5-variable_load.py"


class TestTask5(unittest.TestCase):
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
        expected_output = "98"
        self.assertEqual(script_output, expected_output)

    def test_script_output2(self):
        str = 'a = 2999\n'
        line_num = 2
        original_line = get_original_line(filename, line_num)
        expected_output = "2999"
        
        replace_line(filename, line_num, str)
        script_output = run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_imported_script(self):
        """ Testing a case the file is imported. no return expected. """
        sys.path.append(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")))
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            # Import the script dynamically
            module_name = '5-variable_load'
            __import__(module_name)
            # capture output

            expected_output = ""
            self.assertEqual(captured_output.getvalue(), expected_output)

        finally:
            # Restore sys.stdout to its original value
            sys.stdout = sys.__stdout__

    def test_import_used(self):
        """ Testing if import used in the file. """

        target_construct = "import"
        count_obj = count_constructs(filename, [target_construct])
        expected_count = 1
        self.assertEqual(count_obj[target_construct], expected_count,
                         f"There shouldn't be <{target_construct}> statement in use.")

    def test_count_star(self):
        """ Testing if import * is used in the file. """

        target_construct = "import *"
        count_obj = count_constructs(filename, [target_construct])
        expected_count = 0
        self.assertEqual(count_obj[target_construct], expected_count,
                         f"There shouldn't be <{target_construct}> statement in use.")


if __name__ == "__main__":
    unittest.main()
