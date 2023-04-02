import unittest

from python.vector import Vector
from python.force import Force

from python.point import origin, Point


class TestForce(unittest.TestCase):
    def test_init(self):
        point = Point(1, 0)
        f = Force(point)
        self.assertIsInstance(f, Vector)

