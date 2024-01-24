import subprocess

def run_pycodestyle(file_path):
    """ Run pycodestyle on the specified script and return the result. """
    command = ["pycodestyle", file_path]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return result


def run_script(file_path, executable="python3"):
    """ Execute the file_path, and return the output. """

    command = [executable, file_path]
    result = subprocess.run(
        command, stdout=subprocess.PIPE, text=True)
    script_output = result.stdout.strip()

    return script_output


def replace_line(file_path, line_number, new_code):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if 0 < line_number <= len(lines):
        ends_with_newline = lines[line_number - 1].endswith('\n')
        lines[line_number - 1] = new_code + ('\n' if ends_with_newline == False else '')
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
