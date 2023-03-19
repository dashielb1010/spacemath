import unittest
from python.obj import Object
from python.point import Point, origin
from python.force import Force


class TestObject(unittest.TestCase):
    def test_obj_id(self):
        # null object
        obj = Object()

        # Test id property
        self.assertTrue(hasattr(obj, "id"))

    def test_obj_location(self):
        obj = Object()
        # Test location property
        point = Point(0, 0)
        obj.location = point
        self.assertEqual(obj.location, point)

        # now initialize Object and make sure it hooks up.
        point2 = Point(3, 4, 5)
        obj2 = Object(
            location=point2
        )
        self.assertEqual(obj2.location, point2)

        with self.assertRaises(ValueError):
            obj2.location = (1, 2, 3)

    def test_obj_mass(self):
        obj = Object()
        # Test mass property
        mass = 1.0
        obj.mass = mass
        self.assertEqual(obj.mass, mass)
        self.assertIsInstance(obj.mass, float)

        obj2 = Object(
            mass=10,  # pass int to make sure it's later float.
        )
        self.assertEqual(obj2.mass, 10.0)


if __name__ == '__main__':
    unittest.main()
