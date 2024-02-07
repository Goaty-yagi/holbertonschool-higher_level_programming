# Learning Objectives

- [What’s the difference between errors and exceptions](what’s-the-difference-between-errors-and-exceptions)
- [What are exceptions and how to use them](what-are-exceptions-and-how-to-use-them)
- [When do we need to use exceptions](when-do-we-need-to-use-exceptions)
- [How to correctly handle an exception](how-to-correctly-handle-an-exception)
- [What’s the purpose of catching exceptions](what’s-the-purpose-of-catching-exceptions)
- [How to raise a builtin exception](how-to-raise-a-builtin-exception)
- [When do we need to implement a clean-up action after an exception](when-do-we-need-to-implement-a-clean-up-action-after-an-exception)

## 1, What’s the difference between errors and exceptions

### Errors:

- In a broad sense, "errors" refer to any unexpected or undesirable situation that occurs during the execution of a program, causing it to terminate abnormally or produce incorrect results.
- Errors can include syntax errors, which occur when the code violates the rules of the Python language and cannot be executed, as well as runtime errors, which occur during the execution of the program and may cause it to crash.
- Syntax errors are detected by the Python interpreter before the program starts running, while runtime errors are detected during the execution of the program.
### Exceptions:

- "Exceptions" are a specific type of error that occurs during the execution of a Python program and disrupts the normal flow of execution.
- Exceptions are raised when a statement or function encounters an error condition that it cannot handle, such as dividing by zero, accessing a non-existent index in a list, or trying to open a file that does not exist.
- When an exception occurs, Python raises an exception object, which contains information about the type of error that occurred and where it occurred in the code.
- Python provides mechanisms for catching and handling exceptions using try-except blocks, allowing you to gracefully handle errors and prevent your program from crashing.

## 2, What are exceptions and how to use them

Exceptions in Python are events that occur during the execution of a program and disrupt the normal flow of control. They typically represent errors or exceptional conditions that need to be handled gracefully to prevent the program from crashing.

### 1. Exception Handling with try-except Blocks:
You can use the try-except statement to catch and handle exceptions in Python. This allows you to gracefully handle errors and prevent your program from crashing.

```python
try:
    # Code that may raise an exception
    result = 10 / 0  # Attempting to divide by zero
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero")

```

### 2. Handling Multiple Exceptions:
You can handle multiple exceptions by specifying multiple except blocks or by using a tuple of exception types.
```python
try:
    # Code that may raise exceptions
    result = int("abc")  # Attempting to convert a string to an integer
except ValueError:
    # Handle ValueError
    print("Error: Invalid conversion")
except TypeError:
    # Handle TypeError
    print("Error: Type mismatch")

```

### 3. Handling All Exceptions:
You can use a generic except block to catch all exceptions. However, this is generally discouraged because it can make debugging more difficult.

```python
try:
    # Code that may raise exceptions
    result = 10 / 0  # Attempting to divide by zero
except:
    # Handle any exception
    print("An error occurred")

```

### 4. The else Clause:
You can use the else clause in a try-except statement to execute code that should run only if no exceptions occur.
```python
try:
    # Code that may raise an exception
    result = 10 / 2  # Division
except ZeroDivisionError:
    # Handle division by zero
    print("Error: Division by zero")
else:
    # Code to execute if no exception occurs
    print("Result:", result)

```

### 5. The finally Clause:
You can use the finally clause to execute cleanup code that should always run, whether an exception occurs or not.

```python
try:
    # Code that may raise an exception
    result = 10 / 0  # Attempting to divide by zero
except ZeroDivisionError:
    # Handle division by zero
    print("Error: Division by zero")
finally:
    # Cleanup code that always runs
    print("End of try-except block")

```

### 6. Raising Exceptions:
You can manually raise exceptions using the raise statement to signal an error condition.
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

try:
    validate_age(-5)  # Attempting to validate a negative age
except ValueError as e:
    print(e)  # Output: Age cannot be negative

```
## 3, When do we need to use exceptions
Exceptions are used to handle unexpected or exceptional situations that may occur during the execution of a program.
Example:
- Handling Errors:
- Input Validation
- Error Reporting
- Control Flow
## 4, How to correctly handle an exception
Handling exceptions correctly involves using try-except blocks to catch and handle specific types of exceptions that may occur during program execution. Here's a step-by-step guide on how to correctly handle exceptions:

- Identify Potential Errors: Identify the parts of your code where exceptions might occur, such as operations involving I/O, network communication, or user input.

- Wrap Code in a try Block: Place the code that may raise an exception inside a try block.

- Handle Exceptions: Use one or more except blocks to catch specific types of exceptions that you expect might occur. Inside each except block, provide code to handle the exception gracefully.

- Handle Multiple Exceptions: If necessary, use multiple except blocks to handle different types of exceptions separately.

- Handle Generic Exceptions: Optionally, you can use a generic except block to catch any unexpected exceptions that are not handled by specific except blocks. This allows you to log or report unexpected errors.

- Cleanup Code: Use the finally block to provide cleanup code that should always run, regardless of whether an exception occurred.

## 5, What’s the purpose of catching exceptions
- Graceful Error Handling
- Preventing Program Crashes
- Facilitating Debugging
## 6, How to raise a builtin exception
You can raise a built-in exception using the raise statement followed by the exception type. Here's how you can raise a built-in exception:
```python
# Raise a ValueError exception
raise ValueError("This is a custom error message")

```
## 7, When do we need to implement a clean-up action after an exception
Implementing a clean-up action after an exception is important in situations where your program needs to release resources or perform certain actions regardless of whether an exception occurred or not.
Example:

- Resource Management: If your program acquires system resources such as file handles, network connections, or database connections, it's essential to release these resources properly to avoid resource leaks. Clean-up actions ensure that resources are released even if an exception occurs during the execution of your program.

- Transactional Operations: In transactional operations, you may need to roll back changes or finalize transactions in case of an exception. Clean-up actions help to ensure that your program maintains data integrity and consistency by reverting changes made before the exception occurred.

- Temporary Modifications: If your program makes temporary modifications to the system state or configuration, you may need to revert these modifications in case of an exception. Clean-up actions allow you to restore the system to a consistent state and prevent unintended side effects.

- Memory Management: In memory-intensive applications, clean-up actions may be necessary to release dynamically allocated memory or perform garbage collection. This helps to prevent memory leaks and optimize resource usage in your program.

- File Operations: When working with files, it's important to close file handles properly to release locks and ensure data integrity. Clean-up actions ensure that file handles are closed even if an exception occurs while reading, writing, or manipulating files.

```python
file = open('filename.txt', 'r')
try:
    # Code to read or write to the file
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found")
finally:
    # Close the file
    file.close()

```