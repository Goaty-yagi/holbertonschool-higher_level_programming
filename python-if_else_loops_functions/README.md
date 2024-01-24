# Python - if/else, loops, functions

This repository is to learn and practice fundamental Python concepts, specifically focusing on if/else statements, loops, and functions.

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/LEANING_OBJECTIVES.md) file for details.

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

**File:** `0-positive_or_negative.py`
**Description:** This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.
**Requirement:** 
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

**File:** `1-last_digit.py`
**Description:** This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.
**Requirement:** 
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

**File:** `2-print_alphabet.py`
**Description:** Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
**Requirement:** 
- Use only one print function with string format
- Use only one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module


### 3. When I was having that alphabet soup, I never thought that it would pay off

**File:** `3-print_alphabt.py`
**Description:** Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
**Requirement:** 
- Print all the letters except q and e
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module


