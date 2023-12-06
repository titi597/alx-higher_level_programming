#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # If the key exists, delete it using del statement
        del a_dictionary[key]

    return a_dictionary
