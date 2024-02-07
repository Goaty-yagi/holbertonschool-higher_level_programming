# Learning Objectives

- [How to Use the Python Interpreter](#how-to-use-the-python-interpreter)
- [How to print text and variables using print](#how-to-print-text-and-variables-using-print)
- [How to use strings](#how-to-use-strings)
- [What are indexing and slicing in Python](#what-are-indexing-and-slicing-in-python)
- [What is the official Python coding style and how to check your code with pycodestyle](#what-is-the-official-python-coding-style-and-how-to-check-your-code-with-pycodestyle)

## 1, How to use the Python interpreter

- 1, Open a Terminal/Command Prompt:
  -- On Windows, you can use the Command Prompt or PowerShell.
  -- On macOS and Linux, you can use the Terminal.

- 2, Launch the Python Interpreter:

```bash
python or python3 (depending on your system and Python version)
```

You should see the Python prompt (>>>), indicating that you are now in interactive mode.

```bash
exit() to close the Python interpreter
```

## 2, How to print text and variables using print

You can use the print function to display text and the values of variables.

### Printing Text:

```python
# Printing a simple text
print("Hello, World!")

# Printing multiple texts
print("Welcome", "to", "Python!")

# Printing text with escape characters
print("This is a new line.\nThis is another line.")

# Printing text without a newline at the end
print("This is on the same line.", end="")
print(" This is still on the same line.")

```

### Printing Variables:

```python
# Printing the value of a variable
name = "Nobuhiro"
print("Hello, " + name + "!")

# Using f-strings (Python 3.6 and later)
age = 99
print(f"{name} is {age} years old.")

# Using the format method
height = 1.754454654644
print("{} has a height of {:.2f} meters.".format(name, height))

# Without using the format method
print(f"{name} has a height of {height:.2f} meters.")

# Combining text and variables
print("The result is:", name)
```

In Python's string formatting, {: .2f} is a format specification used for formatting floating-point numbers.

## 3, How to use strings

### Creating Strings:

You can create strings in Python using single (' '), double (" "), or triple (''' ''' or """ """) quotes:

```python
# Single quotes
single_quoted_string = 'Hello, World!'

# Double quotes
double_quoted_string = "Python Programming"

# Triple quotes for multiline strings
multiline_string = '''
This is a multiline
string in Python.
'''
```

### Concatenating Strings:

You can concatenate strings using the + operator:

```python
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

```

### String Formatting:

Use string formatting to embed variables or expressions within a string:

```python
name = "Nobuhiro"
age = 99

message = f"Hello, {name}! You are {age} years old."
print(message)
# Output: Hello, Nobuhiro! You are 99 years old.

```

### Accessing Characters and Slicing:

You can access individual characters in a string using indexing and perform slicing to extract substrings:

```python
text = "Python"

# Accessing individual characters
first_char = text[0]  # P
second_char = text[1]  # y

# Slicing
substring = text[1:4]  # yth

```

### Common String Methods:

Python provides a variety of built-in string methods for common operations:

```python
text = "  Python Programming  "

# Removing leading and trailing whitespaces
cleaned_text = text.strip()

# Converting to lowercase and uppercase
lowercase_text = text.lower()
uppercase_text = text.upper()

# Finding the index of a substring
index = text.find("Programming")

# Replacing a substring
replaced_text = text.replace("Python", "JavaScript")

# Checking if a string starts or ends with a particular substring
starts_with_python = text.startswith("Python")
ends_with_ing = text.endswith("ing")

```

### String Length:

You can find the length of a string using the len() function:

```python
text = "Hello, World!"
length = len(text)
print(length)  # Output: 13

```

### Escape Characters:

Use escape characters to include special characters in a string:

```python
text = "Hello, World!"
length = len(text)
print(length)  # Output: 13

```

## 4, What are indexing and slicing in Python

Indexing and slicing are ways to access and manipulate elements in sequences in Python, such as strings, lists, and tuples. Both concepts are fundamental for working with ordered collections of items.

### Indexing:

Indexing refers to accessing individual elements within a sequence using their position or index. In Python, indexing is zero-based, meaning the first element has an index of 0, the second has an index of 1, and so on.

```python
text = "Python"

# Accessing individual characters
first_char = text[0]  # P
second_char = text[1]  # y
last_char = text[-1]  # n
second_last_char = text[-2]  # o
```

### Slicing:

Slicing involves extracting a portion or a range of elements from a sequence. The syntax for slicing is sequence[start:stop]. The start index is inclusive, and the stop index is exclusive.

```python
text = "Python"

# Slicing
substring = text[1:4]  # yth

```

In the example above, text[1:4] retrieves a substring starting from the character at index 1 (inclusive) to the character at index 4 (exclusive).

### Additional Slicing Features:

#### Omitting Start or Stop:

- If you omit the start index, the slice starts from the beginning.
- If you omit the stop index, the slice goes until the end.

```python
text = "Python"

# Omitting start or stop
substring1 = text[:3]    # Pyt (from the beginning to index 3 - exclusive)
substring2 = text[3:]    # hon (from index 3 to the end)

```

#### Step/Stride:

- You can specify a step or stride to skip elements in the slice.

```python
text = "Python"

# Slicing with step
every_second_char = text[::2]  # Pto (every second character)

```

## 5, What is the official Python coding style and how to check your code with pycodestyle

### What is the official Python coding style

The official coding style guide for Python is outlined in PEP 8 (Python Enhancement Proposal 8), titled "Style Guide for Python Code." Following a consistent coding style is important for enhancing code readability and maintainability, especially in collaborative projects.
You can access the official coding style guide from [here](https://peps.python.org/pep-0008/)

#### Indentation:

- Use 4 spaces per indentation level.

#### Maximum Line Length:

- Limit all lines to a maximum of 79 characters for code, and 72 for docstrings and comments.

#### Imports:

Imports should usually be on separate lines and should be grouped in the following order:

- Standard library imports.
- Related third-party imports.
- Local application/library specific imports.

#### Whitespace in Expressions and Statements:

Avoid extraneous whitespace in the following situations:

- Immediately inside parentheses, brackets, or braces.
- Immediately before a comma, semicolon, or colon.
- Immediately before the open parenthesis that starts the argument list of a function call.

#### Comments:

- Comments should be complete sentences and should be used sparingly.

#### Naming Conventions:

- Function and variable names should be lowercase, with words separated by underscores.
- Constants should be in all uppercase with underscores separating words.
- Class names should follow the CapWords (or CamelCase) convention.

#### Function and Method Arguments:

- Avoid using mutable default arguments.

### How to check your code with pycodestyle

- To check your Python code against PEP 8 using a tool, you can use pycodestyle. Here are the steps:

```bash
pip install pycodestyle or pip3 install pycodestyle
```

- Check Your Code:

```bash
pycodestyle your_file.py
```

- Automatically Fix Some Issues:

```bash
autopep8 --in-place --aggressive --aggressive your_file.py
```
