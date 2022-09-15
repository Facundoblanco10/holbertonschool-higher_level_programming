#!/usr/bin/python3
def common_elements(set_1, set_2):
    res = []
    for e in set_1:
        for el in set_2:
            if e == el:
                res.append(e)
    return (res)
