# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")



class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)

    def area(self):
        return 0.5*self.base*self.height

    def __str__(self):
        return 'Triangle with base %.1f and height %.1f' %(self.base, self.height)

    def __eq__(self, other):
        return type(other) == Triangle and self.base == other.base and self.height == other.height

#
# Problem 2: Create the ShapeSet class
#

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.sh_list = []
        self.i = -1

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        if sh in self.sh_list:
            pass
        else:
            self.sh_list.append(sh)

        #print "Try to add a shape object: " + str(sh)
        

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        return self

    def next(self):
        if (self.i < len(self.sh_list)-1):
            self.i = self.i + 1
            return self.sh_list[self.i]
        else:
            raise StopIteration



    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """

        ss = ""
        for sh in self.sh_list:
            ss = ss + str(sh) + '\n'

        return ss

    def __ior__(self, other):
        """
        Add all elements from the Set "other"
        """
        for sh in other:
            self.addShape(sh)
            """if sh in self.sh_list:
                pass
            else:
                self.sh_list.append(sh)
            """
        return self


#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    max_area = 0.0
    max_shapes = []
    for sh in shapes:
        if sh.area() > max_area:
            max_shapes = [sh]
            max_area = sh.area()
        elif sh.area() == max_area:
            max_shapes.append(sh)
    
    return tuple(max_shapes)
         




#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """

    f = open(filename,'r')
    cs = ShapeSet()
    ss = ShapeSet()
    ts = ShapeSet()
    for line in f:
        obj_info = line.strip().split(',')
        if obj_info[0] == "circle":
            cs.addShape(Circle(obj_info[1]))
        elif obj_info[0] == "square":
            ss.addShape(Square(obj_info[1]))
        elif obj_info[0] == "triangle":
            ts.addShape(Triangle(obj_info[1], obj_info[2]))

    all_shapes = ShapeSet()
    #print "all circles: \n", cs
    all_shapes |= cs
    all_shapes |= ss
    all_shapes |= ts
    
    return all_shapes


def test1():
    ss = ShapeSet()
    ss.addShape(Square(0.5))
    ss.addShape(Triangle(1, 2))
    ss.addShape(Circle(3.1))
    ss.addShape(Circle(3.1))
    print "The ShapeSet has: \n" + str(ss)

    for sh in ss:
        print sh



def test2():
    ss = ShapeSet()
    t1 = Triangle(3, 8)
    ss.addShape(t1)
    t2 = Triangle(4, 6)
    ss.addShape(t2)
    ss.addShape(Circle(1))
    ss.addShape(Square(3))
    
    largest = findLargest(ss)

    print "size of largest:" , len(largest)
    for e in largest:
        if e is t1: print "Obj t1: " + str(e)
        if e is t2: print "Obj t2: " + str(e)

def test3():
    load_ss = readShapesFromFile("shapes.txt")
    print load_ss

