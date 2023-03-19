from .vector import Vector


class Force(Vector):
    def __init__(self, p0, p1):
        super().__init__(p0, p1)
