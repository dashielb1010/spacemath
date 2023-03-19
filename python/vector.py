from .distance import distance
from .point import Point


class Vector(object):
    def __init__(self, p0, p1):

        if not isinstance(p0, Point) or not isinstance(p1, Point):
            raise ValueError("Vector's must be initialized with valid Point objects.")

        self._tail = p0
        self._head = p1

    @property
    def magnitude(self):
        return distance(self._tail, self._head)

    def __repr__(self):
        return "%s(%s,%s)" % (self.__class__.__name__, self._tail, self._head)

    @property
    def tail(self):
        return self._tail

    @property
    def head(self):
        return self._head
