import unittest
import subprocess
import os
import this

filename = "9-easter_egg.py"


class TestScriptOutput(unittest.TestCase):
    def run_script(self, path):
        # Run the script and capture its output
        result = subprocess.run(
            ["python3", path], stdout=subprocess.PIPE, text=True)

        script_output = result.stdout.strip()

        return script_output

    def test_file_exist(self):
        self.assertTrue(os.path.exists(filename),
                        f"File '{filename}' does not exist")

    def test_is_executable(self):

        is_exist = os.access(filename, os.X_OK)
        self.assertTrue(is_exist, f"{is_exist} should be executable")

    def test_max_line_length(self):
        script_output = self.run_script(filename)
        max_line_length = max(len(line) for line in script_output.split('\n'))
        self.assertLessEqual(max_line_length, 98)

if __name__ == "__main__":
    unittest.main()
