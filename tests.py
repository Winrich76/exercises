import unittest
from polygon import Point


class PointTest(unittest.TestCase):


    def test_azimuth_S(self):
        p1 = Point(1, 2, 2)
        p2 = Point(2, 2, -2)
        result =p1.azimuth(p2)
        expected = [180.0, 4.0]
        self.assertEqual(expected, result)
    def test_azimuth_N(self):
        p1 = Point(1, 2, 2)
        p2 = Point(2, 2, -2)
        result = p2.azimuth(p1)
        expected = [0.0, 4.0]
        self.assertEqual(expected, result)
    def test_azimuth_W(self):
        p1 = Point(1, 2, 2)
        p2 = Point(2, -2, 2)
        result = p1.azimuth(p2)
        expected = [270.0, 4.0]
        self.assertEqual(expected, result)

    def test_azimuth_E(self):
        p1 = Point(1, 2, 2)
        p2 = Point(2, -2, 2)
        result = p2.azimuth(p1)
        expected = [90.0, 4.0]
        self.assertEqual(expected, result)
    def test_azimuth_NE(self):
        p1 = Point(1, 0, 0)
        p2 = Point(2, 2, 2)
        result = p1.azimuth(p2)
        expected = [45.0, 2.82843]
        self.assertEqual(expected, result)

    def test_azimuth_SE(self):
        p1 = Point(1, 0, 0)
        p2 = Point(2, 2, -2)
        result = p1.azimuth(p2)
        expected = [135.0, 2.82843]
        self.assertEqual(expected, result)

    def test_azimuth_NW(self):
        p1 = Point(1, 0, 0)
        p2 = Point(2, 2, -2)
        result = p2.azimuth(p1)
        expected = [315.0, 2.82843]
        self.assertEqual(expected, result)

    def test_azimuth_SW(self):
        p1 = Point(1, 0, 0)
        p2 = Point(2, -2, -2)
        result = p1.azimuth(p2)
        expected = [225.0, 2.82843]
        self.assertEqual(expected, result)




if __name__ == "__main__":
    unittest.main()


