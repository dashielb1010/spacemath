from .obj import Object


class Simulation(object):
    def __init__(self, t=0.0):
        self._t = float(t)
        self._objects = dict()

    @property
    def time(self):
        return self._t

    @property
    def objects(self):
        return self._objects

    def add_object(self, obj):
        if not isinstance(obj, Object):
            raise ValueError("Simulation objects must be instance of `obj.Object`, not %s" % type(obj))

        if obj.id in self._objects:
            raise ValueError("Cannot add the same object to a simulation twice.")

        self._objects[obj.id] = obj
