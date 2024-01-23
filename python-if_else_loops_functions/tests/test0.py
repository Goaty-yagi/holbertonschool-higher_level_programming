import unittest
import subprocess
import os

from utils import replace_line, get_original_line

filename = "0-positive_or_negative.py"


class TestScriptOutput(unittest.TestCase):
    def run_script(self, path):
        result = subprocess.run(
            ["python3", path], stdout=subprocess.PIPE, text=True)
        script_output = result.stdout.strip()

        return script_output

    def test_negative_num(self):
        str = 'number = -100\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "-100 is negative"
        
        replace_line(filename, line_num, str)
        script_output = self.run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_positive_num(self):
        str = 'number = 100\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "100 is positive"
        
        replace_line(filename, line_num, str)
        script_output = self.run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_zero(self):
        str = 'number = 0\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "0 is zero"
        
        replace_line(filename, line_num, str)
        script_output = self.run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_file_exist(self):
        self.assertTrue(os.path.exists(filename),
                        f"File '{filename}' does not exist")

    def test_is_executable(self):

        is_exist = os.access(filename, os.X_OK)
        self.assertTrue(is_exist, f"{is_exist} should be executable")



if __name__ == "__main__":
    unittest.main()
