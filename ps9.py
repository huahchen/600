# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Triangle(Shape):
    def __init__(self, b, h):
        """
        b: length of base of the triangle
        h: height of the triangle
        """
        self.base = float(b)
        self.height = float(h)
    def area(self):
        """
        Returns area of the triangle
        """
        return self.base * self.height * 0.5
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same dimensions.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height


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

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.container = []
        ## TO DO
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if not sh in self.container:
            self.container.append(sh)
        else:
            print "Identical shape already exists in set"
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        self.place = 0
        return self
    def next(self):
        if self.place >= len(self.container):
            raise StopIteration
        self.place += 1
        return self.container[self.place - 1]
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        result = ""
        for x in self.container:
            if type(x) == Circle:
                result += (str(x) + "\n")
        for x in self.container:
            if type(x) == Square:
                result += (str(x) + "\n")
        for x in self.container:
            if type(x) == Triangle:
                result += (str(x) + "\n")
        return result
        


#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    result = ()
    largestArea = 0
    for x in shapes:
        if x.area() > largestArea:
            largestArea = x.area()
    for x in shapes:
        if x.area() == largestArea:
            result += (x,)
    return result

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    inputFile = open(filename)
    ss = ShapeSet()
    for line in inputFile:
        shape_list = line.split(',')
        shape_list[-1] = float(shape_list[-1].strip('\n'))
        if shape_list[0] == "circle":
            ss.addShape(Circle(shape_list[-1]))
        if shape_list[0] == "square":
            ss.addShape(Square(shape_list[-1]))
        if shape_list[0] == "triangle":
            shape_list[1] = float(shape_list[1])
            ss.addShape(Triangle(shape_list[1], shape_list[-1]))
    return ss

ss = readShapesFromFile('shapes.txt')
print ss

