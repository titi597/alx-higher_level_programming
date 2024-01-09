#!/usr/bin/python3
"""Append to a file."""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added
