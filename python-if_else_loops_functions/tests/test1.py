import unittest
import os

from utils import replace_line, get_original_line, run_script, run_pycodestyle

filename = "1-last_digit.py"


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

    def test_negative_num(self):
        """ Test positive number and the last digit is less than 6"""

        str = 'number = -3472\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "Last digit of -3472 is -2 and is less than 6 and not 0"
        
        replace_line(filename, line_num, str)
        script_output = run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_positive_num(self):
        """ Test positive number and the last figit is greater than 5"""

        str = 'number = 9428\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "Last digit of 9428 is 8 and is greater than 5"
        
        replace_line(filename, line_num, str)
        script_output = run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_zero(self):
        """ Test negative number and the last figit is 0"""

        str = 'number = -100\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "Last digit of -100 is 0 and is 0"
        
        replace_line(filename, line_num, str)
        script_output = run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)


if __name__ == "__main__":
    unittest.main()
