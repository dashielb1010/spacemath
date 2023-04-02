import unittest

from python.simulation import Simulation
from python.body import Body
from python.force import Force
from python.point import Point, origin


class TestSimulation(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            # Make sure `t` requires a number.
            Simulation(t="spam")
        with self.assertRaises(ValueError):
            Simulation(t_inc="ham")

    def test_time(self):
        sim0 = Simulation()
        self.assertTrue(hasattr(sim0, "time"))
        self.assertIsInstance(sim0.time, float)

        t0 = 2
        t_inc = 3
        num_incs = 4
        sim1 = Simulation(t=t0, t_inc=t_inc)
        sim1.run(num_incs)
        t1 = t0 + t_inc * num_incs
        self.assertEqual(sim1.time, t1)

    def test_objects(self):
        sim = Simulation()
        self.assertTrue(hasattr(sim, "objects"))
        self.assertIsInstance(sim.objects, dict)

    def test_add_objects(self):
        sim = Simulation()
        with self.assertRaises(ValueError):
            sim.add_object(1)

        with self.assertRaises(ValueError):
            obj = Body()
            sim.add_object(obj)
            sim.add_object(obj)

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

    def test_run(self):
        sim = Simulation()
        sim.run(1)
        self.assertEqual(sim.time, 1.0)

        p0 = origin(2)

        jeff = Body(mass=1, location=p0)
        sim.add_object(jeff)
        force_jeff = Force(Point(1, 0))
        jeff.apply_forces(force_jeff)


if __name__ == '__main__':
    unittest.main()
