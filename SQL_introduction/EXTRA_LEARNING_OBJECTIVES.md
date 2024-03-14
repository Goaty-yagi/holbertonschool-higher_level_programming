# Extra Learning Objectives


What is default character set?
How to check defaut character set?
How to modify character set
What is Collation in SQL
What is default Collation
Howo to see Collation set
How to modify Collation set


## What is default character set?
The default character set in MySQL depends on various factors, including the MySQL server configuration, the default character set defined at the server level, and the default character set defined at the database level.
## How to check defaut character set?
```sql
SHOW VARIABLES LIKE 'character_set_%';

-- Shows like this
Variable_name   Value
character_set_client    utf8mb4
character_set_connection        utf8mb4
character_set_database  utf8mb4
character_set_filesystem        binary
character_set_results   utf8mb4
character_set_server    utf8mb4
character_set_system    utf8mb3
character_sets_dir      /usr/share/mysql/charsets/
```
## How to modify character set
when you change the character set of a database, table, or column in MySQL, it's often recommended to also update the collation to be compatible with the new character set.

### Database Level
```sql
ALTER DATABASE <your db name>
CHARACTER SET <charset name ex utf8mb4>
COLLATE utf8mb4_unicode_ci;
```

### Table Level
```sql
ALTER TABLE my_table
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

### Column Level
```sql
ALTER TABLE my_table
MODIFY name VARCHAR(255)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

it's important to note that altering the character set of a database in MySQL doesn't automatically convert the character set of existing tables and columns within that database.

## What is Collation in SQL
collation refers to the set of rules used to compare and sort character data in a database. It defines how characters are compared and sorted in various operations such as querying, sorting, and indexing text data.<br>

Collation rules govern several aspects of character comparison, including:<br>

### Case Sensitivity:
Collation rules determine whether character comparisons are case-sensitive or case-insensitive. For example, in a case-insensitive collation, 'A' and 'a' are considered equal.

### Accent Sensitivity:
Collation rules define how accents and diacritical marks are treated in character comparisons. For instance, in an accent-insensitive collation, characters with accents are treated the same as their unaccented counterparts.

### Character Equivalence:
Collation rules specify the equivalence of certain characters, such as treating 'ß' (German sharp S) as equivalent to 'ss'.

### Sorting Order:
Collation rules define the order in which characters are sorted. This includes the sorting of characters from different languages and scripts according to the language-specific sorting rules.

<br>

Collation is an essential aspect of database operations, especially when dealing with multilingual data or databases that need to support different language-specific sorting orders. By choosing an appropriate collation for a database, table, or column, you can ensure that character data is compared and sorted according to the desired rules.

In SQL, collation can be specified at different levels:

### Database Level:
Collation can be specified for the entire database, affecting all character data within that database.

### Table Level:
Collation can be specified for individual tables, allowing different collations within the same database.

### Column Level:
Collation can be specified for individual columns within a table, allowing fine-grained control over character comparison and sorting for specific columns.

## What is default Collation
The default collation in SQL is the collation used when no specific collation is explicitly specified for a database, table, or column. The default collation is determined by the default settings of the database management system (DBMS) being used.

In MySQL, for example, the default collation for newly created databases, tables, and columns is determined by the server configuration. Typically, the default collation for MySQL is utf8mb4_general_ci or utf8mb4_unicode_ci for UTF-8 encoded data, depending on the server configuration.

## Howo to see Collation set
```sql
SHOW VARIABLES LIKE 'collation_%';
```
Looks like this
```bash
Variable_name   Value
collation_connection    utf8mb4_0900_ai_ci
collation_database      utf8mb4_0900_ai_ci
collation_server        utf8mb4_0900_ai_ci
```
## How to modify Collation set

### Database level
```sql
ALTER DATABASE database_name 
COLLATE collation_name;
```

### Table Level
```sql
ALTER TABLE my_table
COLLATE utf8mb4_unicode_ci;
```

### Column Level
```sql
ALTER TABLE my_table
MODIFY name VARCHAR(255)
COLLATE utf8mb4_unicode_ci;
```
