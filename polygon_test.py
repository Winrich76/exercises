import pytest

from polygon import Point


@pytest.fixture()
def point():
    point = Point(0, 0, 0)
    return point


def test_initialization(point):
    assert point


@pytest.mark.parametrize("end_point, expected", (
        (Point(1, 0, 2), [0.0, 2.0]),
        (Point(1, 2, 2), [45.0, 2.82843]),
        (Point(1, 2, 0), [90.0, 2.0]),
        (Point(1, 2, -2), [135.0, 2.82843]),
        (Point(1, 0, -2), [180.0, 2.0]),
        (Point(1, -2, -2), [225.0, 2.82843]),
        (Point(1, -2, 0), [270.0, 2.0]),
        (Point(1, -2, 2), [315.0, 2.82843]),
))
def test_azimuth(point, end_point, expected):
    assert point.azimuth(end_point) == expected


@pytest.mark.parametrize('left,  right, expected', (
        (Point(1, -2, 0), Point(3, 0, 2), 90),
        (Point(1, -2, 0), Point(3, 2, 0), 180),
        (Point(1, 0, 2), Point(3, 0, 4), 0),
))
def test_angle(point, left, right, expected):
    assert Point.angle(left, point, right) == expected
