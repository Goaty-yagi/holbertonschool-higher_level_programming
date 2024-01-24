import unittest
import subprocess
import os

from utils import count_constructs, count_variable_declarations, use_method

filename = "2-print_alphabet.py"


class TestScriptOutput(unittest.TestCase):
    def run_script(self, path):
        result = subprocess.run(
            ["python3", path], stdout=subprocess.PIPE, text=True)
        script_output = result.stdout.strip()

        return script_output

    def test_count_print(self):
        target_construct = "print"
        count_obj = count_constructs(filename, [target_construct])
        expected_count = 1
        self.assertEqual(count_obj[target_construct], expected_count,
                         "There should be exactly one print statement.")

    def test_count_loop(self):
        target_constructs = ["for", "while"]
        count_obj = count_constructs(filename, target_constructs)
        expected_count = 1
        total_count = count_obj["for"] + count_obj["while"]
        self.assertEqual(total_count, expected_count,
                         "There should be exactly one loop statement.")


    def test_count_import(self):
        target_construct = "import"
        count_obj = count_constructs(filename, [target_construct])
        expected_count = 0
        self.assertEqual(count_obj[target_construct], expected_count,
                         "There should be exactly no import statement.")

    def test_variable_declarations(self):
        variable_count = count_variable_declarations(filename)
        expected_count = 0
        self.assertEqual(variable_count, expected_count,
                         f"Expected variable declaration count: {expected_count}")


    def test_format_in_use(self):
        method_name = "format"
        has_format_method = use_method(filename, method_name)
        expected = True
        self.assertEqual(has_format_method, expected,
                         f"The method '{method_name}' is not used in the script.")


    def test_file_exist(self):
        self.assertTrue(os.path.exists(filename),
                        f"File '{filename}' does not exist")

    def test_is_executable(self):
        is_exist = os.access(filename, os.X_OK)
        self.assertTrue(is_exist, f"{is_exist} should be executable")


if __name__ == "__main__":
    unittest.main()
