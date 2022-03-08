#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = 'Last digit of '
if number < 0:
    n = number % -10
else:
    n = number % 10
if n == 0:
    print('{}{:d} is {:d} and is 0'.format(s, number, n))
elif n > 5:
    print('{}{:d} is {:d} and is greater than 5'.format(s, number, n))
else:
    print('{}{:d} is {:d} and is less than 6 and not 0'.format(s, number, n))
