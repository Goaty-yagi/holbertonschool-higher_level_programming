import unittest
import os

from utils import run_pycodestyle, get_original_line, run_script, replace_line


filename = "7-edges.py"


class TestScriptOutput(unittest.TestCase):
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
        script_output = run_script(filename)
        expected_output = "First 3 letters: Hol\nLast 2 letters: on\nMiddle word: olberto"
        self.assertEqual(script_output, expected_output)


    def test_script_output2(self):
        str = 'word = "JavascriptSchool"\n'
        line_num = 2
        original_line = get_original_line(filename, line_num)
        expected_output = """First 3 letters: Jav\nLast 2 letters: ol\nMiddle word: avascriptSchoo"""
        
        replace_line(filename, line_num, str)
        script_output = run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)


    def test_line_count(self):
        """ Testing line number of the file is expected. """

        with open(filename, 'r') as file:
            script_content = file.read()

        lines = script_content.splitlines()
        expected_line_count = 8
        self.assertEqual(len(lines), expected_line_count,
                         "Line count mismatch")


if __name__ == "__main__":
    unittest.main()
