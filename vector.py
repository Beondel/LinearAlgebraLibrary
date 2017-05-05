
# Ben MacMillan
# Vector Algebra Function Library
# 5/2/17

from math import sqrt, acos, pi

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, other):
        return Vector([x + y for x, y in zip(self.coordinates, other.coordinates)])

    def minus(self, other):
        return Vector([x - y for x, y in zip(self.coordinates, other.coordinates)])

    def timesScalar(self, scalar):
        return Vector([x * scalar for x in self.coordinates])

    def magnitude(self):
        return sqrt(sum([x**2 for x in self.coordinates]))

    def normalize(self):
        try:
            return self.timesScalar(1.0/self.magnitude())
        except:
            raise Exception("can not normalize the zero vector")

    def dot(self, other):
        return sum([x * y for x, y in zip(self.coordinates, other.coordinates)])

    def angle(self, other):
        result = acos(self.dot(other) / self.magnitude() * other.magnitude())
        print(str(result) + " radians")
        print(str(result * (180 / pi)) + " degrees")
        return result


v1 = Vector([0, 1, 0])
v2 = Vector([1, 0, 0])

v1.angle(v2)
