#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if len(set_1) == 0:
        return (set_2)
    if len(set_2) == 0:
        return (set_1)
    res = []
    for elem1 in set_1:
        for dif1 in set_2:
            if elem1 == dif1:
                break
        if elem1 != dif1:
            res.append(elem1)
    for elem2 in set_2:
        for dif2 in set_1:
            if elem2 == dif2:
                break
        if elem2 != dif2:
            res.append(elem2)
    return (res)
