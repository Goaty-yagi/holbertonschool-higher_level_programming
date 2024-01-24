#!/usr/bin/python3

def uppercase(str):
    counter = 0
    current = 0
    separator = ""
    while (counter < len(str)):
        current = ord(str[counter])
        separator = "" if counter != len(str) - 1 else "\n"
        if 97 <= current <= 122:
            print("{}".format(chr(current - 32)), end=separator)
        else:
            print("{}".format(str[counter]), end=separator)
        counter = counter + 1
