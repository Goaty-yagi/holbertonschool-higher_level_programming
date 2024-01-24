#!/usr/bin/python3

def uppercase(str):
    counter = 0
    current = 0

    while (counter < len(str)):
        current = ord(str[counter])
        if 97 <= current <= 122:
            current = ord(str[counter]) - 32
        else:
            current = ord(str[counter])

        print("{}".format(chr(current)), end="")
        counter = counter + 1

    print("{}".format(""))
