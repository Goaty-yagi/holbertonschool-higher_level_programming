#!/usr/bin/python3

""""
The Square module provides a class to represent square shapes.

Usage:
    from square import Square

    # Create a square object
    square = Square()
"""


class Square:
    """
    Represents a square shape.

    Attributes:
        None

    Methods:
        - __init__(self, size=0, position=(0, 0)):
        Initializes a square with a given size and position.
        - size: Property to get or set the size of the square.
        - position: Property to get or set the position of the square.
        - setter(self, new_value): Sets the size of the square with validation.
        - position_setter(self, new_value):
        Sets the position of the square with validation.
        - area(self): Computes and returns the area of the square.
        - my_print(self): Prints the square with '#' characters
        at the specified position.

    Usage:
        # Create a square object
        square = Square()
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.__size = 0
        self.__position = (0, 0)
        self.setter(size)
        self.position_setter(position)

    @property
    def size(self):
        """
        Property to get or set the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The size to set.

        Raises:
            ValueError: If the size is less than 0.
            TypeError: If the size is not an integer.
        """
        return self.setter(value)

    @property
    def position(self):
        """
        Property to get or set the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        return self.position_setter(value)

    def position_setter(self, new_value):
        """
        Sets the position of the square with validation.

        Args:
            new_value (tuple): The position to set.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        
        if isinstance(new_value, tuple) and len(new_value) == 2:
            if all(isinstance(value, int) for value in new_value):
                if all(value >= 0 for value in new_value):
                    self.__position = new_value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def setter(self, new_value):
        """
        Sets the size of the square with validation.

        Args:
            new_value (int): The size to set.

        Raises:
            ValueError: If the size is less than 0.
            TypeError: If the size is not an integer.
        """
        if isinstance(new_value, int):
            if new_value < 0:
                raise ValueError("size must be >= 0")
            self.__size = new_value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with '#' characters at the specified position.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
