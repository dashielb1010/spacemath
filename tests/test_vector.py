import unittest

from python.vector import Vector
from python.point import Point
from python.distance import distance


class TestVector(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Vector(1, 2)

    def test_magnitude(self):
        p0, p1 = Point(1, 2), Point(3, 4)
        d = distance(p1, p0)
        v = Vector(p0, p1)
        self.assertEqual(d, v.magnitude)

    def test_repr(self):
        p0, p1 = Point(1, 2), Point(3, 4)
        v = Vector(p0, p1)
        print(v)


if __name__ == '__main__':
    unittest.main()
