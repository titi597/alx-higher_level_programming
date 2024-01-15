#!/usr/bin/python3
"""Defines unittests for the Square class."""
import unittest
import io
import unittest.mock
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Unittests for testing Square class."""

    def test_instantiation(self):
        s = Square(5)
        self.assertIsInstance(s, Base)
        self.assertIsInstance(s, Square)

        # Add more instantiation tests based on your requirements

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

        # Add more area tests based on your requirements

    def test_display(self):
        s = Square(3)
        captured_output = self.get_display_output(s)
        expected_output = "###\n###\n###\n"
        self.assertEqual(captured_output, expected_output)

        # Add more display tests based on your requirements

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

        # Add more __str__ tests based on your requirements

    def test_to_dictionary(self):
        s = Square(5, 3, 1, 8)
        expected_dict = {
            'id': 8,
            'size': 5,
            'x': 3,
            'y': 1
        }
        self.assertDictEqual(s.to_dictionary(), expected_dict)

        # Add more to_dictionary tests based on your requirements

    def test_update(self):
        s = Square(5, 2, 1, 8)
        s.update(9)
        self.assertEqual(str(s), "[Square] (9) 2/1 - 5")
        
        s.update(size=7, x=1)
        self.assertEqual(str(s), "[Square] (9) 1/1 - 7")

        # Add more update tests based on your requirements

    def get_display_output(self, square):
        """Capture the output of the display method."""
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
        return mock_stdout.getvalue()


if __name__ == "__main__":
    unittest.main()
