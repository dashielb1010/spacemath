from .point import Point, origin
from .vector import Vector
from .force import Force


class Body(object):
    def __init__(
            self,
            mass=1.0,
            location=None,
            forces_applied=None,
            acceleration=None,
            velocity=None,
    ):

        self._id = self.__hash__()

        if mass <= 0.0:
            raise ValueError("%s cannot have zero or negative mass, got %s." % (self.__class__.__name__, mass))
        self._mass = float(mass)

        if location is None:
            location = origin(0)
        self._location = location
        n_dimensions = location.num_dimensions

        if location is None:
            location = origin(n_dimensions)
        self.location = location

        if forces_applied is None:
            self._forces_applied = []
        else:
            self.apply_forces(*forces_applied)

        if acceleration is None:
            acceleration = Vector(origin(n_dimensions))
        self.__acceleration = acceleration

        if velocity is None:
            velocity = Vector(origin(n_dimensions))
        elif not isinstance(velocity, Vector):
            raise ValueError("Parameter velocity must be %s, not %s." % (Vector, type(velocity)))
        self.velocity = velocity

    @property
    def id(self):
        return self._id

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, mass):
        self._mass = float(mass)

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, point):
        if not isinstance(point, Point):
            raise ValueError("Location must be instance of Point, not %s" % type(point))
        self._location = point

    @property
    def forces_applied(self):
        return self._forces_applied

    def apply_forces(self, *forces):
        for force in forces:
            if not isinstance(force, Force):
                raise ValueError(
                    "%s.%s requires %s instance, not %s."
                    % (self.__class__.__name__, __name__,
                       Force.__class__.__name__, type(force))
                )
        self._forces_applied.extend(forces)
    @property
    def acceleration(self):
        return self.__acceleration

    @acceleration.setter
    def acceleration(self, acceleration):
        if not isinstance(acceleration, Vector):
            raise ValueError("Parameter acceleration must be %s, not %s." % (Vector, type(acceleration)))
        self.__acceleration = acceleration



