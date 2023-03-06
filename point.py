class Point(object):
    def __init__(self, *args):
        """

        :param args:
        """
        self._location = [float(arg) for arg in args]

    @property
    def num_dimensions(self):
        """

        :return:
        """
        return len(self._location)

    @property
    def location(self):
        return list(self._location)

