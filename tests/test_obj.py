import unittest
from python.obj import Object
from python.point import Point


class TestObject(unittest.TestCase):
    def test_obj_properties(self):
        # null object
        obj = Object()

        # Test location property
        point = Point(0, 0)
        obj.location = point
        self.assertEqual(obj.location, point)

        # Test mass property
        mass = 1.0
        obj.mass = mass
        self.assertEqual(obj.mass, mass)

        # now initialize Object and make sure it hooks up.
        point2 = Point(3, 4, 5)
        obj2 = Object(
            mass=10,  # pass int to make sure it's later float.
            location=point2
        )
        self.assertEqual(obj2.mass, 10.0)
        self.assertTrue(isinstance(obj.mass, float))
        self.assertEqual(obj2.location, point2)


if __name__ == '__main__':
    unittest.main()
