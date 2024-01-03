#!/usr/bin/python3
"""Text indentantion."""
def text_indentation(text):
    """a function that prints a text with 2 new
    lines after each of these characters: ., ? and :
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the indented text
    indented_text = ""

    # Iterate through each character in the text
    for char in text:
        indented_text += char

        # Add two new lines after '.', '?', and ':'
        if char in ['.', '?', ':']:
            indented_text += "\n\n"

    # Print the indented text with no leading or trailing spaces
    print(indented_text.strip())
