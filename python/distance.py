import math

from .point import Point


def distance(p1, p2):
    if not isinstance(p1, Point) or not isinstance(p2, Point):
        raise ValueError("Distance calculation requires spacemath.point.Point(), not %s and %s" % (type(p1), type(p2)))

    if 0 in (p1.num_dimensions, p2.num_dimensions):
        raise ValueError("Zero dimensional points cannot be used in distance calculations.")

    if p1.num_dimensions != p2.num_dimensions:
        raise ValueError(
            "Cannot find the distance between spacemath.point.Point()s with different number of dimensions."
        )

    # Compare vector components by subtraction, square the results, and collect them.
    diff_sqs = []
    for vc1, vc2 in zip(p1.location, p2.location):
        vc_d = vc1 - vc2
        d_sq = vc_d ** 2
        diff_sqs.append(d_sq)

    sum_diffs = math.fsum(diff_sqs)

    dist = math.sqrt(sum_diffs)

    return dist
