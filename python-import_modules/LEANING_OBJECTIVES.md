# Learning Objectives

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function dir()
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs


## 1, Why Python programming is awesome
Python programming is awesome for a variety of reasons, making it a popular and widely adopted language across different domains.
- Readability and Simplicity:
Python emphasizes readability and simplicity, making it easy to learn and understand. Its syntax allows developers to express concepts in fewer lines of code compared to other languages, reducing the likelihood of errors and enhancing code clarity.

- High-Level Language:
Python is a high-level language, abstracting away many low-level details. This makes it easier for developers to focus on solving problems rather than dealing with intricate system-specific nuances.

## 2, How to import functions from another file
You can import functions from another file using the import statement. 
## 3, How to use imported functions
Once you have imported functions from another file/module, you can use them in your current script or module as if they were defined locally.
```python
from test import add

result = add(1, 2)
print("Result: " result) # Result is 3
```
## 4, How to create a module
Creating a module in Python is essentially creating a Python script with reusable code and saving it with a .py extension. 

## 5, How to use the built-in function dir()
### Listing Names in the Current Scope:
When called without any arguments, dir() returns a list of names in the current local scope.

```python
# Example 1
names_in_scope = dir()
print(names_in_scope)

```

### Listing Names in a Module or Object:
When called with an argument, dir() returns a list of names defined in that module or object.
```python
# Example 2
import math

math_names = dir(math)
print(math_names)

```

### Interactive Exploration:
dir() is often used interactively in the Python interpreter to explore the attributes of an object.
```python
# Example 3
my_list = [1, 2, 3]

# List the attributes and methods of the list object
list_attributes = dir(my_list)
print(list_attributes)

```

## 6, How to prevent code in your script from being executed when imported
You can use the if __name__ == "__main__": construct to prevent certain code from being executed when the script is imported as a module.
## 7, How to use command line arguments with your Python programs
You can use the sys.argv list from the sys module.
```python
# my_script.py
import sys

# Access command line arguments using sys.argv
# sys.argv[0] is the script name itself
# sys.argv[1:], starting from index 1, are the command line arguments
arguments = sys.argv[1:]

# Print the command line arguments
print("Command line arguments:", arguments)
```

Run the command.
```bash
python my_script.py arg1 arg2 arg3

```
Expected output.
```bash
Command line arguments: ['arg1', 'arg2', 'arg3']

```





