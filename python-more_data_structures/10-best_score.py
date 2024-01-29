#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    current_key = ""
    current_max_val = 0
    for key, val in a_dictionary.items():
        current_key = key if val > current_max_val else current_key
        current_max_val = val if val > current_max_val else current_max_val

    return current_key
