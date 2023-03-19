from .obj import Object
from .force import Force


class Simulation(object):
    def __init__(self, t=0.0, t_inc=1.0):
        self._t = float(t)
        self._t_inc = float(t_inc)
        self._objects = dict()
        self._forces_applied = dict()

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
        if not isinstance(obj, Object):
            raise ValueError("Simulation objects must be instance of `obj.Object`, not %s" % type(obj))

        if obj.id in self._objects:
            raise ValueError("Cannot add the same object to a simulation twice.")

        self._objects[obj.id] = obj
        self._forces_applied[obj.id] = []

    def apply_force(self, obj, force):
        if not isinstance(obj, Object):
            raise ValueError("Object required as first argument, not %s." % type(obj))

        if not isinstance(force, Force):
            raise ValueError("Force type object is required when applying force, not %s." % type(force))

        if obj.id not in self._objects:
            raise ValueError("%s has not been added to simulation." % obj)

        self._forces_applied[obj.id].append(force)

    def get_forces(self, obj):
        if not isinstance(obj, Object):
            raise ValueError("Input requires Object type, not %s." % type(obj))

        if obj.id not in self._objects:
            raise ValueError("%s has not been added to simulation." % obj)

        return self._forces_applied[obj.id]

    def run(self, increments=1):
        if not isinstance(increments, int):
            raise ValueError("Argument increments requires %s not %s." % (int, type(increments)))
        for i in range(increments):
            self._run()

    def _run(self):
        self._t += self._t_inc
