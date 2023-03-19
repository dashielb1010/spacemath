import unittest

from python.vector import Vector
from python.force import Force

from python.point import origin, Point


class TestForce(unittest.TestCase):
    def test_init(self):
        p0 = origin()
        p1 = Point(1, 0)
        f = Force(p0, p1)
        self.assertIsInstance(f, Vector)

