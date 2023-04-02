import unittest
from python.body import Body
from python.point import Point, origin
from python.force import Force
from python.vector import Vector


class TestObject(unittest.TestCase):
    def test_id(self):
        # null object
        obj = Body()

        # Test id property
        self.assertTrue(hasattr(obj, "id"))
        self.assertEqual(obj.id, obj.__hash__())

    def test_location(self):
        obj = Body()
        # Test location property
        point = Point(0, 0)
        obj.location = point
        self.assertEqual(obj.location, point)

        # now initialize Object and make sure it hooks up.
        point2 = Point(3, 4, 5)
        obj2 = Body(
            location=point2
        )
        self.assertEqual(obj2.location, point2)

        with self.assertRaises(ValueError):
            obj2.location = (1, 2, 3)

    def test_mass(self):
        obj = Body()
        # Test mass property
        mass = 1.0
        obj.mass = mass
        self.assertEqual(obj.mass, mass)
        self.assertIsInstance(obj.mass, float)

        with self.assertRaises(ValueError):
            Body(mass=0)

        with self.assertRaises(ValueError):
            Body(mass=-1.0)

        obj2 = Body(
            mass=10,  # pass int to make sure it's later float.
        )
        self.assertEqual(obj2.mass, 10.0)
        self.assertIsInstance(obj2.mass, float)

    def test_forces(self):
        obj = Body()
        self.assertEqual(obj.forces_applied, [])
        with self.assertRaises(ValueError):
            obj.apply_forces(1)
        with self.assertRaises(ValueError):
            obj.apply_forces(2, 3, 4)
        force = Force(Point(1, 1))
        obj.apply_forces(force)
        self.assertEqual(obj.forces_applied, [force])

    def test_acceleration(self):
        obj = Body(mass=1.0)
        self.assertIsInstance(obj.acceleration, Vector)


if __name__ == '__main__':
    unittest.main()
