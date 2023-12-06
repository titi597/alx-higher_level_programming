#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Get the keys of the dictionary in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate through the sorted keys and print key-value pairs
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
