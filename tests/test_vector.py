import unittest

from python.vector import Vector
from python.point import Point, origin
from python.distance import distance


class TestVector(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Vector(1)

    def test_magnitude(self):
        p0, p1 = Point(0, 0), Point(3, 4)
        d = distance(p1, p0)
        v = Vector(p1)
        self.assertEqual(d, v.magnitude)

    def test_repr(self):
        p0 = Point(1, 2)
        v = Vector(p0)
        print(v)

    def test_add(self):
        p0 = Point(0, 0)
        v0 = Vector(p0)

        p1 = Point(1, 0)
        v1 = Vector(p1)

        p2 = Point(0, 1)
        v2 = Vector(p2)

        p3 = Point(1, 1)
        v3 = Vector(p3)

        with self.assertRaises(ValueError):
            v0 + 1

        r1 = v0 + v1
        self.assertEqual(r1, v1)

        r2 = v0 + v2
        self.assertEqual(r2, v2)

        r3 = v1 + v2
        self.assertEqual(r3, v3)


if __name__ == '__main__':
    unittest.main()
