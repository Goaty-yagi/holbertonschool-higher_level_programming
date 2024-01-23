import unittest
import subprocess
import os

from utils import replace_line, get_original_line
from printer import compare_output 

filename = "7-edges.py"


class TestScriptOutput(unittest.TestCase):
    def run_script(self, path):
        result = subprocess.run(
            ["python3", path], stdout=subprocess.PIPE, text=True)
        script_output = result.stdout.strip()

        return script_output

    def test_file_exist(self):
        self.assertTrue(os.path.exists(filename),
                        f"File '{filename}' does not exist")

    def test_script_output(self):
        script_output = self.run_script(filename)
        expected_output = "First 3 letters: Hol\nLast 2 letters: on\nMiddle word: olberto"
        self.assertEqual(script_output, expected_output)

    def test_script_output2(self):
        str = 'word = "JavascriptSchool"\n'
        line_num = 2
        original_line = get_original_line(filename, line_num)
        expected_output = """First 3 letters: Jav\nLast 2 letters: ol\nMiddle word: avascriptSchoo"""
        
        replace_line(filename, line_num, str)
        script_output = self.run_script(filename)
        self.assertEqual(script_output, expected_output)
        compare_output(repr(script_output), expected_output)
        replace_line(filename, line_num, original_line)

    def test_is_executable(self):
        is_exist = os.access(filename, os.X_OK)
        self.assertTrue(is_exist, f"{is_exist} should be executable")

    def test_line_count(self):
        with open(filename, 'r') as file:
            script_content = file.read()

        lines = script_content.splitlines()
        expected_line_count = 8
        self.assertEqual(len(lines), expected_line_count,
                         "Line count mismatch")


if __name__ == "__main__":
    unittest.main()