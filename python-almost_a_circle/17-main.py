#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    s1 =Square.create(**{ 'size': 2 })
    s2 = Square.create(**{ 'size': 2, 'x': 1 }) 
    print(s1)
    print(s2)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
