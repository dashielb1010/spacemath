import unittest

from python.simulation import Simulation
from python.obj import Object


class TestSimulation(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            # Make sure `t` requires a number.
            Simulation(t="spam")

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


if __name__ == '__main__':
    unittest.main()
