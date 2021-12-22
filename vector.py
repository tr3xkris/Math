from point import Point

class Vector:
    '''
    Class of vector in 3D.
    Parameters:
        name - name of the vector
        x - first coordinate
        y - second coordinate
        z - third coordinate
        startpoint - first point
        endpoint - second point
    '''

    def __init__(self, p1, p2):
        '''
        Constructor of vector
        :param p1: first point
        :param p2: second point
        '''
        self.name = p1.name + p2.name
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y
        self.z = p2.z - p1.z

    def __repr__(self):
        '''
        Return string to print instance description
        :return:
        '''
        return f"{self.name}({self.x}; {self.y}; {self.z})"

    def length(self):
        '''
        Calculate length of vector
        :return: length
        '''
        return (self.x**2 + self.y**2 + self.z**2)**0.5


    def __imul__(self, other):
        '''
        Multiplies vector on a number
        :param other: number
        :return: new vector
        '''
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __iadd__(self, other):
        '''
        Add other vector to current
        :param other: second vector
        :return: new vector
        '''
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def scalar_multiplication(self, other):
        '''
        Multiply current vector on other like scalars
        :param other: second
        :return: number = x1*x2 + y1*y2 + z1*z2
        '''
        return self.x * other.x + self.y * other.y + self.z * other.z

    def vector_multiplication(self, other):
        '''
        Multiply current vector on other like vectors
        :param other: second
        :return: new orthogonal vector
        '''
        new_x = self.y * other.z - self.z * other.y
        new_y = self.z * other.x - self.x * other.z
        new_z = self.x * other.y - self.y * other.x
        result = Vector(Point("O", 0, 0, 0), Point("Z", 0, 0, 0))
        result.x = new_x
        result.y = new_y
        result.z = new_z
        return result

    def get_angle(self, other, degree=False):
        '''
        Calculate an angle between current and other vector
        :param other: second vector
        :return: angle in radians
        '''
        from math import acos, pi
        angle = acos(self.scalar_multiplication(other) / self.length() / other.length())
        if degree:
            return angle * 180 / pi
        else:
            return angle

if __name__ == "__main__":
    p1 = Point(filename="p.txt")
    p2 = Point("B", 9, 3, -3)
    v1 = Vector(p1, p2)
    v2 = Vector(p2, p1)
    print(v1)
    print(v1.scalar_multiplication(v2))
    v1 += v2
    print(v1)
    e1 = Vector(Point("O", 0, 0, 0), Point("Y", 1, 0, 0))
    e2 = Vector(Point("O", 0, 0, 0), Point("Y", 0, 1, 0))
    e3 = e1.vector_multiplication(e2)
    print(e3)
    print(e1.get_angle(e2, degree=True))
    A = Point("A", 0, 0, 0)
    B = Point("B", 0, 2, 0)
    C = Point("C", 2, 2, 0)
    A1 = Point("A1", 0, 0, 1)
    C1 = Point("C1", 2, 2, 1)
    E = Point("E", 2 / 3**0.5, 2 - 2 / 3**0.5, 1 / 3**0.5)
    v1 = Vector(A, B)
    v2 = Vector(A, C)
    n1 = v1.vector_multiplication(v2)
    v1 = Vector(A1, C1)
    v2 = Vector(A1, E)
    n2 = v1.vector_multiplication(v2)
    print(n2.get_angle(n1, degree=True))
