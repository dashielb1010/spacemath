import unittest

from python.point import Point

from python.distance import distance


class TestDistance(unittest.TestCase):
    def test_distance_0d(self):
        p1 = Point()
        p2 = Point()
        p3 = Point(1)
        with self.assertRaises(ValueError):
            distance(p1, p2)
        with self.assertRaises(ValueError):
            distance(p1, p3)

    def test_diff_dimensions(self):
        p0 = Point(1)
        p1 = Point(1, 2)
        with self.assertRaises(ValueError):
            distance(p0, p1)
        with self.assertRaises(ValueError):
            distance(p1, p0)

    def test_distance_1d(self):
        p1 = Point(1)
        p2 = Point(3)
        self.assertEqual(distance(p1, p2), 2)
        self.assertEqual(distance(p2, p1), 2)

    def test_distance_2d(self):
        # 3-4-5 triangle should nail it.
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
