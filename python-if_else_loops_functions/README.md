# Python - if/else, loops, functions

This repository is to learn and practice fundamental Python concepts, specifically focusing on if/else statements, loops, and functions.

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
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Practice Exercises

### 0. Positive anything is better than negative nothing

**File:** [0-positive_or_negative.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/0-positive_or_negative.py)<br>
**Description:** This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.<br>
**Requirement:**<br> 
- You can find the source
  ```python
     #!/usr/bin/python3
     import random
     number = random.randint(-10, 10)
     # YOUR CODE HERE
  ```
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random. randint do. Please do not touch this code
- The output of the program should be:
- The number, followed by
-- if the number is greater than 0: is positive
--- if the number is 0: is zero
--- if the number is less than 0: is negative
-- followed by a new line

### 1. The last digit

**File:** [1-last_digit.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/1-last_digit.py)<br>
**Description:** This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.<br>
**Requirement:** <br>
- You can find the source
  ```python
     #!/usr/bin/python3
     import random
     number = random.randint(-10000, 10000)
     # YOUR CODE HERE
  ```
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
- The output of the program should be:
-- The string Last digit of, followed by
-- the number, followed by
-- the string is, followed by the last digit of number, followed by
--- if the last digit is greater than 5: the string and is greater than 5
--- if the last digit is 0: the string and is 0
--- if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
-- followed by a new line

### 2. Alphabet game

**File:** [2-print_alphabet.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/2-print_alphabet.py)<br>
**Description:** Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.<br>
**Requirement:** <br>
- Use only one print function with string format
- Use only one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module


### 3. When I was having that alphabet soup, I never thought that it would pay off

**File:** [3-print_alphabt.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/3-print_alphabt.py)<br>
**Description:** Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.<br>
**Requirement:** <br>
- Print all the letters except q and e
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module


### 4. Hexadecimal printing

**File:** [4-print_hexa.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/4-print_hexa.py)<br>
**Description:** Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal.<br>
**Requirement:** <br>
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module


### 5. 00...99

**File:** [5-print_comb2.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/5-print_comb2.py)<br>
**Description:** Write a program that prints numbers from 0 to 99.<br>
**Requirement:** <br>
- Numbers must be separated by "," ,followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module


### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need

**File:** [6-print_comb3.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/6-print_comb3.py)<br>
**Description:** Write a program that prints all possible different combinations of two digits.<br>
**Requirement:** <br>
- Numbers must be separated by "," ,followed by a space
- The two digits must be different
- 01 and 10 are considered the same combination of the two digits 0 and 1
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 print functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module


### 7. islower

**File:** [7-islower.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/7-islower.py)<br>
**Description:** Write a function that checks for lowercase character.<br>
**Requirement:** <br>
- Prototype: def islower(c):
- Returns True if c is lowercase
- Returns False otherwise
- You are not allowed to import any module
- You are not allowed to use str.upper() and str.isupper()


### 8. To uppercase

**File:** [8-uppercase.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/8-uppercase.py)<br>
**Description:** Write a function that checks for lowercase character.<br>
**Requirement:** <br>
- Prototype: def uppercase(str):
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use str.upper() and str.isupper()


### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important

**File:** [9-print_last_digit.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/9-print_last_digit.py)<br>
**Description:** Write a function that checks for lowercase character.<br>
**Requirement:** <br>
- Prototype: def print_last_digit(number):
- Returns the value of the last digit
- You are not allowed to import any module

### 10. a + b

**File:** [10-add.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/10-add.py)<br>
**Description:** Write a function that adds two integers and returns the result.<br>
**Requirement:** <br>
- Prototype: def add(a, b):
- Returns the value of a + b
- You are not allowed to import any module

### 11. a ^ b

**File:** [11-pow.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/11-pow.py)<br>
**Description:** Write a function that computes a to the power of b and return the value.<br>
**Requirement:** <br>
- Prototype: def pow(a, b):
- Returns the value of a ^ b
- You are not allowed to import any module


### 12. Fizz Buzz

**File:** [12-fizzbuzz.py](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/python-if_else_loops_functions/12-fizzbuzz.py)<br>
**Description:** Write a function that prints the numbers from 1 to 100 separated by a space.<br>
**Requirement:** <br>
- For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
- For numbers which are multiples of both three and five print FizzBuzz.
- Prototype: def fizzbuzz():
- Each element should be followed by a space
- You are not allowed to import any module


## Tests
This project includes a comprehensive suite of tests to ensure the reliability and functionality of the codebase. These tests cover various aspects, including unit tests.<br>

### [Running Tests](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/tree/main/python-if_else_loops_functions/tests)
 There are two ways to run the tests.

- 1, Run the following command in the root dir.<br>
   `python3 <path of the test> ` ex) `python3 tests/test0.py`
- 2, Run with Makefile command.
  This project includes Makefile to automate testing processes.<br>
  `make` command run the all test files in the tests directory.<br>
  `make filename without py` such as `make test4` run the specific test file.<br>
- **Install make:** install make with `apt-get install make` (if necessary)


