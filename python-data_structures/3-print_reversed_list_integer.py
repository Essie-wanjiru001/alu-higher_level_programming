#!/usr/bin/python3

def print_reversed_list_interger(my_List=[]):
    if my_list:
        for i in my_list[::-1]:
            print("{:d}".format(i))
