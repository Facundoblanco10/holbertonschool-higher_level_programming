#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    res = 0.0
    count = 0
    for i in my_list:
        for idx, j in enumerate(i):
            if idx == 0:
                temp = j
            else:
                count += j
                res += temp * j
    res = res / count
    return (res)
