class Point:
    '''
    Class of point in 3D.
    Parameters:
        x - first coordinate
        y - second coordinate
        z - third coordinate
    '''

    def __init__(self, name, x, y, z):
        '''
        Constructor of point
        :param name: name of the point
        :param x: first coordinate
        :param y: second coordinate
        :param z: third coordinate
        '''
        self.x = x
        self.y = y
        self.z = z

p1 = Point("A", 6, 23, -3)
p2 = Point("B", 8, 7, 2)
print(p1.x)
print(p2.x)