import unittest

from python.point import Point


class PointTest(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            Point(None)

        with self.assertRaises(ValueError):
            Point("")

        with self.assertRaises(TypeError):
            Point(PointTest)

    def test_num_dimensions(self):
        p0 = Point()
        self.assertEqual(p0.num_dimensions, 0)

        p1 = Point(1)
        self.assertEqual(p1.num_dimensions, 1)

        p2 = Point(1, 2)
        self.assertEqual(p2.num_dimensions, 2)

        p3 = Point(1, 2, 3)
        self.assertEqual(p3.num_dimensions, 3)

    def test_location(self):

        # All location values should be floats.
        p = Point(1, 2, 3)
        for n in p.location:
            self.assertIsInstance(n, float)

        # Make sure we can't modify a point's location from outside the class.
        loc = p.location
        loc[0] = 10
        self.assertNotEqual(p.location, loc)


if __name__ == '__main__':
    unittest.main()
