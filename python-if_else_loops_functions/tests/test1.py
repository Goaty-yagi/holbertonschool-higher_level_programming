import unittest
import subprocess
import os

from utils import replace_line, get_original_line

filename = "1-last_digit.py"


class TestScriptOutput(unittest.TestCase):
    def run_script(self, path):
        result = subprocess.run(
            ["python3", path], stdout=subprocess.PIPE, text=True)
        script_output = result.stdout.strip()

        return script_output

    def test_negative_num(self):
        """ Test positive number and the last figit is less than 6"""
        str = 'number = -3472\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "Last digit of -3472 is -2 and is less than 6 and not 0"
        
        replace_line(filename, line_num, str)
        script_output = self.run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_positive_num(self):
        """ Test positive number and the last figit is greater than 5"""

        str = 'number = 9428\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "Last digit of 9428 is 8 and is greater than 5"
        
        replace_line(filename, line_num, str)
        script_output = self.run_script(filename)
        self.assertEqual(script_output, expected_output)
        replace_line(filename, line_num, original_line)

    def test_zero(self):
        """ Test negative number and the last figit is 0"""
        str = 'number = -100\n'
        line_num = 4
        original_line = get_original_line(filename, line_num)
        expected_output = "Last digit of -100 is 0 and is 0"
        
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
