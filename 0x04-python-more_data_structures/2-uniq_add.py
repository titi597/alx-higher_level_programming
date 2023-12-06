#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate through the elements of the original list
    for num in my_list:
        # Add unique integers to the set
        unique_integers.add(num)

    # Sum up the unique integers in the set
    result = sum(unique_integers)

    return result
