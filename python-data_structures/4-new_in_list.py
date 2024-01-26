#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list = []
    for i in range(len(my_list)):
        list.append(my_list[i])
    if idx < 0 or len(my_list) <= idx:
        return list

    list[idx] = element
    return list
