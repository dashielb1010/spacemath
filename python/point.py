class Point(object):
    def __init__(self, *args):
        """

        :param args:
        """
        self._location = [float(arg) for arg in args]

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, ", ".join([str(f) for f in self._location]))

    @property
    def num_dimensions(self):
        """

        :return:
        """
        return len(self._location)

    @property
    def location(self):
        return list(self._location)

