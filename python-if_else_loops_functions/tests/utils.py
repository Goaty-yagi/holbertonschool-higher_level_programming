import re
import ast


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
    counts = {construct: len(re.findall(
        rf'\b{re.escape(construct)}\b', script_content)) for construct in constructs}
    return counts


def count_variable_declarations(file_path):
    with open(file_path, 'r') as script_file:
        script_content = script_file.read()
    tree = ast.parse(script_content)  # generate an abstract syntax tree
    variable_count = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign): # ast.Assign representation of the assignment like statement: a = 10
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
