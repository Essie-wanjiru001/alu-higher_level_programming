#!/usr/bin/python3

def print_reversed_list_interger(my_List=[]):
    if my_list is not None:
        for i in my_list((len(my_list) - 1), -1,-1):
            print("{:d}".format(my_List[i]))
        else:
            return
