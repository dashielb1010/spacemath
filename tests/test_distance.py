import unittest

from ..point import Point

from ..distance import distance


class TestDistance(unittest.TestCase):
    def test_distance_2d(self):

        with self.assertRaises(ValueError):
            p0 = Point()
            p1 = Point(1)
            distance(p0, p1)

        # 3 4 5 triangle should nail it.
        right_triangle_0 = Point(0, 0)
        right_triangle_1 = Point(3, 0)
        right_triangle_2 = Point(3, 4)

        self.assertEqual(distance(right_triangle_0, right_triangle_0), 0)
        self.assertEqual(distance(right_triangle_0, right_triangle_1), 3)
        self.assertEqual(distance(right_triangle_1, right_triangle_2), 4)
        self.assertEqual(distance(right_triangle_0, right_triangle_2), 5)

    def test_distance_3d(self):
        # https://www.calculatorsoup.com/calculators/geometry-solids/distance-two-points.php
        d = 10.246950765959598
        p1 = Point(7, 4, 3)
        p2 = Point(17, 6, 2)
        self.assertEqual(distance(p1, p2), d)


if __name__ == '__main__':
    unittest.main()
