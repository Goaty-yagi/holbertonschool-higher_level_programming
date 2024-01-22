import unittest
import subprocess


class TestScriptOutput(unittest.TestCase):
    def run_script(self, path):
        # Run the script and capture its output
        result = subprocess.run(
            ["python3", path], stdout=subprocess.PIPE, text=True)

        # Extract the output from the result
        script_output = result.stdout.strip()

        # Check actual output
        print("Actual Output:", repr(script_output))

        return script_output

    def test_script_output(self):

        script_output = self.run_script("2-print.py")

        # Define the expected output based on the script
        expected_output = '"Programming is like building a multilingual puzzle'

        # Assert that the actual output matches the expected output
        self.assertEqual(script_output, expected_output)

    def test_line_count(self):
        # Get the script output
        script_output = self.run_script("2-print.py")

        # Check if script_output is empty
        if not script_output:
            self.fail("Script output is empty")

        # Count the lines using wc -l
        line_count_command = f"echo '{script_output}' | wc -l"
        line_count_process = subprocess.run(
            line_count_command, shell=True, stdout=subprocess.PIPE, text=True)

        # Extract the line count from the result
        actual_line_count_str = line_count_process.stdout.strip()

        try:
            actual_line_count = int(actual_line_count_str)
        except ValueError:
            self.fail(f"Invalid line count: {actual_line_count_str}")

        # Define the expected line count
        expected_line_count = 1

        # Assert that the actual line count matches the expected line count
        self.assertEqual(actual_line_count, expected_line_count)


if __name__ == "__main__":
    unittest.main()
