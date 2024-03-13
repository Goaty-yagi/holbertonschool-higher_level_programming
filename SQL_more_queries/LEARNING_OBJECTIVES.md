# Learning Objectives

- [How to create a new MySQL user](#How-to-create-a-new-MySQL-user)
- [How to manage privileges for a user to a database or table](#How-t-manage-privileges-for-a-user-to-a-database-or-table)
- [What’s a PRIMARY KEY](#What’s-a-PRIMARY-KEY)
- [What’s a FOREIGN KEY](#What’s-a-FOREIGN-KEY)
- [How to use NOT NULL and UNIQUE constraints](#How-to-use-NOT-NULL-and-UNIQUE-constraints)
- [How to retrieve datas from multiple tables in one request](#How-to-retrieve-datas-from-multiple-tables-in-one-request)
- [What are subqueries](#What-are-subqueries)
- [What are JOIN and UNION](#What-are-JOIN-and-UNION)

## How to create a new MySQL user
`CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';`
## How to manage privileges for a user to a database or table
`GRANT PRIVILEGE ON database.table TO 'username'@'host';`
Example
`GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;`
## What’s a PRIMARY KEY
Uniquely identifies each record in a table.
```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

```
## What’s a FOREIGN KEY
a column or a set of columns in a table that refers to the PRIMARY KEY or a UNIQUE KEY of another table. 
```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

```
## How to use NOT NULL and UNIQUE constraints
Set attributes when create a table.
```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

```
## How to retrieve datas from multiple tables in one request
You can use the JOIN operation.
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240313%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240313T041547Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f128df2343eca32ecdeab073fbf5a18d46bdfdcc6e586600ea63a9def552760c">


## What are subqueries
inner query or nested query,
## What are JOIN and UNION
### JOIN
JOIN operation is used to combine rows from two or more tables based on a related column between them. The related column is typically a primary key in one table that matches a foreign key in another table.

```sql
SELECT columns
FROM table1
INNER JOIN table2 ON table1.column = table2.column;

-- excludes unmatched rows from both tables,
```
### LEFT JOIN 

### UNION

The UNION operator is used to combine the results of two or more SELECT statements into a single result set. The following conditions must be met for a UNION:

- The SELECT statements must have the same number of columns.
- The corresponding columns in the SELECT statements must have compatible data types.

```sql
SELECT employee_id, employee_name FROM employees
UNION
SELECT vendor_id, vendor_name FROM vendors;

```
In this example, the UNION operator is used to combine the results of two SELECT statements, each retrieving data from different tables. The result set contains unique rows from both SELECT statements.

It's important to note that UNION removes duplicate rows from the result set. If you want to include duplicate rows, you can use UNION ALL.