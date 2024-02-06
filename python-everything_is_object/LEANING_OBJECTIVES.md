# Learning Objectives

- [What is the difference between immutable object and mutable object](#what-is-the-difference-between-immutable-object-and-mutable-object)
- [What is a reference](#what-is-a-reference)
- [What is an assignment](#what-is-an-assignment)
- [What is an alias](#what-is-an-alias)
- [How to know if two variables are identical](#how-to-know-if-two-variables-are-identical)
- [How to know if two variables are linked to the same object](#how-to-know-if-two-variables-are-linked-to-the-same-object)
- [How to display the variable identifier (which is the memory address in the CPython implementation)](#how-to-display-the-variable-identifier(which is the memory address in the CPython implementation))
- [What is mutable and immutable](#what-is-mutable-and-immutable)
- [What are the built-in mutable types](#what-are-the-built-in-mutable-types)
- [What are the built-in immutable types](#what-are-the-built-in-immutable-types)
- [How does Python pass variables to functions](#how-does-python-pass-variables-to-functions)

## 1, What is the difference between immutable object and mutable object
The main difference between immutable objects and mutable objects in programming lies in whether their state (i.e., their data) can be modified after they are created.
## 2, What is a reference
A reference is a value that refers to an object in memory. When you create a variable and assign it a value, that variable holds a reference to the object in memory rather than the actual object itself. This reference allows you to access and manipulate the object's data.
### Variables as References:
- Variables in Python are essentially names or labels that refer to objects in memory.
- When you create a variable and assign it a value, the variable becomes a reference to the object.
```python
x = 42  # x is a reference to the integer object 42

```

### Mutability and Immutability:

- For mutable objects (e.g., lists, dictionaries), the reference allows modification of the object's content in place.
- For immutable objects (e.g., integers, strings), any operation that seems to modify the object actually creates a new object, and the reference is updated to point to the new object.
```python
# Mutable object (list)
my_list = [1, 2, 3]
my_reference = my_list  # Both my_list and my_reference point to the same list
my_list.append(4)      # Modifies the list, affects both references
print(my_reference)    # Output: [1, 2, 3, 4]

# Immutable object (string)
my_str = "Hello"
my_reference = my_str   # Both my_str and my_reference point to the same string
my_str = my_str.upper()  # Creates a new string, my_str now points to the new string
print(my_reference)      # Output: Hello

```

### Passing by Object Reference:

- When passing arguments to functions in Python, the reference to the object is passed, not a copy of the object itself.
- This means changes made to mutable objects within a function can affect the original object outside the function.
```python
def modify_list(lst):
    lst.append(42)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 42]

def assign_value(n, v):
    n = v # reassign in function doesn't change the original

    # This works
    n.clear()  # Clears the contents of the list pointed to by n
    n.extend(v)  # Appends the elements of v to the list pointed to by n

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1) # Output: [1, 2, 3] 

```
## 3, What is an assignment
An assignment is a statement that associates a value with a variable or a name. It is the process of binding a name to an object.
```python
variable = value

x = 42  # Assigning the value 42 to the variable x
name = "John"  # Assigning the string "John" to the variable name
my_list = [1, 2, 3]  # Assigning a list to the variable my_list

my_list = [1, 2, 3, 4]

# Assigning a new value to a specific index
my_list[1] = 5

print(my_list)
# Output: [1, 5, 3, 4]

```

## 4, What is an alias
An alias typically refers to an alternative name assigned to an existing variable, module, function, or class. It allows you to refer to the same entity by different names within the scope of your code. 
- Variable Alias:
```python
original_name = 42
alias_name = original_name  # alias_name is an alias for original_name

```

- Function Alias:
```python
def original_function():
    print("Hello, World!")

alias_function = original_function  # alias_function is an alias for original_function

```
- Module Alias:
```python
import math as m  # m is an alias for the math module

```
- Class Alias:
```python
class OriginalClass:
    pass

AliasClass = OriginalClass  # AliasClass is an alias for OriginalClass

```

- Namespace Alias:
```python
import pandas as pd  # pd is an alias for the pandas module

```
## 5, How to know if two variables are identical
You can use the is operator to check if two variables refer to the same object in memory. This is different from the == operator, which checks if the values of two variables are equal.
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # Output: False (different objects in memory)
print(a == b)  # Output: True (values are equal)

```
In CPython (the standard implementation of Python), small integers (typically in the range of -5 to 256) are cached and reused for performance optimization. 
## 6, How to know if two variables are linked to the same object
Same as above
## 7, How to display the variable identifier (which is the memory address in the CPython implementation)
You can use the id() function to obtain the identity (memory address) of an object. The id() function returns a unique identifier for the object.
```python
x = [1, 2, 3]

# Display the memory address of the variable x
print(id(x))

# Display the variable name and its memory address
print(f"Variable 'x' has memory address: {hex(id(x))}")
```
## 8, What is mutable and immutable
Objects are classified as either mutable or immutable based on whether their state (the values they contain) can be changed after they are created.
## 9, What are the built-in mutable types
- List
- Dictionary
- Set
- Bytearray
```python
my_bytearray = bytearray(b'hello')
my_bytearray[0] = 65  # Mutable: elements can be modified

```
## 10, What are the built-in immutable types
- Integer
- Float
- Tuple
- String
- Frozenset
Frozensets are immutable sets.
```python
my_frozenset = frozenset({1, 2, 3})
# Immutable: elements cannot be modified or added
# my_frozenset.add(4)  # This line would raise an AttributeError

```
## 11, How does Python pass variables to functions
In Python, variables are passed to functions using a mechanism known as "pass by object reference" or "call by object reference." This mechanism involves passing references to objects as arguments to functions rather than the actual values of the objects. It's important to understand this concept to grasp how modifications to variables inside functions affect the original objects.

### Mutable Objects:

- When a mutable object (e.g., a list or dictionary) is passed to a function, the function receives a reference to the same object.
- Modifications made to the object inside the function are reflected outside the function because the reference points to the same object in memory.
```python
def modify_list(my_list):
    my_list.append(4)

original_list = [1, 2, 3]
modify_list(original_list)
print(original_list)  # Output: [1, 2, 3, 4]

```

### Immutable Objects:

- When an immutable object (e.g., an integer or string) is passed to a function, the function receives a copy of the object's value.
- Modifications made to the object inside the function do not affect the original object because the function is working with a separate copy.
```python
def modify_string(my_string):
    my_string += " World"

original_string = "Hello"
modify_string(original_string)
print(original_string)  # Output: Hello

```
### Variable Reassignment:

- If a new value is assigned to the variable inside the function, it does not affect the original variable outside the function.
```python
def reassign_variable(x):
    x = 42

original_value = 10
reassign_variable(original_value)
print(original_value)  # Output: 10

```