import os
import sys
import unittest

from pprint import pformat

if __name__ == '__main__':
    print("Running tests with Python version:\n%s\n" % sys.version)

    sys.path.append(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )
    )

    print("sys.path:\n %s" % pformat(sys.path))

    loader = unittest.TestLoader()
    tests = loader.discover(os.curdir)

    runner = unittest.TextTestRunner()
    runner.run(tests)
