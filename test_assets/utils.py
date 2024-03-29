import re
import ast
import subprocess


def run_pycodestyle(file_path):
    """ Run pycodestyle on the specified script and return the result. """
    command = ["pycodestyle", file_path]
    # CompletedProcess object returned
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return result

def run_script(file_path, args=[], executable="python3"):
    """ Execute the file_path, and return the output. """

    command = [executable, file_path] + args
    result = subprocess.run(
        command, stdout=subprocess.PIPE, text=True)
    script_output = result.stdout.strip()

    return script_output


def replace_line(file_path, line_number, new_code):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if 0 < line_number <= len(lines):
        ends_with_newline = lines[line_number - 1].endswith('\n')
        lines[line_number - 1] = new_code + \
            ('\n' if ends_with_newline == False else '')
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print(f"Error: Line number {line_number} is out of range.")


def get_original_line(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if 0 < line_number <= len(lines):
        return lines[line_number - 1]

    else:
        print(f"Error: Line number {line_number} is out of range.")


def count_constructs(file_path, constructs):
    with open(file_path, 'r') as script_file:
        script_content = script_file.read()
    script_content = remove_comments_and_docstrings(script_content)
    counts = {construct: len(re.findall(
        rf'\b{re.escape(construct)}\b', script_content)) for construct in constructs}
    return counts


def count_variable_declarations(file_path):
    with open(file_path, 'r') as script_file:
        script_content = script_file.read()
    tree = ast.parse(script_content)  # generate an abstract syntax tree
    variable_count = 0

    for node in ast.walk(tree):
        # ast.Assign representation of the assignment like statement: a = 10
        if isinstance(node, ast.Assign):
            variable_count += 1

    return variable_count


def use_method(file_path, method_name):
    with open(file_path, 'r') as script_file:
        script_content = script_file.read()
    tree = ast.parse(script_content)

    for node in ast.walk(tree):
        # ast.Attribute represents an attribute access or method invocation in the AST.
        if isinstance(node, ast.Attribute) and node.attr == method_name:
            return True

    return False

def use_function(filename, function_name):
    with open(filename, 'r') as file:
        code = file.read()
        tree = ast.parse(code)

        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == function_name:
                return True

    return False

def is_format_method_used_with_specifier(filename, specifier):
    with open(filename, 'r') as file:
        code = file.read()
        tree = ast.parse(code)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'format':
                for arg in node.args:
                    if isinstance(arg, ast.Str) and specifier in arg.s:
                        return True
    return False

def remove_comments_and_docstrings(code):
    # Remove single-line comments
    code = re.sub(r'#.*', '', code)

    # Remove multi-line comments
    code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
    code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)

    # Remove docstrings
    code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
    code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)

    return code

