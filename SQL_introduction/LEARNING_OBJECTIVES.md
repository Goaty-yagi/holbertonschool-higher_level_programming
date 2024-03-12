# Learning Objectives

- [What’s a database](#What-s-a-database)
- [What’s a relational database](#What’s-a-relational-database)
- [What does SQL stand for](#What-does-SQL-stand-for)
- [What’s MySQL](#What’s-MySQL)
- [How to create a database in MySQL](#How-to-create-a-database-in-MySQL)
- [What does DDL and DML stand for](#What-does-DDL-and-DML-stand-for)
- [How to CREATE or ALTER a table](#How-to-CREATE-or-ALTER-a-table)
- [How to SELECT data from a table](#How-to-SELECT-data-from-a-table)
- [How to INSERT, UPDATE or DELETE data](#How-to-INSERT,-UPDATE-or-DELETE-data)
- [What are subqueries](#What-are-subqueries)
- [How to use MySQL functions](#How-to-use-MySQL-functions)

## What’s a database
A database is a structured collection of data that is organized and stored in a way that allows for efficient retrieval, management, and manipulation of information

## What’s a relational database
<img src="https://static.javatpoint.com/dbms/images/what-is-rdbms.png">
A relational database is a type of database that organizes and stores data in tables with a predefined structure. The relational database model was introduced by Edgar Codd in 1970 and is based on the principles of the relational algebra. In a relational database:

- Tables:
Data is organized into tables, each of which represents a specific entity or concept. Tables consist of rows and columns, where each row corresponds to a record (data entry) and each column represents an attribute of that record.

- Records:
Each row in a table is a record, and it contains a complete set of data for a particular entity. For example, in a "users" table, each row might represent information about a specific user.

- Columns:
Columns define the attributes or fields of the data stored in a table. Each column has a specific data type, such as text, number, or date, and represents a particular characteristic of the records.

- Keys:
Relational databases use keys to establish relationships between tables. The primary key uniquely identifies each record in a table, and a foreign key links a record in one table to a record in another table.

- Relationships:
Relationships between tables are established through common fields (usually keys). This allows for efficient organization of data and the ability to retrieve related information across multiple tables.

## What does SQL stand for
Structured Query Language
- Relational databases use SQL to define and manipulate the data. SQL provides a standardized way to create, retrieve, update, and delete data in the database.

## What’s MySQL
MySQL is an open-source relational database management system (RDBMS) that is widely used for managing and organizing structured data.

## How to create a database in MySQL
### Install MySql
`apt install mysql-server`
### start MySql
`service mysql start`
### Check status
`service mysql status`
### Start Sql shell

## What does DDL and DML stand for

### DDL (Data Definition Language)
- Definition:
DDL is a subset of SQL that deals with the structure and definition of the database objects.
- Purpose:
DDL statements are used to define, modify, and delete database objects such as tables, indexes, and schemas.
- Examples:
 -- CREATE TABLE: Defines a new table.
 -- ALTER TABLE: Modifies the structure of an existing table.
 -- DROP TABLE: Deletes a table.
 -- CREATE INDEX: Defines an index on one or more columns.

### DML (Data Manipulation Language)
- Definition:
DML is another subset of SQL that focuses on manipulating the data stored in the database.
- Purpose:
DML statements are used to insert, update, retrieve, and delete data in the database.
- Examples:
 -- SELECT: Retrieves data from one or more tables.
 -- INSERT INTO: Adds new records to a table.
 -- UPDATE: Modifies existing records in a table.
 -- DELETE FROM: Removes records from a table.

In summary, DDL deals with the structure and definition of the database, while DML deals with the manipulation of the actual data within the database. 

## How to CREATE or ALTER a table
### Create
```sql
CREATE TABLE table_name (
    column1 datatype1,
    column2 datatype2,
    ...
    columnN datatypeN
);

-- examle
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    birthdate DATE
);

-- * VARCHAR (Variable Character)

```

### ALTER
```sql
ALTER TABLE table_name
ADD COLUMN new_column_name datatype;

-- example

-- add column
ALTER TABLE table_name
ADD COLUMN new_column_name datatype;

ALTER TABLE users
ADD COLUMN phone_number VARCHAR(20);

-- Modify a column:
ALTER TABLE table_name
MODIFY COLUMN column_name new_datatype;

ALTER TABLE users
MODIFY COLUMN email VARCHAR(150);

-- Drop a column:
ALTER TABLE table_name
DROP COLUMN column_name;

ALTER TABLE users
DROP COLUMN phone_number;


```
## How to SELECT data from a table
```sql
SELECT column1, column2, ...
FROM table_name;

-- select all
SELECT *
FROM table_name;

-- with conditiopn

SELECT column1, column2, ...
FROM table_name
WHERE condition;

SELECT name, salary
FROM employees
WHERE salary > 50000;


```
## How to INSERT, UPDATE or DELETE data
### Insert
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);

-- example
INSERT INTO employees (name, age, salary)
VALUES ('John Doe', 30, 60000);

```
### Update
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

-- example
UPDATE employees
SET salary = 65000
WHERE name = 'John Doe';

```
### Delete
```sql
DELETE FROM table_name
WHERE condition;

-- example
DELETE FROM employees
WHERE name = 'John Doe';
```
## What are subqueries
Subqueries, also known as nested queries or inner queries, are queries nested within another SQL statement. 
## How to use MySQL functions
MySQL provides a wide range of built-in functions that you can use to perform various operations on data. These functions can be categorized into different types.

###  String Functions
```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;

```

### 2. Numeric Functions
```sql
SELECT ABS(-10) AS absolute_value;
```

### 3. Date and Time Functions
```sql
SELECT DATE_FORMAT(birth_date, '%Y-%m-%d') AS formatted_birth_date
FROM employees;

```

### 4. Aggregate Functions
```sql
SELECT COUNT(*) AS total_employees
FROM employees;

```

### 5. Control Flow Functions:
```sql
SELECT IF(salary > 50000, 'High Salary', 'Low Salary') AS salary_category
FROM employees;

```
### 6. Mathematical Functions
```sql
SELECT SQRT(25) AS square_root;

```