from .point import Point


class Object(object):
    def __init__(self, mass=0.0, location=Point(), _id=None):
        self._mass = mass
        self._location = location
        if _id is None:
            self._id = self.__hash__()
        else:
            self._id = _id

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
            raise ValueError("Location must be instance of spacemath.point.Point, not %s" % type(point))
        self._location = point
