#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    new_dict = {}

    # Iterate through the original dictionary and multiply each value by 2
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2

    return new_dict
