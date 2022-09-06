#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    print(f"Last digit of {number} is {number % 10} and ", end = '')
    if (number % 10) > 5:
        print("is greater than 5")
    elif (number % 10) == 0:
        print("is 0")
    else:
        print("is less than 6 and not 0")
else:
    print(f"Last digit of {number} is ", end = '')
    if (number % 10) == 0:
        print(f"{number % 10} and is 0")
    else:
        print(f"{(abs(number) % 10) * -1} and is less than 6 and not 0")
