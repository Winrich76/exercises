import math


class Point:

    def __init__(self, number, x, y):
        self.number = number
        self.x = float(x)
        self.y = float(y)
        self.next_points = []

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
        return [math.degrees(azimuth), round(distance,5)]


    @staticmethod
    def angle(point_l, point_c, point_r):
        angle=point_r.azimuth(point_c)[0]-point_l.azimuth(point_c)[0]
        if angle<0: angle+=360
        return angle

    @staticmethod
    def quarter(dx, dy, azimuth):
        if dx > 0 and dy < 0: azimuth += (math.pi / 2)
        if dx <= 0 and dy <= 0: azimuth += math.pi
        if dx < 0 and dy > 0: azimuth += (math.pi * 3 / 2)
        return azimuth

    @staticmethod
    def go_by_azimuth(start_point):
        stack = [start_point]
        observations = {}
        angles={}
        angle_point=[start_point]
        while stack:
            point = stack.pop()
            for next_point in point.next_points:
                stack.append(next_point)
                angle_point.append(next_point)
                # if len(angle_point)>3:
                #     del angle_point[0]
                # if len(angle_point)==3:
                #     angles[(angle_point[0], angle_point[1], angle_point[2])]=Point.angle(angle_point[0], angle_point[1], angle_point[2])

                observations[(point, next_point)] = point.azimuth(next_point)

        return [observations, angle_point]

    @staticmethod
    def print_observation(start_point):
        observations=Point.go_by_azimuth(start_point)[0]
        for observation in observations:
            print(observation, observations[observation])
        angles=Point.go_by_azimuth(start_point)[1]
        for angle in angles:
            print(angle)




if __name__ == "__main__":


    p1 = Point(1, 0, 0)

    p2 = Point(2, 2, 2)
    p1.next_points.append(p2)
    p3 = Point(3, 2, -2)
    p2.next_points.append(p3)
    p4 = Point(4, -2, -2)
    p3.next_points.append(p4)
    p5 = Point(5, -2, 2)
    p2.next_points.append(p5)
    p6=Point(6, -4, (6/math.sqrt(3)+2))
    p5.next_points.append(p6)
    p7=Point(7,0,4)
    p5.next_points.append(p7)


    Point.print_observation(p1)





