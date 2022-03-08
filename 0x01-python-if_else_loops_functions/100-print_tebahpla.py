#!/usr/bin/python3
for i in range(122, 96, -2):
    print('{}{}'.format(chr(i), chr((i - 1) - 32)), end='')
