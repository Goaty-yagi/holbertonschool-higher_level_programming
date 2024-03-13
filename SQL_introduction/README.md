# SQL - Introduction
This repository serves as a beginner-friendly introduction to SQL.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/LEARNING_OBJECTIVES.md) file for details.

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc


## Practice Exercises

### 0. List databases

**File:** [0-list_databases.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/0-list_databases.sql)<br>
**Description:** Write a script that lists all databases of your MySQL server. <br>


### 1. Create a database

**File:** [1-create_database_if_missing.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/1-create_database_if_missing.sql)<br>
**Description:** Write a script that creates the database hbtn_0c_0 in your MySQL server. <br>
**Requirements:** <br>
- If the database hbtn_0c_0 already exists, your script should not fail
- You are not allowed to use the SELECT or SHOW statements

### 2. Delete a database

**File:** [2-remove_database.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/2-remove_database.sql)<br>
**Description:** Write a script that deletes the database hbtn_0c_0 in your MySQL server. <br>
**Requirements:** <br>
- If the database hbtn_0c_0 doesn’t exist, your script should not fail
- You are not allowed to use the SELECT or SHOW statements

### 3. List tables

**File:** [3-list_tables.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/3-list_tables.sql)<br>
**Description:** Write a script that lists all the tables of a database in your MySQL server. <br>
**Requirements:** <br>
- The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

### 4. First table

**File:** [4-first_table.sql](https://github.com/Goaty-yagi/holbertonschool-higher_level_programming/blob/main/SQL_introduction/4-first_table.sql)<br>
**Description:** Write a script that creates a table called first_table in the current database in your MySQL server. <br>
**Requirements:** <br>
- first_table description:
 -- id INT
 -- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table first_table already exists, your script should not fail
- You are not allowed to use the SELECT or SHOW statements
