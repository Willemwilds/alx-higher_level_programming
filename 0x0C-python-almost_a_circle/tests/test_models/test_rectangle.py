import unittest
import json
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        # Test the constructor (__init__) of Rectangle
        r = Rectangle(10, 20, 1, 2, 100)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_area(self):
        # Test the area method
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        # Test the display method
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        # Test the __str__ method
        r = Rectangle(4, 6, 2, 1, 99)
        expected_str = "[Rectangle] (99) 2/1 - 4/6"
        self.assertEqual(str(r), expected_str)

    def test_update(self):
        # Test the update method
        r = Rectangle(2, 3, 4, 5, 10)
        r.update(1, 6, 7, 8, 9)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)

    def test_to_dictionary(self):
        # Test the to_dictionary method
        r = Rectangle(3, 4, 1, 2, 5)
        d = r.to_dictionary()
        expected = {"id": 5, "width": 3, "height": 4, "x": 1, "y": 2}
        self.assertEqual(d, expected)

if __name__ == '__main__':
    unittest.main()
