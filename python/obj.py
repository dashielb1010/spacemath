from .point import Point


class Object(object):
    def __init__(self, mass=0.0, location=Point()):
        self._mass = mass
        self._location = location

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
        self._location = point
