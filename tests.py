import unittest
from polygon import Point


class PointTest(unittest.TestCase):


    def setUp(self):
        self.p1 = Point(1, 2, 2)
        self.p2 = Point(2, 2, -2)
        self.p3 = Point(3, -2, 2)
        self.p4 = Point(4, 0, 0)
        self.p5 = Point(5, -2, -2)
        self.p6 = Point(6, 2, 4)


    def test_azimuth_S(self):
        result = self.p1.azimuth(self.p2)
        expected = [180.0, 4.0]
        self.assertEqual(expected, result)

    def test_azimuth_N(self):
        result = self.p2.azimuth(self.p1)
        expected = [0.0, 4.0]
        self.assertEqual(expected, result)

    def test_azimuth_W(self):
        result = self.p1.azimuth(self.p3)
        expected = [270.0, 4.0]
        self.assertEqual(expected, result)

    def test_azimuth_E(self):
        result = self.p3.azimuth(self.p1)
        expected = [90.0, 4.0]
        self.assertEqual(expected, result)

    def test_azimuth_NE(self):
        result = self.p4.azimuth(self.p1)
        expected = [45.0, 2.82843]
        self.assertEqual(expected, result)

    def test_azimuth_SE(self):
        result = self.p4.azimuth(self.p2)
        expected = [135.0, 2.82843]
        self.assertEqual(expected, result)

    def test_azimuth_NW(self):
        result = self.p2.azimuth(self.p4)
        expected = [315.0, 2.82843]
        self.assertEqual(expected, result)

    def test_azimuth_SW(self):
        result = self.p4.azimuth(self.p5)
        expected = [225.0, 2.82843]
        self.assertEqual(expected, result)

    def test_angle_1(self):
        result = Point.angle(self.p3, self.p4, self.p1)
        expected = 90
        self.assertEqual(expected, result)

    def test_angle_2(self):
        result = Point.angle(self.p5, self.p4, self.p1)
        expected = 180
        self.assertEqual(expected, result)

    def test_angle_3(self):
        result = Point.angle(self.p1, self.p2, self.p6)
        expected = 0
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
