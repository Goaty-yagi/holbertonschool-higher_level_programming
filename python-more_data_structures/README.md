# Python - More Data Structures: Set, Dictionary

This Python repository focuses on exploring more advanced data structures, specifically sets and dictionaries. It provides code examples and explanations how to effectively use sets and dictionaries in Python programming. 

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)
## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/LEANING_OBJECTIVES.md) file for details.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Practice Exercises

### 0. Squared simple

**File:** [0-square_matrix_simple.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/0-square_matrix_simple.py)<br>
**Description:** Write a function that computes the square value of all integers of a matrix.<br>
**Requirement:** <br>
- Prototype: def square_matrix_simple(matrix=[]):
- matrix is a 2 dimensional array
- Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, map, etc.


### 1. Search and replace

**File:** [1-search_replace.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/1-search_replace.py)<br>
**Description:** Write a function that replaces all occurrences of an element by another in a new list.<br>
**Requirement:** <br>
- Prototype: def search_replace(my_list, search, replace):
- my_list is the initial list
- search is the element to replace in the list
- replace is the new element
- You are not allowed to import any module

### 2. Unique addition

**File:** [2-uniq_add.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/2-uniq_add.py)<br>
**Description:** Write a function that adds all unique integers in a list (only once for each integer).<br>
**Requirement:** <br>
- Prototype: def uniq_add(my_list=[]):
- You are not allowed to import any module

### 3. Present in both

**File:** [3-common_elements.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/3-common_elements.py)<br>
**Description:** Write a function that returns a set of common elements in two sets.<br>
**Requirement:** <br>
- Prototype: def common_elements(set_1, set_2):
- You are not allowed to import any module


### 4. Only differents

**File:** [4-only_diff_elements.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/4-only_diff_elements.py)<br>
**Description:** Write a function that returns a set of all elements present in only one set.<br>
**Requirement:** <br>
- Prototype: def only_diff_elements(set_1, set_2):
- You are not allowed to import any module


### 5. Number of keys

**File:** [5-number_keys.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/5-number_keys.py)<br>
**Description:** Write a function that returns the number of keys in a dictionary.<br>
**Requirement:** <br>
- Prototype: def number_keys(a_dictionary):
- You are not allowed to import any module


### 6. Print sorted dictionary

**File:** [6-print_sorted_dictionary.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/6-print_sorted_dictionary.py)<br>
**Description:** Write a function that prints a dictionary by ordered keys.<br>
**Requirement:** <br>
- Prototype: def print_sorted_dictionary(a_dictionary):
- You can assume that all keys are strings
- Keys should be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
- You are not allowed to import any module


### 7. Update dictionary

**File:** [7-update_dictionary.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/7-update_dictionary.py)<br>
**Description:** Write a function that prints a dictionary by ordered keys.<br>
**Requirement:** <br>
- Prototype: def update_dictionary(a_dictionary, key, value):
- key argument will be always a string
- value argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
- You are not allowed to import any module


### 8. Simple delete by key

**File:** [8-simple_delete.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/8-simple_delete.py)<br>
**Description:** Write a function that deletes a key in a dictionary.<br>
**Requirement:** <br>
- Prototype: def simple_delete(a_dictionary, key=""):
- key argument will be always a string
- If a key doesn’t exist, the dictionary won’t change
- You are not allowed to import any module


### 9. Multiply by 2

**File:** [9-multiply_by_2.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/9-multiply_by_2.py)<br>
**Description:** Write a function that returns a new dictionary with all values multiplied by 2.<br>
**Requirement:** <br>
- Prototype: def multiply_by_2(a_dictionary):
- You can assume that all values are only integers
- Returns a new dictionary
- You are not allowed to import any module


### 10. Best score

**File:** [10-best_score.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/10-best_score.py)<br>
**Description:** Write a function that returns a key with the biggest integer value.<br>
**Requirement:** <br>
- Prototype: def best_score(a_dictionary):
- You can assume that all values are only integers
- If no score found, return None
- You can assume all students have a different score
- You are not allowed to import any module


### 11. Multiply by using map

**File:** [11-multiply_list_map.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/11-multiply_list_map.py)<br>
**Description:** Write a function that returns a key with the biggest integer value.<br>
**Requirement:** <br>
- Prototype: def multiply_list_map(my_list=[], number=0):
- Returns a new list:
Same length as my_list
Each value should be multiplied by number
- Initial list should not be modified
- You are not allowed to import any module
- You have to use map
- Your file should be max 3 lines
