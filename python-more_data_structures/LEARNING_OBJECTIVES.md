# Learning Objectives

- [Why Python programming is awesome](#why-python-programming-is-awesome)
- [What are sets and how to use them](#what-are-sets-and-how-to-use-them)
- [What are the most common methods of set and how to use them](#what-are-the-most-common-methods-of-set-and-how-to-use-them)
- [When to use sets versus lists](#when-to-use-sets-versus-lists)
- [How to iterate into a set](#How-to-iterate-into-a-set)
- [What are dictionaries and how to use them](#what-are-dictionaries-and-how-to-use-them)
- [When to use dictionaries versus lists or sets](#when-to-use-dictionaries-versus-lists-or-sets)
- [What is a key in a dictionary](#what-is-a-key-in-a-dictionary)
- [How to iterate over a dictionary](#how-to-iterate-over-a-dictionary)
- [What is a lambda function](#what-is-a-lambda-function)
- [What are the map, reduce and filter functions](#what-are-the-map,-reduce-and-filter-functions)

## 1, Why Python programming is awesome

Python programming is awesome for a variety of reasons, making it a popular and widely adopted language across different domains.

- Readability and Simplicity:
  Python emphasizes readability and simplicity, making it easy to learn and understand. Its syntax allows developers to express concepts in fewer lines of code compared to other languages, reducing the likelihood of errors and enhancing code clarity.

- High-Level Language:
  Python is a high-level language, abstracting away many low-level details. This makes it easier for developers to focus on solving problems rather than dealing with intricate system-specific nuances.

## 2, What are sets and how to use them

Sets in Python are unordered collections of unique elements. This means that sets do not allow duplicate elements, and the order in which elements are stored is not guaranteed.

- Creating Sets:
  You can create a set by enclosing comma-separated values within curly braces {} or by using the set() constructor with an iterable (like a list or a tuple).

```python
# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}

# Creating a set using the set() constructor with a list
another_set = set([1, 2, 3, 4, 5])

```

- Adding Elements:
  You can add elements to a set using the add() method.

```python
my_set.add(6)

```

- Removing Elements:
  You can remove elements from a set using the remove() method.

```python
my_set.remove(3)

```

- Set Operations:
  Sets support various set operations like union (|), intersection (&), difference (-), and symmetric difference (^).

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of sets
union_set = set1 | set2  # {1, 2, 3, 4, 5}

union_set = set1.union(set2) # {1, 2, 3, 4, 5}

# Intersection of sets
intersection_set = set1 & set2  # {3}

intersection_set = set1.intersection(set2) # {3}

# Difference of sets
difference_set = set1 - set2  # {1, 2}

# Returns a new set containing elements that are present in the first set but not in the second set.
difference_set = set1.difference(set2) # {1, 2}

# Symmetric difference of sets
symmetric_difference_set = set1 ^ set2  # {1, 2, 4, 5}

symmetric_difference_set = set1.symmetric_difference(set2) # {1, 2, 4, 5}

```

- Checking Membership:
  You can check if an element is present in a set using the in keyword.

```python
if 3 in my_set:
    print("3 is present in the set")

```

- Iterating Over Sets:
  You can iterate over a set using a for loop.

```python
for element in my_set:
    print(element)

```

- length

```python
print(len({1, 2, 3}))  # Output: 3

```

- clear
```python
my_set.clear()
print(my_set)  # Output: set()

```

## 3, What are the most common methods of set and how to use them

See the above.

## 4, When to use sets versus lists
Choosing between sets and lists depends on the specific requirements of your program and the characteristics of the data you're working with.

### Use Sets When:
- Uniqueness Matters:
Use sets when you need to work with a collection of unique elements. Sets automatically eliminate duplicates, so they are ideal when you want to ensure uniqueness or remove duplicate elements from a collection.

- Membership Testing:
Sets provide very efficient membership testing using the in operator. If you frequently need to check whether an element is present in a collection, sets offer faster lookups compared to lists.

- Set Operations:
If you need to perform set operations such as union, intersection, difference, or symmetric difference, sets provide built-in methods for these operations, making your code cleaner and more concise.

- Order Doesn't Matter:
Sets are unordered collections, meaning the order of elements is not guaranteed. If the order of elements is not important for your use case, sets can be a good choice.

### Use Lists When:
- Ordered Collection:
Use lists when you need to maintain the order of elements in your collection. Lists preserve the order in which elements are added and allow for indexed access to elements.

- Allows Duplicates:
If your data includes duplicate elements and you want to preserve them, lists are suitable. Unlike sets, lists allow duplicate elements.

- Sequential Data:
Lists are suitable for sequential data where the position of elements matters, such as maintaining a sequence of steps or representing a time series.

- Flexible Data Structure:
Lists offer more flexibility in terms of data manipulation and storage. They support operations like appending, extending, inserting, and removing elements, which makes them versatile for various tasks.

## 5, How to iterate into a set

```python
for element in my_set:
    print(element)

```

## 6, What are dictionaries and how to use them
Dictionaries in Python are unordered collections of key-value pairs. They are mutable, meaning you can add, update, or remove elements from them. Dictionaries are commonly used for storing data in the form of key-value mappings, where each key maps to a corresponding value.

## 7, When to use dictionaries versus lists or sets
- Key-Value Mapping:
Use dictionaries when you need to store data in the form of key-value pairs, where each key maps to a corresponding value. Dictionaries are ideal for representing relationships between entities or for storing structured data.

- Fast Lookup by Key:
Dictionaries offer fast lookup times by key. If you frequently need to access or retrieve values based on their associated keys, dictionaries provide efficient access compared to lists or sets.

- Uniqueness and Immutability of Keys:
Keys in dictionaries must be unique and immutable. If your data naturally fits into this structure and you need to enforce uniqueness among keys, dictionaries are a suitable choice.

- Flexibility in Data Structure:
Dictionaries offer flexibility in terms of data manipulation and storage. They allow you to add, update, or remove key-value pairs dynamically, making them versatile for various tasks.

## 8, What is a key in a dictionary
In a dictionary, a key is a unique identifier for a value. Each key in a dictionary must be unique, meaning that no two keys can have the same name. Keys are used to access and retrieve values associated with them. 
```python
my_dict = {"name": "John", "age": 30, "city": "New York"}

print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

```
## 9, How to iterate over a dictionary
You can iterate over dictionaries using for loops to access keys, values, or key-value pairs.
```python
# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

```
## 10, What is a lambda function
A lambda function in Python is a small anonymous function defined using the lambda keyword. It allows you to create a function without a formal def statement. Lambda functions can take any number of arguments, but they can only have one expression. Lambda functions are often used when you need a simple function for a short period of time, such as when passing a function as an argument to another function.

```python
# Syntax
lambda arguments: expression

# Example
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

```

## 11, What are the map, reduce and filter functions
map(), filter(), and reduce() are built-in functions in Python for functional programming. They operate on iterables (such as lists, tuples, or sets) and perform operations on the elements of these iterables.

- map():
The map() function applies a given function to each item of an iterable and returns a list of the results. Lambda functions are commonly used with map() to apply a simple operation to every element in an iterable.

syntax
```python
map(function, iterable)

```

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

```

- filter():
The filter() function filters elements of an iterable based on a given function. Lambda functions are often used with filter() to select elements that satisfy a certain condition.

syntax
```python
map(function, iterable)
```

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

```

- reduce():
The reduce() function is used to apply a function of two arguments cumulatively to the items of an iterable, reducing them to a single value. Note that reduce() is not a built-in function in Python 3 and needs to be imported from the functools module.

Syntax
```python
functools.reduce(function, iterable[, initializer])

```
function: The function of two arguments to apply cumulatively to the items of the iterable.
iterable: The iterable to apply the function to.
initializer: An optional argument providing the initial value for the accumulation.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Output: 15

```


- sorted():
The sorted() function sorts the elements of an iterable. Lambda functions can be used with sorted() to define custom sorting criteria.

```python
words = ["banana", "apple", "grape", "orange"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['apple', 'grape', 'banana', 'orange']

```