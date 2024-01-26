#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for i in my_list:
        list.append(True if i % 2 == 0 else False)

    if len(list) == len(my_list):
        return list
    else:
        print("Unpredictable error")
