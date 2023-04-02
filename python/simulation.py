from .body import Body
from .force import Force


class Simulation(object):
    def __init__(self, t=0.0, t_inc=1.0):
        self._t = float(t)
        self._t_inc = float(t_inc)
        self._objects = dict()
        self._force = dict()

    @property
    def time(self):
        return self._t

    @property
    def time_increment(self):
        return self._t_inc

    @time_increment.setter
    def time_increment(self, t_inc):
        self._t_inc = t_inc

    @property
    def objects(self):
        return self._objects

    def add_object(self, obj):
        if not isinstance(obj, Body):
            raise ValueError("Simulation objects must be instance of %s, not %s" % (Body.__name__, type(obj)))

        if obj.id in self._objects:
            raise ValueError("Cannot add the same object to a simulation twice.")

        self._objects[obj.id] = obj

    def run(self, increments=1):
        if not isinstance(increments, int):
            raise ValueError("Argument increments requires %s not %s." % (int, type(increments)))
        for i in range(increments):
            self._run_step()

    def _run_step(self):
        self._t += self._t_inc
