from .distance import distance
from .point import Point, origin


class Vector(object):
    def __init__(self, p1):

        if not isinstance(p1, Point):
            raise ValueError("Vector's must be initialized with valid %s objects." % Point.__name__)

        self._head = p1

    @property
    def magnitude(self):
        return distance(origin(self._head.num_dimensions), self._head)

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self._head)

    @property
    def head(self):
        return self._head

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError("Cannot add %s to type %s." % (self.__class__.__name__, type(other)))
        coordinates = [a + b for a, b in zip(self.head.location, other.head.location)]
        add_p = Point(*coordinates)
        return self.__class__(add_p)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.head == other.head
