# Python - Data Structures: Lists, Tuples

This repository contains Python code examples and explanations for working with two fundamental data structures: Lists and Tuples. Whether you're a beginner learning Python or an experienced developer looking for a quick reference, this repository aims to provide clear and concise examples to enhance your understanding.

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/LEARNING_OBJECTIVES.md) file for details.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Practice Exercises

### 0. Print a list of integers

**File:** [0-print_list_integer.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/0-print_list_integer.py)<br>
**Description:** Write a function that prints all integers of a list.<br>
**Requirement:** <br>
- Prototype: def print_list_integer(my_list=[]):
- Format: one integer per line.
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers

### 1. Secure access to an element in a list

**File:** [1-element_at.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/1-element_at.py)<br>
**Description:** Write a function that retrieves an element from a list.<br>
**Requirement:** <br>
- Prototype: def element_at(my_list, idx):
- If idx is negative, the function should return None
- If idx is out of range (> of number of element in my_list), the function should return None
- You are not allowed to import any module
- You are not allowed to use try/except


### 2. Replace element

**File:** [2-replace_in_list.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/2-replace_in_list.py)<br>
**Description:** Write a function that replaces an element of a list at a specific position.<br>
**Requirement:** <br>
- Prototype: def replace_in_list(my_list, idx, element):
- If idx is negative, the function should not modify anything, and returns the original list
- If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use try/except


### 3. Print a list of integers... in reverse!

**File:** [3-print_reversed_list_integer.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/3-print_reversed_list_integer.py)<br>
**Description:** Write a function that prints all integers of a list, in reverse order.<br>
**Requirement:** <br>
- Prototype: def print_reversed_list_integer(my_list=[]):
- Format: one integer per line.
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers


### 4. Replace in a copy

**File:** [4-new_in_list.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/4-new_in_list.py)<br>
**Description:** Write a function that replaces an element in a list at a specific position without modifying the original list.<br>
**Requirement:** <br>
- Prototype: def new_in_list(my_list, idx, element):
- If idx is negative, the function should return a copy of the original list
- If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
- You are not allowed to import any module
- You are not allowed to use try/excepts


### 5. Can you C me now?

**File:** [5-no_c.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/5-no_c.py)<br>
**Description:** Write a function that removes all characters c and C from a string.<br>
**Requirement:** <br>
- Prototype: def no_c(my_string):
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use str.replace()

### 6. Lists of lists = Matrix

**File:** [6-print_matrix_integer.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/6-print_matrix_integer.py)<br>
**Description:** Write a function that prints a matrix of integers.<br>
**Requirement:** <br>
- Prototype: def print_matrix_integer(matrix=[[]]):
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers
- example
```bash
1 2 3$
4 5 6$
7 8 9$
```

### 7. Tuples addition

**File:** [7-add_tuple.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/7-add_tuple.py)<br>
**Description:** Write a function that adds 2 tuples.<br>
**Requirement:** <br>
- Prototype: def add_tuple(tuple_a=(), tuple_b=()):
- Returns a tuple with 2 integers:
-- The first element should be the addition of the first element of each argument
-- The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value 0 for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers


### 8. More returns!

**File:** [8-multiple_returns.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/8-multiple_returns.py)<br>
**Description:** Write a function that returns a tuple with the length of a string and its first character.<br>
**Requirement:** <br>
- Prototype: def multiple_returns(sentence):
- If the sentence is empty, the first character should be equal to None
- You are not allowed to import any module


### 9. Find the max

**File:** [9-max_integer.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/9-max_integer.py)<br>
**Description:** Write a function that finds the biggest integer of a list.<br>
**Requirement:** <br>
- Prototype: def max_integer(my_list=[]):
- If the list is empty, return None
- You can assume that the list only contains integers
- You are not allowed to import any module
- You are not allowed to use the builtin max()

### 10. Only by 2

**File:** [10-divisible_by_2.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/10-divisible_by_2.py)<br>
**Description:** Write a function that finds all multiples of 2 in a list.<br>
**Requirement:** <br>
- Prototype: def divisible_by_2(my_list=[]):
- Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list
- You are not allowed to import any module

### 11. Delete at

**File:** [11-delete_at.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/11-delete_at.py)<br>
**Description:** Write a function that deletes the item at a specific position in a list.<br>
**Requirement:** <br>
- Prototype: def delete_at(my_list=[], idx=0):
- If idx is negative or out of range, nothing change (returns the same list)
- You are not allowed to use pop()
- You are not allowed to import any module


### 12. Switch

**File:** [12-switch.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-data_structures/12-switch.py)<br>
**Description:** Complete the source code in order to switch value of a and b.<br>
**Requirement:** <br>
- You can find the source code
```python
#!/usr/bin/python3
a = 89
b = 10
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("a={:d} - b={:d}".format(a, b))
```
- Your code should be inserted where the comment is (line 4)
- Your program should be exactly 5 lines long


## Tests
This project includes a comprehensive suite of tests to ensure the reliability and functionality of the codebase. These tests cover various aspects, including unit tests.<br>

### [Running Tests](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/tree/main/python-hello_world/tests)
 There are two ways to run the tests.

- 1, Run the following command in the root dir.<br>
   `python3 <path of the test> ` ex) `python3 tests/test0.py`
- 2, Run with Makefile command.
  This project includes Makefile to automate testing processes.<br>
  `make` command run the all test files in the tests directory.<br>
  `make filename without py` such as `make test4` run the specific test file.<br>
- **Install make:** install make with `apt-get install make` (if necessary)