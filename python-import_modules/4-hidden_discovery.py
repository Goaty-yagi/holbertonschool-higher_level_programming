#!/usr/bin/python3
import string


if __name__ == "__main__":
    with open("hidden_4_bis.pyc", 'rb') as f:
        line = f.read()
    array = []
    is_checking = 0
    is_name = 0
    name = ""
    alpha_lower = list(string.ascii_lowercase)
    for i in range(len(line)):
        if chr(line[i]) in alpha_lower:
            is_checking = 1
            name += chr(line[i])
        elif is_checking and chr(line[i]) == "_":
            name += chr(line[i])
            is_name = 1
        elif is_checking and is_name and chr(line[i]) not in alpha_lower:
            is_checking = 0
            is_name = 0
            array.append(name)
            name = ""
        else:
            is_checking = 0
            name = ""
    array.sort()
    for i in range(len(array)):
        if (array[i] != "hidden_" and not array[i].endswith("__")):
            print(array[i])
