#!/usr/bin/python3
def uppercase(str):
    upstr = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            upstr += chr(ord(i) - 32)
        else:
            upstr += i
    print('{}'.format(upstr))
