# Learning Objectives

- [What is OOP](what-is-oop)
- [“first-class everything”](“first-class-everything”)
- [What is a class](what-is-a-class)
- [What is an object and an instance](what-is-an-object-and-an-instance)
- [What is the difference between a class and an object or instance](what-is-the-difference-between-a-class-and-an-object-or-instance)
- [What is an attribute](what-is-an-attribute)
- [What are and how to use public, protected and private attributes](what-are-and-how-to-use-public,-protected-and-private-attributes)
- [What is self](What-is-self)
- [What is a method](What-is-a-method)
- [What is the special __init__ method and how to use it](what-is-the-special-__init__-method-and-how-to-use-it)
- [What is Data Abstraction, Data Encapsulation, and Information Hiding](what-is-Data-Abstraction,-Data-Encapsulation,-and-Information-Hiding)
- [What is a property](What-is-a-property)
- [What is the difference between an attribute and a property in Python](what-is-the-difference-between-an-attribute-and-a-property-in-Python)
- [What is the Pythonic way to write getters and setters in Python](what-is-the-Pythonic-way-to-write-getters-and-setters-in-Python)
- [How to dynamically create arbitrary new attributes for existing instances of a class](how-to-dynamically-create-arbitrary-new-attributes-for-existing-instances-of-a-class)
- [How to bind attributes to object and classes](how-to-bind-attributes-to-object-and-classes)
- [What is the __dict__ of a class and/or instance of a class and what does it contain](what-is-the-__dict__-of-a-class-and/or-instance-of-a-class-and-what-does-it-contain)
- [How does Python find the attributes of an object or class](how-does-Python-find-the-attributes-of-an-object-or-class)
- [How to use the getattr function](how-to-use-the-getattr-function)


## 1, What is OOP
OOP stands for Object-Oriented Programming. It's a programming paradigm based on the concept of "objects," which can contain data in the form of fields (often known as attributes or properties) and code in the form of procedures (often known as methods or functions).

- Encapsulation: Encapsulation refers to bundling data and methods that operate on the data into a single unit, i.e., an object. It allows you to hide the internal state of an object from the outside world and only expose the necessary functionality through methods.

- Inheritance: Inheritance is the mechanism by which a class can inherit properties and behavior from another class. It promotes code reusability and allows for the creation of hierarchical relationships between classes.

- Polymorphism: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to be used for entities of different types, providing flexibility and extensibility in code design.

- Abstraction: Abstraction involves simplifying complex systems by modeling classes based on real-world entities and only including the relevant details. It allows you to focus on essential attributes and behaviors while hiding unnecessary implementation details.

## 2, “first-class everything”
"First-class everything" is a concept in programming languages where entities such as functions, objects, or data types are treated uniformly, without any special restrictions or limitations. In a language that embraces the "first-class everything" principle, these entities can be passed as arguments to functions, returned from functions, assigned to variables, and stored in data structures like any other data type.
Languages that embrace the "first-class everything" principle provide developers with a high degree of flexibility and expressiveness, allowing them to write concise and elegant code. 

- First-Class Functions: In a language with first-class functions, functions are treated as first-class citizens. This means they can be assigned to variables, passed as arguments to other functions, returned from functions, and stored in data structures.

- First-Class Objects: Similarly, in a language with first-class objects, objects (or instances of classes) are treated as first-class citizens. They can be assigned to variables, passed as arguments, returned from functions, and manipulated like any other data type.

- First-Class Data Types: Some languages extend the concept of first-class to other data types, such as integers, strings, arrays, and even more complex data structures like dictionaries or sets. In such languages, these data types can be manipulated in the same way as functions or objects.

## 3, What is a class
A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of the class will have.
## 4, What is an object and an instance
An object and an instance are closely related concepts, often used interchangeably, especially in the context of object-oriented programming (OOP).

- Object: An object is a tangible entity that represents a particular instance of a class. It combines data (attributes) and behaviors (methods) defined by its class. For example, if we have a class called Car, an object of that class could represent a specific car, such as a "Toyota Camry" or a "Ford Mustang." Each object of the class Car would have its own unique set of attributes (e.g., color, make, model) and behaviors (e.g., start_engine(), accelerate(), brake()).

- Instance: An instance is a concrete occurrence of a class during the runtime of a program. It refers to a specific object created from a class. For example, if we create two objects car1 and car2 from the class Car, car1 and car2 are instances of the Car class. Each instance represents a unique manifestation of the class, with its own set of attribute values.

In summary, while "object" refers to a conceptual entity that encapsulates both data and behavior defined by its class, "instance" refers to a specific occurrence of that object during the execution of a program. Every instance is an object, but not every object is necessarily an instance—objects exist conceptually, while instances exist concretely during program execution.

## 5, What is the difference between a class and an object or instance
### Class:

- Definition: A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that objects of the class will have.

- Purpose: Classes serve as the fundamental building blocks in OOP. They encapsulate data and behavior related to a specific entity or concept.

### Object (or Instance):
- Definition: An object (or instance) is a concrete occurrence of a class during the runtime of a program. It represents a specific manifestation of the class, with its own set of attribute values.

- Purpose: Objects are the actual entities that interact with each other and perform operations in a program. They encapsulate both data and behavior defined by their class.

In summary, a class is a blueprint that defines the structure and behavior of objects, while an object (or instance) is a concrete entity created from that blueprint, representing a specific occurrence of the class during the execution of a program. Classes define what objects are capable of, while objects represent actual instances of those capabilities in action.

## 6, What is an attribute
Attribute refers to a piece of data associated with a class or an object. Attributes define the state or characteristics of an object and represent the properties that describe its identity, behavior, or appearance.

### Data Representation:
Attributes represent data stored within an object. They can hold various types of information such as numbers, strings, booleans, or even references to other objects.

### Class-Level and Instance-Level Attributes: 
Attributes can be defined at the class level or the instance level:

- Class-level attributes: These are shared among all instances of a class. They are defined within the class but outside of any methods, typically at the top of the class definition.

- Instance-level attributes: These are specific to each individual instance of a class. They are typically defined within the constructor method (__init__ in Python) and can vary from one instance to another.

### Accessing Attributes:
Attributes can be accessed and manipulated using dot notation. For example, if we have a class Car with an attribute color, we can access it as car.color to get the value of the color attribute for a specific car object.

## 7, What are and how to use public, protected and private attributes
In Python, attributes can be categorized into public, protected, and private based on naming conventions, although Python does not strictly enforce access control like some other languages.

**- Public Attributes:** Public attributes have no naming convention and are accessible from anywhere, both inside and outside the class.
```python
class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"

obj = MyClass()
print(obj.public_attribute)  # Output: I am public

```

**- Protected Attributes:** Protected attributes are prefixed with a single underscore _. While not enforced by the language, it's a convention indicating that the attribute should be treated as protected and accessed only within the class or its subclasses.
```python
class MyClass:
    def __init__(self):
        self._protected_attribute = "I am protected"


obj = MyClass()
# Accessing a protected attribute (though discouraged)
print(obj._protected_attribute)  # Output: I am protected

```

**- Private Attributes:** Private attributes are prefixed with a double underscore __. Python name mangling is applied to these attributes, making them more difficult to access from outside the class. However, they can still be accessed using name mangling.

```python
class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

obj = MyClass()
# Accessing a private attribute using name mangling
print(obj._MyClass__private_attribute)  # Output: I am private
# Directly accessing a private attribute (outside the class) will raise an AttributeError.
print(obj.__private_attribute)

```

## 8, What is self
"self" is a conventionally used parameter name in instance methods of classes. It represents the instance of the class on which the method is being called.

When you define methods within a class in Python, you typically include self as the first parameter of those methods. However, when you call the method, you don't explicitly pass a value for self; Python handles it automatically. This is why it's often referred to as an implicit parameter.
## 9, What is a method
A method is a function that is associated with an object or class. Methods are defined within classes and are used to define the behavior of objects of that class. They represent actions that objects can perform or operations that can be carried out on objects.


## 10, What is the special __init__ method and how to use it
In Python, __init__ is a special method, also known as the constructor method, that is automatically called when a new instance of a class is created. It's used to initialize the object's state, typically by setting initial values for the object's attributes.

```python
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Creating an instance of MyClass
obj = MyClass(3, 5)

# Accessing the attributes of the object
print(obj.x)  # Output: 3
print(obj.y)  # Output: 5

```

- The __init__ method is defined within the MyClass class.
- It takes self as the first parameter (representing the instance being initialized) and additional parameters x and y.
- Inside the __init__ method, self.x and self.y are used to set the initial values of the object's attributes based on the values passed during object creation (obj = MyClass(3, 5)).

The __init__ method is not mandatory in a class definition, but it's commonly used to ensure that newly created instances of the class start with a known and consistent state. 

## 11, What is Data Abstraction, Data Encapsulation, and Information Hiding
**- Data Abstraction:**
- Definition: Data abstraction is the process of hiding the implementation details of a class and showing only the essential features of the object. It focuses on what an object does rather than how it does it.
- Purpose: By abstracting away unnecessary details, data abstraction simplifies the complexity of a system, making it easier to understand and use. It also promotes modularity and code reusability by allowing components to interact based on their abstract interfaces rather than their internal implementations.

**Data Encapsulation:**
-  Definition: Data encapsulation is the bundling of data (attributes) and methods (behavior) that operate on the data into a single unit, i.e., a class. It restricts direct access to the data and only allows access through well-defined interfaces (methods).
- Purpose: Encapsulation helps protect the integrity of the data by preventing unintended modification from outside the class. It promotes code maintainability and scalability by isolating changes to specific parts of the codebase. Additionally, encapsulation facilitates information hiding.

**Information Hiding:**
- Definition: Information hiding is the principle of restricting access to certain parts of a class, typically its implementation details or internal state, from the outside world. It aims to expose only the necessary information and hide the rest.
- Purpose: Information hiding enhances security and stability by limiting the exposure of sensitive or volatile information. It also fosters loose coupling between components, allowing changes to be made to one part of the system without affecting others. By hiding implementation details, information hiding promotes a clear separation of concerns and reduces dependencies.

In summary, data abstraction focuses on presenting essential features of objects, data encapsulation combines data and behavior into a single unit while restricting access, and information hiding restricts access to certain parts of a class to promote security, stability, and modularity.

## 12, What is a property
A property is a special kind of attribute that provides a mechanism for controlling access to the attributes of an object. Properties allow you to define custom behavior for getting, setting, and deleting attribute values.

- Getter Method (@property): The @property decorator is used to define a getter method for a property. **This method is called when the property's value is accessed.**
```python
class MyClass:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

```

- Setter Method (@x.setter): The @<property_name>.setter decorator is used to define a setter method for a property. **This method is called when the property's value is set.**

```python
class MyClass:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

```

- Deleter Method (@x.deleter): The @<property_name>.deleter decorator is used to define a deleter method for a property. **This method is called when the property's value is deleted.**

```python
class MyClass:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

```

## 13, What is the difference between an attribute and a property in Python
In Python, both attributes and properties are used to manage data associated with objects, but they serve slightly different purposes and provide different levels of control over how that data is accessed, set, and deleted.

### Attribute:

- An attribute is a variable that is bound to an object. It represents a piece of data associated with the object.
- Attributes can be directly accessed, set, or deleted without any special control or validation.
- Attributes are typically accessed using dot notation (obj.attribute_name), and they can store any value, including basic data types, objects, or even functions.
Example:
```python
class MyClass:
    def __init__(self):
        self.attribute = 42

obj = MyClass()
print(obj.attribute)  # Output: 42

```

### Property:

- A property is a special kind of attribute that provides additional control over how data is accessed, set, or deleted.
- Properties are defined using getter, setter, and deleter methods, allowing you to customize the behavior of attribute access.
- Properties are accessed like attributes, using dot notation (obj.property_name), but behind the scenes, the associated getter, setter, and deleter methods may be called.
- Properties are typically used when you need to add validation, transformation, or other custom logic to attribute access.
Example:
```python
class MyClass:
    def __init__(self):
        self._attribute = 42

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        if value < 0:
            raise ValueError("Attribute value cannot be negative")
        self._attribute = value

obj = MyClass()
print(obj.attribute)  # Output: 42
obj.attribute = 50
print(obj.attribute)  # Output: 50
obj.attribute = -10  # Raises ValueError

```

In summary, attributes are basic variables that store data, while properties are special attributes with getter, setter, and deleter methods that provide additional control over how data is accessed, set, or deleted. Properties are often used to add validation, transformation, or other custom logic to attribute access in a controlled manner.

## 14, What is the Pythonic way to write getters and setters in Python
The Pythonic way to write getters and setters in Python is to use properties like above.

## 15, How to dynamically create arbitrary new attributes for existing instances of a class

To dynamically create arbitrary new attributes for existing instances of a class, you can directly set the attribute using the instance name followed by a dot and the attribute name. 
```python
class MyClass:
    def __init__(self, initial_value):
        self.initial_attribute = initial_value

# Creating an instance of MyClass
obj = MyClass(42)

# Dynamically adding a new attribute
obj.new_attribute = "Hello, World!"

# Accessing the new attribute
print(obj.new_attribute)  # Output: Hello, World!

```
## 16, How to bind attributes to object and classes

Attributes can be bound to both classes and objects.

- Binding Attributes to Classes:

You can bind attributes directly within the class definition using assignment statements. These attributes become class attributes, shared among all instances of the class.
```python
class MyClass:
    class_attribute = "This is a class attribute"

print(MyClass.class_attribute)  # Output: This is a class attribute

```

- Binding Attributes to Objects:

You can bind attributes to individual objects by assigning values to them after the object has been created. These attributes become instance attributes, specific to each object.
```python
class MyClass:
    pass

obj1 = MyClass()
obj1.instance_attribute = "This is an instance attribute"

print(obj1.instance_attribute)  # Output: This is an instance attribute

```
- Class Attributes: Attributes defined within the class scope but outside any methods are class attributes. They are shared among all instances of the class and can be accessed using either the class name or instance name.
- Instance Attributes: Attributes bound to individual instances of a class are instance attributes. They are specific to each object and can only be accessed using the instance name.
## 17, What is the __dict__ of a class and/or instance of a class and what does it contain
In Python, the __dict__ attribute of a class or an instance of a class is a dictionary that contains the namespace of the class or instance. It stores the attributes and methods defined within the class or instance as key-value pairs, where the keys are the attribute or method names, and the values are the corresponding objects or functions.

### For a Class (__dict__ of a class):

- For a class, __dict__ contains the namespace of the class, including all class attributes, methods, and any other objects defined within the class.
- Class attributes and methods are stored as key-value pairs in the __dict__ dictionary.

```python
class MyClass:
    class_attribute = "Class Attribute"

    def method(self):
        pass

print(MyClass.__dict__)
# output
{'__module__': '__main__', 'class_attribute': 'Class Attribute', 'method': <function MyClass.method at 0x7f33a3a2c3a0>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}

```
In this example, MyClass.__dict__ contains the class namespace, including the class attribute class_attribute, the method method, and other special attributes like __module__, __dict__, __weakref__, and __doc__.

### For an Instance (__dict__ of an instance):

- For an instance of a class, __dict__ contains the namespace specific to that instance, including all instance attributes defined for that instance.
- Instance attributes are stored as key-value pairs in the __dict__ dictionary.
```python
class MyClass:
    pass

obj = MyClass()
obj.instance_attribute = "Instance Attribute"

print(obj.__dict__)

# output
{'instance_attribute': 'Instance Attribute'}

```
it only shows the instance attributes (variables bound to that instance) and not the methods.

## 18, How does Python find the attributes of an object or class
In Python, when you access an attribute of an object or class, Python follows a process known as attribute resolution to determine which attribute to retrieve. The attribute resolution process involves searching through multiple namespaces to find the attribute.

### 1, Instance Namespace: 
When you access an attribute from an instance (obj.attribute), Python first looks for the attribute in the instance's namespace (obj.__dict__). If the attribute is found in the instance namespace, Python returns its value.

### 2, Class Namespace:
If the attribute is not found in the instance namespace, Python then looks for it in the class namespace (Class.__dict__). This includes class attributes and methods defined within the class. If the attribute is found in the class namespace, Python returns its value.

### 3, Base Classes (Inheritance): 
If the attribute is not found in the class namespace, Python continues the search in the base classes of the class (if any) according to the method resolution order (MRO). Python follows the MRO defined by the class's inheritance hierarchy to search for the attribute in the parent classes and their ancestors. If the attribute is found in any of the base classes, Python returns its value.

### 4, Object Built-ins:
If the attribute is not found in the class hierarchy, Python looks for special built-in attributes and methods that all objects inherit from the base object class. These include methods like __getattr__, __setattr__, __delattr__, and others. If the attribute is found in the object's built-ins, Python returns its value or invokes the appropriate method.

If Python cannot find the attribute after searching through these namespaces and base classes, it raises an AttributeError.

## 19, How to use the getattr function
The getattr() function in Python is used to retrieve the value of an attribute from an object. It provides a way to access attributes dynamically, based on their names stored in strings. The getattr() function takes three arguments:

object: The object from which to retrieve the attribute.
name: A string representing the name of the attribute to retrieve.
default (optional): An optional argument specifying the default value to return if the attribute does not exist. If not provided and the attribute does not exist, getattr() raises an AttributeError.
```python
class MyClass:
    class_attribute = "Class Attribute"

    def __init__(self):
        self.instance_attribute = "Instance Attribute"

obj = MyClass()

# Accessing class attribute using getattr()
print(getattr(MyClass, 'class_attribute'))  # Output: Class Attribute

# Accessing instance attribute using getattr()
print(getattr(obj, 'instance_attribute'))    # Output: Instance Attribute

# Accessing non-existing attribute with default value
print(getattr(obj, 'non_existing_attribute', 'Default Value'))  # Output: Default Value

```

