import unittest
import subprocess


class TestScriptOutput(unittest.TestCase):
    def run_script(self, path):
        # Run the script and capture its output
        result = subprocess.run(
            ["python3", path], stdout=subprocess.PIPE, text=True)

        # Extract the output from the result
        script_output = result.stdout.strip()

        return script_output

    def test_script_output(self):

        script_output = self.run_script("3-print_number.py")

        # Define the expected output based on the script
        expected_output = '98 Battery street'

        # Assert that the actual output matches the expected output
        self.assertEqual(script_output, expected_output)

    def test_line_count(self):
        with open("3-print_number.py", 'r') as file:
            script_content = file.read()

        # Count the lines using splitlines() method
        lines = script_content.splitlines()

        expected_line_count = 3
        
        # Assert that the actual line count matches the expected line count
        self.assertEqual(len(lines), expected_line_count, "Line count mismatch")



if __name__ == "__main__":
    unittest.main()
