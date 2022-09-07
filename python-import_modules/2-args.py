#!/usr/bin/python3
import sys
print("{} arguments:".format(len(sys.argv) - 1))
for i in range(len(sys.argv)):
    if i != 0:
        print("{}: {}".format(i, sys.argv[i]))
