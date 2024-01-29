#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    temp = 0
    appended = 0
    for i in range(list_length):
        try:
            temp = my_list_1[i] / my_list_2[i]
            new_list.append(temp)
            appended = 1
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            if appended == 0:
                new_list.append(0)
            else:
                appended = 0
    return new_list
