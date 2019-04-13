import math


class Point:

    def __init__(self, number, x, y):
        self.number = number
        self.x = float(x)
        self.y = float(y)
        self.next_point = []

    def __str__(self):
        return 'point {}'.format(self.number)

    def __repr__(self):
        return str(self)

    def azimuth(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx * dx + dy * dy)
        if dy == 0:
            azimuth = math.pi / 2
        else:
            azimuth = abs(math.atan(dx / dy))
        azimuth = Point.quarter(dx, dy, azimuth)
        return [math.degrees(azimuth), distance]

    @staticmethod
    def quarter(dx, dy, azimuth):
        if dx > 0 and dy < 0: azimuth += (math.pi / 2)
        if dx <= 0 and dy <= 0: azimuth += math.pi
        if dx < 0 and dy > 0: azimuth += (math.pi * 3 / 2)
        return azimuth

    @staticmethod
    def go_by_azimuth(start_point):
        stack = [start_point]
        polygon = [start_point]
        observation = {}
        while stack:
            point = stack.pop()
            try:
                next_point = point.next_point[0]
                stack.append(next_point)
                polygon.append(next_point)
                observation[(point, next_point)] = point.azimuth(next_point)
            except:
                return [polygon, observation]

    @staticmethod
    def print_observation(start_point):
        observations=Point.go_by_azimuth(start_point)[1]
        for observation in observations:
            print(observation, observations[observation])












p1 = Point(1, 0, 0)
p2 = Point(2, 2, 2)
p1.next_point.append(p2)
p3 = Point(3, 2, -2)
p2.next_point.append(p3)
p4 = Point(4, -2, -2)
p3.next_point.append(p4)
p5 = Point(5, -2, 2)
p4.next_point.append(p5)

Point.print_observation(p1)

# print(p1.azimuth(p2))
# print(p1.azimuth(p3))
# print(p1.azimuth(p4))
# print(p1.azimuth(p5))
#
# print(p2.azimuth(p3))
# print(p3.azimuth(p2))
# print(p5.azimuth(p2))
# print(p2.azimuth(p5))