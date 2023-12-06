#!/usr/bin/python3

def best_score(a_dictionary):
    # Check if the dictionary is not None
    if a_dictionary is not None:
        # Check if the dictionary is not empty
        if a_dictionary:
            # Find the key with the maximum value
            best_key = max(a_dictionary, key=a_dictionary.get)
            return best_key

    # If no score found or the dictionary is None, return None
    return None
