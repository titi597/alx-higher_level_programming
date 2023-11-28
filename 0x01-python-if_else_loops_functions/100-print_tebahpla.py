#!/usr/bin/python3

for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char) if (char - ord('z')) % 2 == 0 else chr(char - 32)),
            end="")
