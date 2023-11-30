#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4 as h4_module  # Changed alias for better readability

    # Using list comprehension for simplicity
    names = [name for name in dir(h4_module) if not name.startswith("__")]

    for name in names:
        print(name)
