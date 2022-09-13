#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

list = []
idx = 0
new_list = delete_at(list, idx)
print(new_list)
print(list)