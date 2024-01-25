import unittest
import os
import sys

from utils import use_method, get_original_line, run_script, run_pycodestyle, count_constructs, count_variable_declarations


filename = "10-add.py"

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Use __import__ for relative import
module_name = '10-add'
module = __import__(module_name, fromlist=['add'])

add = module.add

class TestTask10(unittest.TestCase):
    def test_file_exist(self):
        """ Testing the target file exists. """

        self.assertTrue(os.path.exists(filename),
                        f"File '{filename}' does not exist")

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
        """ Testing a return value. """

        result = add(1,4)
        expected_output = 5
        self.assertEqual(result, expected_output)


    def test_count_import(self):
        """ Testing if import is used in the file. """

        target_construct = "import"
        count_obj = count_constructs(filename, [target_construct])
        expected_count = 0
        self.assertEqual(count_obj[target_construct], expected_count,
                         "There should be exactly no import statement.")



if __name__ == "__main__":
    unittest.main()
