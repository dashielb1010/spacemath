import unittest

from python.simulation import Simulation
from python.obj import Object
from python.force import Force
from python.point import Point, origin


class TestSimulation(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            # Make sure `t` requires a number.
            Simulation(t="spam")
        with self.assertRaises(ValueError):
            Simulation(t_inc="ham")

    def test_sim_time(self):
        sim = Simulation()
        self.assertTrue(hasattr(sim, "time"))
        self.assertIsInstance(sim.time, float)

    def test_sim_objects(self):
        sim = Simulation()
        self.assertTrue(hasattr(sim, "objects"))
        self.assertIsInstance(sim.objects, dict)

    def test_sim_add_objects(self):
        sim = Simulation()
        with self.assertRaises(ValueError):
            sim.add_object(1)

        with self.assertRaises(ValueError):
            obj = Object()
            sim.add_object(obj)
            sim.add_object(obj)

    def test_forces(self):
        sim = Simulation()
        obj = Object(mass=1)
        sim.add_object(obj)

        with self.assertRaises(ValueError):
            sim.apply_force(123, 123)

        with self.assertRaises(ValueError):
            sim.apply_force(obj, 123)

        f = Force(origin(), Point(1, 0))
        with self.assertRaises(ValueError):
            sim.apply_force(123, f)

        obj2 = Object()
        with self.assertRaises(ValueError):
            sim.apply_force(obj2, f)

        self.assertEqual(sim.get_forces(obj), [])
        sim.apply_force(obj, f)
        self.assertIn(f, sim.get_forces(obj))

    def test_increment(self):
        sim = Simulation()
        t0 = 0.0
        t_inc = 1
        t1 = t0 + t_inc
        sim.run()
        self.assertEqual(sim.time, t1)

        steps = 2
        t2 = t1 + t_inc * steps
        sim.run(steps)
        self.assertEqual(sim.time, t2)

        steps = 3
        t_inc = 10
        sim.time_increment = t_inc
        sim.run(steps)
        t3 = t2 + t_inc * steps
        self.assertEqual(sim.time, t3)

        with self.assertRaises(ValueError):
            sim.run("Spam!")

        with self.assertRaises(ValueError):
            sim.run(1.0)


if __name__ == '__main__':
    unittest.main()
