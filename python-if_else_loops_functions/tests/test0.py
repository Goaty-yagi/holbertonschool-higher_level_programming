import unittest
import subprocess
import os

from utils import replace_line, get_original_line


filename = "0-positive_or_negative.py"


class TestTask0(unittest.TestCase):
    def run_script(self, path):
        """ Execute the file_path, and return the output. """
        result = subprocess.run(
            ["python3", path], stdout=subprocess.PIPE, text=True)
        script_output = result.stdout.strip()

        return script_output

    def test_readme_exist(self):
        """ Testing README.md exists in the current dir, and has contents. """

        readme = "README.md"
        self.assertTrue(os.path.exists(readme),
                        f"File '{readme}' does not exist")
        with open(readme, 'r') as script_file:
            script_content = script_file.read()

        self.assertTrue(len(script_content),
                        f"File '{readme}' does not have contents")

    def test_negative_num(self):
        """ Testing the behavior of a script when a specific line in the script file
         is modified to include a negative number. """
         
        str = 'number = -100\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "-100 is negative"

        replace_line(filename, line_num, str)
        script_output = self.run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_positive_num(self):
        """ Testing the behavior of a script when a specific line in the script file
         is modified to include a positive number. """

        str = 'number = 100\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "100 is positive"

        replace_line(filename, line_num, str)
        script_output = self.run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_zero(self):
        """ Testing the behavior of a script when a specific line in the script file
         is modified to include a positive number. """

        str = 'number = 0\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "0 is zero"

        replace_line(filename, line_num, str)
        script_output = self.run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_file_exist(self):
        """ Testing the target file exists. """

        self.assertTrue(os.path.exists(filename),
                        f"File '{filename}' does not exist")

    def test_is_executable(self):
        """ Testing the target file is executable. """

        is_executable = os.access(filename, os.X_OK)
        self.assertTrue(is_executable, f"{is_executable} should be executable")


if __name__ == "__main__":
    unittest.main()
