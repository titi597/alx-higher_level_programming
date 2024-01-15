#!/usr/bin/python3
"""Defines unittests for the Rectangle class."""
import io
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unittests for testing Rectangle class."""

    def test_instantiation(self):
        r = Rectangle(10, 5)
        self.assertIsInstance(r, Base)
        self.assertIsInstance(r, Rectangle)

        # Add more instantiation tests based on your requirements

    def test_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

        # Add more area tests based on your requirements

    def test_display(self):
        r = Rectangle(2, 3)
        captured_output = self.get_display_output(r)
        expected_output = "##\n##\n##\n"
        self.assertEqual(captured_output, expected_output)

        # Add more display tests based on your requirements

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

        # Add more __str__ tests based on your requirements

    def test_to_dictionary(self):
        r = Rectangle(10, 5, 3, 1, 8)
        expected_dict = {
            'id': 8,
            'width': 10,
            'height': 5,
            'x': 3,
            'y': 1
        }
        self.assertDictEqual(r.to_dictionary(), expected_dict)

        # Add more to_dictionary tests based on your requirements

    def test_update(self):
        r = Rectangle(10, 5, 3, 1, 8)
        r.update(9)
        self.assertEqual(str(r), "[Rectangle] (9) 3/1 - 10/5")
        
        r.update(width=20, height=7, x=1)
        self.assertEqual(str(r), "[Rectangle] (9) 1/1 - 20/7")

        # Add more update tests based on your requirements

    def get_display_output(self, rectangle):
        """Capture the output of the display method."""
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rectangle.display()
        return mock_stdout.getvalue()


if __name__ == "__main__":
    unittest.main()
