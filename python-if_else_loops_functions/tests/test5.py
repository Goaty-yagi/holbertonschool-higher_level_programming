import unittest
import os

from utils import use_method, get_original_line, run_script, run_pycodestyle, count_constructs, count_variable_declarations


filename = "5-print_comb2.py"


class TestTask3(unittest.TestCase):
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
        """ Testing a specific file meets pep8 requirements. """

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
        """ Testing a specific file output is expected. """

        script_output = run_script(filename)
        lines = script_output.strip().split(' ')
        for i in range(100):
            if i < 10:
                self.assertEqual(lines[i], "0{},".format(i))
            else:
                self.assertEqual(lines[i], "{}{}".format(
                    i, "," if i != 99 else ""))

    def test_count_print(self):
        """ Testing  a number of print function in use in the file. """

        target_construct = "print"
        count_obj = count_constructs(filename, [target_construct])
        expected_count = 2
        self.assertLessEqual(count_obj[target_construct], expected_count,
                             "There should be less than {expected_count} print statement.")

    def test_count_loop(self):
        """ Testing  a number of for or while loop in use in the file. """

        target_constructs = ["for", "while"]
        count_obj = count_constructs(filename, target_constructs)
        expected_count = 1
        total_count = count_obj["for"] + count_obj["while"]
        self.assertEqual(total_count, expected_count,
                         "There should be exactly one loop statement.")

    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        count_obj = count_constructs(filename, [target_construct])
        expected_count = 0
        self.assertEqual(count_obj[target_construct], expected_count,
                         "There should be exactly no import statement.")

    def test_variable_declarations(self):
        """ Testing if variable is declared in the file. """

        variable_count = count_variable_declarations(filename)
        expected_count = 0
        self.assertEqual(variable_count, expected_count,
                         f"Expected variable declaration count: {expected_count}")

    def test_format_in_use(self):
        """ Testing the format method is used in the file. """

        method_name = "format"
        has_format_method = use_method(filename, method_name)
        expected = True
        self.assertEqual(has_format_method, expected,
                         f"The method '{method_name}' is not used in the script.")


if __name__ == "__main__":
    unittest.main()
