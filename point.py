class Point:
    '''
    Class of point in 3D.
    Parameters:
        name - name of the point
        x - first coordinate
        y - second coordinate
        z - third coordinate
    '''

    def __init__(self, name=None, x=None, y=None, z=None, filename=None):
        '''
        Constructor of point
        :param name: name of the point
        :param x: first coordinate
        :param y: second coordinate
        :param z: third coordinate
        :param filename: name of the file with coordinates
        '''
        if filename == None:
            self.name = name
            self.x = x
            self.y = y
            self.z = z
        else:
            file = open(filename, "rt")
            line = file.readline().split()
            self.name = line[0]
            self.x, self.y, self.z = map(int, line[1:])

    def __repr__(self):
        '''
        Return string to print instance description
        :return:
        '''
        return f"{self.name}({self.x}; {self.y}; {self.z})"


if __name__ == "__main__":
    p = Point(filename="p.txt")
    print(p)
