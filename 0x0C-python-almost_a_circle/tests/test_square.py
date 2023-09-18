import unittest
import json
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        # Test the constructor (__init__) of Square
        s = Square(5, 2, 3, 100)
        self.assertEqual(s.id, 100)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        # Test the area method
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_display(self):
        # Test the display method
        s = Square(3)
        expected_output = "###\n###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        # Test the __str__ method
        s = Square(4, 2, 1, 99)
        expected_str = "[Square] (99) 2/1 - 4"
        self.assertEqual(str(s), expected_str)

    def test_update(self):
        # Test the update method
        s = Square(2, 3, 4, 10)
        s.update(1, 6, 7, 9)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 9)

    def test_to_dictionary(self):
        # Test the to_dictionary method
        s = Square(3, 1, 2, 5)
        d = s.to_dictionary()
        expected = {"id": 5, "size": 3, "x": 1, "y": 2}
        self.assertEqual(d, expected)

if __name__ == '__main__':
    unittest.main()
