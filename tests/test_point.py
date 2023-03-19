import unittest

from python.point import Point, origin


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

    def test_eq(self):
        p0 = Point(0)
        p1 = Point(0)
        self.assertEqual(p0, p1)

        p2 = Point(0, 0)
        self.assertNotEqual(p0, p2)
        p3 = Point(0, 1)
        self.assertNotEqual(p2, p3)
        p4 = Point(0, 1.0)
        self.assertEqual(p3, p4)

    def test_origin(self):
        p = Point(0, 0)
        self.assertEqual(origin(), p)


if __name__ == '__main__':
    unittest.main()
