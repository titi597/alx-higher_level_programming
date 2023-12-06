#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a copy of the dictionary to avoid modifying it while iterating
    new_dict = a_dictionary.copy()

    # Iterate through the dictionary and delete keys with the specified value
    for key, val in a_dictionary.items():
        if val == value:
            del new_dict[key]

    return new_dict
