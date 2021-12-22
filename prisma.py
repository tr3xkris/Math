from point import Point

class Prisma:
    '''
    3D figure with 4 sides in basement
    '''

    def __init__(self, length, width, height):
        '''
        Define 4 sides in basement figure
        :param length: real length
        :param width:  real width
        :param height: real height
        '''
        self.A = Point('A', 0, 0, 0)
        self.B = Point('B', 0, width, 0)
        self.C = Point('C', length, width, 0)
        self.D = Point('D', length, 0, 0)
        self.A1 = Point('A1', 0, 0, height)
        self.B1 = Point('B1', 0, width, height)
        self.C1 = Point('C1', length, width, height)
        self.D1 = Point('D1', length, 0, height)
        self.newpoints = dict()

    def lenghtside(self,p1,p2):
        return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)**0.5

    def basementsquier(self):
        return self.lenghtside(self.A, self.B)*self.lenghtside(self.A, self.D)

    def volume(self):
        return self.lenghtside(self.A, self.A1)*self.basementsquier()

    def addedgepoint(self, name, begin, end, side1=1, side2=1):
        '''
        Add new point to current edge of prisma object. Divides this edge in proposal side1:side2.
        :param name: name of new point
        :param begin: first edge point
        :param end: last edge point
        :param side1: first part of edge
        :param side2: second part of edge
        '''
        self.newpoints[name] = Point(name, 0, 0, 0)
        #TODO: fill coordinates of new point



if __name__ == "__main__":
    obj = Prisma(3, 4, 5)
    print(obj.basementsquier())