from abc import ABC, abstractmethod
import math

print("Abstraction - Animal Class Examples")
class Animal(ABC):
    def eats(self):
        pass

class Cat(Animal):
    def eats(self):
        print("Eats Mouse")

class Dog(Animal):
    def eats(self):
        print("Eats Meat")

class Lion(Animal):
    def eats(self):
        print("Eats Meat")

class Cow(Animal):
    def eats(self):
        print("Eats Grass")

class Elephant(Animal):
    def eats(self):
        print("Eats Leaves")

class Rabbit(Animal):
    def eats(self):
        print("Eats Carrots")

class Goat(Animal):
    def eats(self):
        print("Eats Grass")

class Deer(Animal):
    def eats(self):
        print("Eats Grass")

class Tiger(Animal):
    def eats(self):
        print("Eats meat")

class Human(Animal):
    def eats(self):
        print("Eats Everything")

c1 = Cat()
d1 = Dog()
l1 = Lion()
c2 = Cow()
e1 = Elephant()
r1 = Rabbit()
g1 = Goat()
d2 = Deer()
t1  = Tiger()
h1 = Human()

for obj in (c1, d1, l1, c2, e1, r1, g1, d2, t1, h1):
    obj.eats()

print("Abstraction - Shapes class Example")
#Shapes

from abc import ABC, abstractmethod
#base abstract class
class Shape(ABC):
    @abstractmethod
    def get_sides(self):
        pass
    @abstractmethod
    def printperimeter(self):
        pass
    @abstractmethod
    def printarea(self):
        pass


class Rectangle(Shape):
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_sides(self):
        print("Number of sides are:", self.sides)

    def printperimeter(self):
        print("Perimeter is:", 2 * (self.length + self.breadth))

    def printarea(self):
        print("Area is:", self.length * self.breadth)


class regPolygon(Shape):
    def __init__(self, nsides=3, side=4):
        self.n = nsides
        self.l = side

    def get_sides(self, name):
        print(f"Number of sides in a {name} are: ", self.n)

    def printperimeter(self, name):
        print(f"Perimeter of {name} is: ", self.n * self.l)

    def printarea(self, name):
        p = self.l * self.n
        a = p / math.tan(180 / self.n)
        A = p * a
        print(f"Area of {name} is: ", A / 2)


class Square(regPolygon):
    def diagonal(self):
        print("Length of diagonal is: ", math.sqrt(2) * self.l)


class Triangle(regPolygon):
    pass


class Rhombus(Shape):
    sides = 4

    def __init__(self, height, base):
        self.h = height
        self.b = base

    def get_sides(self):
        print("Number of sides in a rhombus are:", self.sides)

    def printperimeter(self):
        print("Perimeter of rhombus is: ", self.b * 4)

    def printarea(self):
        print("Area of rhombus is: ", self.b * self.h)



class Parallelogram(Rectangle):
    pass


class Trapezoid(Shape):
    sides = 4

    def __init__(self, height, base, s, c, d):
        self.h = height
        self.b = base
        self.s = s
        self.c = c
        self.d = d

    def get_sides(self):
        print("Number of sides in a trapezoid are:", self.sides)

    def printperimeter(self):
        print("Perimeter of trapezoid is: ", self.c + self.s + self.base + self.d)

    def printarea(self):
        print("Area of trapezoid is: ", (self.b + self.s) * self.h / 2)



class Circle:
    def __init__(self, r):
        self.radius = r

    def circumference(self):
        return 2 * math.pi * (self.radius)

    def area(self):
        return math.pi * math.pow(self.radius, 2)


class Ellipse(Circle):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circumference(self):
        return math.pi * ((self.a) + self.b)

    def area(self):
        return math.pi * (self.a) * (self.b)



class Sphere(Circle):
    def surface_area(self):
        return 4 * super().area()


s = Sphere(4)
print(s.surface_area())
p = Parallelogram(3, 4)
p.printarea()

print("Encapsulation Using Private Members")
class Rectangle:
    __length = 0 #private variable
    __breadth = 0#private variable
    def __init__(self):
        self.__length = 5
        self.__breadth = 3
        print("Length of rectange = ", self.__length)
        print("Breadth of rectangle = ", self.__breadth)

rec = Rectangle() #object created for the class 'Rectangle'

print("Encapsulation Using Protected Members")
class Shape:
    _length = 10
    _breadth = 20

class Parallelogram(Shape):
    def __init__(self):
        print("Length of Parallelogram = ", self._length)
        print("Breadth of Parallelogram = ", self._breadth)

cr = Parallelogram()



