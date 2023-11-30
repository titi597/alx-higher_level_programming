#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Skip the first argument, which is the script name
    args = argv[1:]

    # Ensure at least one argument is provided
    if len(args) == 0:
        print(0)
    else:
        # Convert each argument to an integer and sum them
        result = sum(int(arg) for arg in args)
        print(result)
