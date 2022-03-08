#!/usr/bin/python3
for number in range(0, 9):
    for number2 in range(number + 1, 10):
        if number == 8 and number2 == 9:
            print("{}{}".format(number, number2))
        else:
            print("{}{}".format(number, number2), end=", ")
