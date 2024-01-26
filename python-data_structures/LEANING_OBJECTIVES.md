# Learning Objectives

- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the del statement and how to use it

## 1, What are lists and how to use them

In Python, a list is a built-in data structure that is used to store an ordered collection of items. Lists are versatile and can contain elements of different data types. They are mutable, which means you can modify their contents by adding, removing, or updating elements.

- Creating Lists:
  You can create a list by enclosing a comma-separated sequence of items within square brackets []. Here are some examples:

```python
# Empty list
empty_list = []

# List with integers
numbers = [1, 2, 3, 4, 5]

# List with mixed data types
mixed_list = [1, "two", 3.0, [4, 5]]

# List comprehension
squares = [x**2 for x in range(1, 6)]

# Not recommended
list = list()

```

- Accessing Elements:
  Elements in a list are indexed, and you can access them using square brackets. Python uses zero-based indexing, so the first element is at index 0.

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[0])  # Output: 1
print(numbers[2])  # Output: 3
print(numbers[-1])  # Output: 5 (negative index counts from the end)

```

- Modifying Lists:
  Lists are mutable, so you can modify them by assigning new values to specific indices or using list methods.

```python
numbers = [1, 2, 3, 4, 5]

# Update an element
numbers[2] = 10

# Add elements
numbers.append(6)       # Add 6 to the end
numbers.insert(2, 7)    # Insert 7 at index 2

# Remove elements
numbers.remove(4)       # Remove the first occurrence of 4
popped_element = numbers.pop()  # Remove and return the last element

```


## 2, What are the differences and similarities between strings and lists

Strings and lists are both data structures in Python, but they have distinct characteristics. Here are some differences and similarities between strings and lists:

### Differences:
- Mutability:
Strings are immutable, meaning you cannot modify individual characters in a string. Once a string is created, you cannot change its characters.
Lists are mutable, allowing you to modify, add, or remove elements after the list is created.
- Character vs. Element:
In a string, each element represents a character. Strings are sequences of characters.
In a list, each element can be of any data type, and a list can contain a mix of different data types.
- Syntax for Creation:
Strings are created using single or double quotes, such as my_string = "Hello".
Lists are created using square brackets, such as my_list = [1, 2, 3].

### Similarities:
- Indexing:
Both strings and lists support indexing, allowing you to access individual elements using square brackets and indices.

- Slicing:
Both strings and lists support slicing, allowing you to extract sub-sequences.

- Iteration:
You can iterate over both strings and lists using loops.

- Length:
Both strings and lists have a len() function that returns the number of elements.

## 3, What are the most common methods of lists and how to use them
Lists have several built-in methods for common operations. Some examples include:

```python
numbers = [1, 2, 3, 4, 5]

numbers.append(6)   # Add an element to the end
numbers.extend([7, 8, 9])  # Extend the list with another iterable
numbers.sort()      # Sort the list in ascending order
numbers.reverse()   # Reverse the order of elements

```

## 4, How to use lists as stacks and queues
- Using Lists as Stacks (LIFO):
A stack follows the Last-In, First-Out (LIFO) principle, meaning the last element added is the first one to be removed. Python lists naturally support stack operations with methods like append() and pop().

```python
# Using a list as a stack
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Pop elements from the stack
pop1 = stack.pop()
pop2 = stack.pop()

print(pop1)  # Output: 3
print(pop2)  # Output: 2

```

Using Lists as Queues (FIFO):
A queue follows the First-In, First-Out (FIFO) principle, meaning the first element added is the first one to be removed. While lists are not the most efficient data structure for queue operations, you can use collections.deque for more efficient queue operations.

```python
from collections import deque

# Using a list as a queue
queue = deque()

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue elements
dequeue1 = queue.popleft()
dequeue2 = queue.popleft()

print(dequeue1)  # Output: 1
print(dequeue2)  # Output: 2

```

or just use pop

```python
# Using a list as a simple FIFO queue
fifo_queue = []

# Enqueue elements
fifo_queue.append(1)
fifo_queue.append(2)
fifo_queue.append(3)

# Dequeue elements
dequeue1 = fifo_queue.pop(0)
dequeue2 = fifo_queue.pop(0)

print(dequeue1)  # Output: 1
print(dequeue2)  # Output: 2

```

## 5, What are list comprehensions and how to use them
See the above example in "1, What are lists and how to use them"

## 6, What are tuples and how to use them
In Python, a tuple is a collection of ordered and immutable elements. Tuples are similar to lists, but the key difference is that once a tuple is created, its elements cannot be modified, added, or removed. Tuples are defined using parentheses ().

- Creating Tuples:
You can create tuples using parentheses with or without elements. Here are some examples:
```python
# Empty tuple
empty_tuple = ()

# Tuple with integers
integer_tuple = (1, 2, 3)

# Tuple with mixed data types
mixed_tuple = (1, "two", 3.0, [4, 5])

# Tuple with a single element (needs a trailing comma)
single_element_tuple = (42,)

# Tuple comprehension to create a tuple of squares
squares_tuple = tuple(x**2 for x in range(1, 6))

```

- Accessing Elements:
Elements in a tuple are accessed using square brackets and indices, just like in lists:
```python
my_tuple = (1, 2, 3, "four")

print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
print(my_tuple[-1])  # Output: 'four' (negative index counts from the end)

```

- Immutability:
Tuples are immutable, meaning you cannot modify their elements or their size once they are created. The following code would result in an error:

```python
my_tuple = (1, 2, 3)
# Attempting to modify a tuple (will raise an error)
# my_tuple[0] = 10
# Attempting to add an element to a tuple (will raise an error)
# my_tuple.append(4)

```

- Tuple Methods:
Tuples have fewer built-in methods compared to lists due to their immutability. Some common methods include count() and index():

```python
my_tuple = (1, 2, 2, 3, 4)

# Count occurrences of a value
count_of_2 = my_tuple.count(2)
print(count_of_2)  # Output: 2

# Find the index of a value
index_of_3 = my_tuple.index(3)
print(index_of_3)  # Output: 3

```

## 7, When to use tuples versus lists

- Immutability is Desired:
Tuples are immutable, meaning their elements cannot be modified after creation. If you need a collection of elements that should remain constant throughout the program, use a tuple.

- Data Integrity is Important:
Since tuples are immutable, they provide a level of data integrity. Once a tuple is created, you can trust that its elements won't be changed accidentally or intentionally.

- Performance is Critical:
Due to their immutability, tuples can be more memory-efficient and slightly faster than lists in certain operations. If performance is critical, especially in scenarios with large datasets, consider using tuples.

- Used as Dictionary Keys:
Tuples are hashable and can be used as keys in dictionaries, whereas lists cannot. This makes tuples suitable for situations where you need an immutable key.

## 8, What is a sequence
In Python, a sequence is an ordered collection of elements where each element is identified by an index or a key.
such as lists, tuples and strings.

## 9, What is tuple packing
Tuple packing is a concept in Python where multiple values are assigned to a single tuple. When you group multiple values together, separated by commas, Python automatically packs them into a tuple. This happens implicitly, and you don't need to explicitly create a tuple.

```python
# Tuple packing
coordinates = 3.14, 2.71

# The values 3.14 and 2.71 are packed into a tuple
print(coordinates)  # Output: (3.14, 2.71)

```
## 10, What is sequence unpacking

Sequence unpacking is the process of extracting values from a sequence (such as a tuple, list, or string) and assigning them to multiple variables in a single statement. This is the opposite of sequence packing, where multiple values are grouped into a sequence. 

- Exapmle with tuple
```python
# Tuple unpacking
coordinates = (3.14, 2.71)
x, y = coordinates

print(x)  # Output: 3.14
print(y)  # Output: 2.71

```

- Exapmle with list
```python
# List unpacking
numbers = [1, 2, 3]
a, b, c = numbers

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

```

- Exapmle with string
```python
# String unpacking
word = "Python"
first, second, *rest = word

print(first)  # Output: P
print(second)  # Output: y
print(rest)    # Output: ['t', 'h', 'o', 'n']

```
## 11, What is the del statement and how to use it
The del statement in Python is used to delete items from a collection (such as a list, tuple, or dictionary) or to delete entire variables.

### Deleting Items from a Collection:
 - List
 ```python
 my_list = [1, 2, 3, 4, 5]

# Delete the item at index 2
del my_list[2]
print(my_list)  # Output: [1, 2, 4, 5]

 ```
 
 - Dictionaries:
 ```python
 my_dict = {'a': 1, 'b': 2, 'c': 3}

# Delete the key-value pair with key 'b'
del my_dict['b']
print(my_dict)  # Output: {'a': 1, 'c': 3}

 ```

 ### Deleting Variables:
 ```python
 my_variable = 42

# Delete the variable
del my_variable

# Raises NameError because the variable is no longer defined
# print(my_variable)

```

### Deleting Slices:
```python
my_list = [1, 2, 3, 4, 5]

# Delete a slice of the list
del my_list[1:3]
print(my_list)  # Output: [1, 4, 5]

```

