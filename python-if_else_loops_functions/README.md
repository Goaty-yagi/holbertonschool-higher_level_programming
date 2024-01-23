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


