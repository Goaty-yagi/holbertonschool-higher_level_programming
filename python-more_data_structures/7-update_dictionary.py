#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary.get(key):
        del a_dictionary[key]
    a_dictionary[key] = value

    return a_dictionary
