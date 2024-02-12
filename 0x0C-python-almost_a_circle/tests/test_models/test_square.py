import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_init(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_square_size(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 8
        self.assertEqual(s.size, 8)

    def test_square_update(self):
        s = Square(5, 2, 3, 1)
        s.update(10, 8, 7, 6)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 6)

    def test_square_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        s_dict = s.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()

