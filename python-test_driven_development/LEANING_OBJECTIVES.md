# Learning Objectives

- [What’s an interactive test](#what’s_an_interactive_test)
- [Why tests are important](#why_tests_are_important)
- [How to write Docstrings to create tests](#how_to_write_docstrings_to_create_tests)
- [How to write documentation for each module and function](#how_to_write_documentation_for_each_module_and_function)
- [What are the basic option flags to create tests](#what_are_the_basic_option_flags_to_create_tests)
- [How to find edge cases](#how_to_find_edge_cases)

## 1, What’s an interactive test
An interactive test typically refers to a testing scenario where a user or tester interacts directly with the system or application being tested. This type of testing often involves manual exploration and validation of the system's behavior by inputting various commands, data, or actions and observing the system's response.

Interactive testing can take various forms:

- Manual Testing: This involves testers manually interacting with the application's user interface, entering data, clicking buttons, and navigating through different features to verify functionality and identify potential issues.

- Exploratory Testing: Testers explore the application without predefined test cases, allowing them to uncover unexpected behaviors, usability issues, or edge cases by interacting with the software as an end-user would.

- User Acceptance Testing (UAT): End-users or stakeholders interact with the application to validate that it meets their requirements and expectations before deployment.

- Ad Hoc Testing: Testers perform spontaneous, unscripted tests by interacting with the system based on their intuition and experience, often uncovering critical issues that scripted tests might miss.

Interactive tests can be valuable for uncovering usability issues, edge cases, and unexpected behaviors that automated tests might overlook. 

## 2, Why tests are important
- Ensure Correctness: Tests verify that the software behaves as intended. By running tests, developers can catch and fix bugs early in the development process, preventing them from reaching production and causing issues for end-users.

- Maintain Quality: Tests act as a safety net when making changes to the codebase. They help ensure that new features or modifications do not inadvertently introduce regressions or break existing functionality.

- Facilitate Refactoring: Tests provide confidence when refactoring code. Developers can modify the codebase to improve design, performance, or readability, knowing that existing tests will detect any unintended consequences.

- Enable Collaboration: Tests encourage collaboration among team members by establishing a common understanding of requirements and expected behavior. They help align developers, testers, and stakeholders on what constitutes a successful implementation.

- Reduce Technical Debt: Writing tests upfront can prevent technical debt by fostering good coding practices and encouraging modular, maintainable code. Over time, a comprehensive test suite can save time and resources by minimizing the need for manual regression testing and troubleshooting.


## 3, How to write Docstrings to create tests
Writing docstrings for tests is important for providing clear documentation on what each test is intended to verify and how it should be used.

- Test Function Description: Start with a brief description of what the test is verifying. This description should be concise but informative, providing an overview of the test's purpose.

- Input Description: Describe the input values or parameters required for the test. This helps users understand what inputs are being tested and what values trigger specific behaviors.

- Expected Output Description: Explain the expected outcome or behavior of the test. This includes the expected return value, side effects, or changes in state that the test should detect.

- Example Usage: Provide example usage of the test function, including sample inputs and the expected output. This helps users understand how to use the test and what results to expect.

- Edge Cases and Special Conditions: If the test handles edge cases or special conditions, document them explicitly in the docstring. This ensures that users understand under what circumstances the test may behave differently.

```python
def test_square_area():
    """
    Test the calculation of the area of a square.

    Input:
        - side_length (float): The length of the side of the square.

    Expected Output:
        - area (float): The calculated area of the square.

    Example Usage:
        >>> test_square_area(3)
        9.0
        >>> test_square_area(0)
        0.0

    Edge Cases:
        - Testing with a negative side_length should raise a ValueError.
    """

```
## 4, How to write documentation for each module and function

### Module-level Documentation:
- Module Description: Begin with a brief description of the module's purpose and functionality. Describe what the module contains and how it can be used.

- Module-level Examples: Provide examples demonstrating how to use the module as a whole. These examples can show import statements, module-level functions or variables, and their expected behavior.

- Module-level Edge Cases: Include examples that cover edge cases or special scenarios relevant to the entire module.
```python
# Module-level documentation

"""
This module provides functions for calculating squares.
"""

# Module-level examples

"""
Example Usage:
>>> from square import square
>>> square(2)
4
>>> square(3.5)
12.25
"""

# Module-level edge cases

"""
Edge Cases:
>>> from square import square
>>> square(-2)
4
>>> square(0.5)
0.25
"""
```



### Function-level Documentation:
- Function Description: Start with a brief description of the function's purpose and functionality. Describe what the function does, its parameters, and its return value.

- Parameter Descriptions: Document each parameter accepted by the function, including its name, type, and any constraints or default values.

- Return Value Description: Document the value returned by the function, including its type and any special conditions or behaviors.

- Function Examples: Provide examples demonstrating how to use the function, including different input values and their corresponding output. Use >>> to denote input and ... for continuation lines, if necessary.

- Edge Cases and Error Handling: Include examples that cover edge cases, boundary conditions, and error handling scenarios. Show how the function behaves in exceptional situations, such as invalid input or unexpected conditions.

- Exceptions and Error Messages: Document any exceptions raised by the function and their meanings. Include examples that demonstrate how these exceptions are raised and handled.

```python
def square(x):
    """
    Calculate the square of a number.

    Parameters:
        x (int or float): The number to be squared.

    Returns:
        int or float: The square of the input number.

    Examples:
        >>> square(2)
        4
        >>> square(3.5)
        12.25
        >>> square(0)
        0

    Edge Cases:
        >>> square(-2)
        4
        >>> square(0.5)
        0.25

    Error Handling:
        >>> square('a')
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    """

    return x ** 2
```
## 5, What are the basic option flags to create tests
- -v, --verbose: Increase verbosity level. When used, doctest will provide more detailed output, including the name of each test and its status (pass or fail).

- -m, --module: Run doctests in a specified module. You can specify one or more module names separated by spaces.

- -f, --fail-fast: Stop on the first failure or error. With this option, doctest will stop execution as soon as it encounters the first failing or erroneous test case.

- -x, --exitfirst: Stop after the first test failure or error and exit immediately. This is similar to -f, but it exits without running any remaining tests.

- -b, --blank-line: Allow doctests to recognize blank lines in interactive sessions. By default, doctests ignore blank lines, but this option tells it to treat them as part of the input.

- -p, --preserve: Preserve leading whitespace in doctest examples. By default, doctests remove the common leading whitespace from each example, but this option tells it to preserve the original formatting.

- -t, --testdir: Run doctests in a specified directory. You can specify a directory path, and doctest will search for Python files containing doctests within that directory.

- -o, --option: Provide additional options to doctest. This flag allows you to pass additional options to doctest as a comma-separated list.

You can view the complete list of options and their descriptions by running python -m doctest --help in your terminal.
## 6, How to find edge cases

- Understand the Requirements: Gain a clear understanding of the requirements and specifications for your code. Identify any constraints, limits, or special conditions mentioned in the requirements.

- Identify Input Boundaries: Determine the boundaries or limits of the input space for your code. Consider the minimum and maximum values allowed for each input parameter.

- Consider Special Cases: Think about special cases or exceptional scenarios that might cause your code to behave differently. These could include zero, negative, or fractional values, as well as cases where the input is at the extremes of the allowable range.

- Consider Corner Cases: Consider corner cases where multiple input parameters interact in unique ways. These cases can often reveal unexpected behavior or errors in your code.

- Explore Invalid Inputs: Test your code with invalid inputs that fall outside the expected range or violate input constraints. Check how your code handles these invalid inputs and whether it provides appropriate error messages or handles them gracefully.

- Review Previous Issues and Bugs: Review any previous issues, bugs, or edge cases encountered during development or testing. Ensure that these cases are covered by your test suite to prevent regressions.

- Collaborate with Peers: Discuss potential edge cases with your peers or team members. They may offer different perspectives or insights that can help identify additional edge cases.

