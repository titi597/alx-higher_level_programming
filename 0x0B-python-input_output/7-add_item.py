#!/usr/bin/python3
"""Load, add, save."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    existing_items.extend(sys.argv[1:])
    save_to_json_file(existing_items, "add_item.json")
