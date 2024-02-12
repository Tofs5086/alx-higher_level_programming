import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle_init(self):
        r = Rectangle(5, 8, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_rectangle_area(self):
        r = Rectangle(5, 8)
        self.assertEqual(r.area(), 40)

    def test_rectangle_display(self):
        r = Rectangle(4, 4)
        self.assertEqual(r.display(), None)  # It's hard to assert stdout, so just check if the method runs without errors

    def test_rectangle_update(self):
        r = Rectangle(5, 8, 2, 3, 1)
        r.update(10, 2, 4, 6, 8)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 8)

    def test_rectangle_to_dictionary(self):
        r = Rectangle(5, 8, 2, 3, 1)
        r_dict = r.to_dictionary()
        expected_dict = {'id': 1, 'width': 5, 'height': 8, 'x': 2, 'y': 3}
        self.assertEqual(r_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()

