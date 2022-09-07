#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    if len(sys.argv) == 1:
        print("0")
        quit()
    else:
        for i in range(len(sys.argv)):
            if i != 0:
                res += int(sys.argv[i])
    print("{}".format(res))
