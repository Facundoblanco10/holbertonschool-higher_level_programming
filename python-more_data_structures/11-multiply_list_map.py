#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    number_list = [number] * len(my_list)
    new_list = []
    new_list = list(map(multiplication, my_list, number_list))
    return (new_list)

def multiplication(n, number_list):
    return (n * number_list)
