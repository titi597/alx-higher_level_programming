#!/usr/bin/python3
def uppercase(s):
    for char in s:
        print("{}".format(chr(ord(char) - 32) if 'a' <= char <= 'z' else char), end="")
    print()
