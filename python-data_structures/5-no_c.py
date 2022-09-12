#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    my_string = my_string.translate({ord("c"): "", ord("C"): ""})
    return (my_string)
