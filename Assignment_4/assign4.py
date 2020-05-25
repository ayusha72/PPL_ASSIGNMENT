#Inheritance is a mechanism that allows us to create a new class – known as child class –
#that is based upon an existing class – the parent class, by adding new attributes and methods
#on top of the existing class. When you do so, the child class inherits the attributes and methods of the parent class.
import math

from abc import ABC, abstractmethod
print("Animal Example to demonstrate Inheritance")
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
class Shape:
    def __init__(self, filled=False):
        self.__filled = filled
    def get_filled(self):
        return self.__filled
    def set_filled(self, filled):
        self.__filled = filled

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth
    def get_length(self):
        return self.__length
    def set_length(self, length):
        self.__length = length
    def get_breadth(self):
        return self.__breadth
    def set_breadth(self, breadth):
        self.__breadth = breadth
    def get_area(self):
        return self.__length * self.__breadth
    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius
    def get_area(self):
        return math.pi * self.__radius ** 2
    def get_perimeter(self):
        return 2 * math.pi * self.__radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def get_side(self):
        return self.side1, self.side2, self.side3
    def set_side(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def get_area(self):
        sp = (self.side1 + self.side2 + self.side3) / 3
        return math.sqrt(sp * (sp - self.side1) * (sp - self.side2) * (sp - self.side3))
    def get_perimeter(self):
        return (self.side1 + self.side2 + self.side3)


class Ellipse(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
    def get_axes(self):
        return self.a, self.b
    def set_axes(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return math.pi * self.a * self.b
    def get_perimeter(self):
       pass

class Square(Rectangle):
    def __init__(self, a):
        super().__init__()
        self.a = a
    def get_side(self):
        return self.a
    def set_side(self, a):
        self.a = a
    def get_area(self):
        return self.a * self.a
    def get_perimeter(self):
        return 4 * self.a

class EquilateralTraingle(Triangle):
    def __init__(self, side):
        super().__init__()
        self.side1 = side
    def get_side(self):
        return self.side
    def set_side(self, side):
        self.side1 = side
    def get_area(self):
        return (math.sqrt(3)/4)*self.side*self.side
    def get_perimeter(self):
        return 3 * self.side

class Polygon(Shape):
    def __init__(self, nsides=3, side=4):
        super().__init__()
        self.n = nsides
        self.l = side
    def get_sides(self):
        return self.n
    def get_perimeter(self, name):
        return self.n * self.l
    def get_area(self, name):
        p = self.l * self.n
        a = p / math.tan(180 / self.n)
        A = p * a
        return  A / 2



r1 = Rectangle(10.5, 2.5)
c1 = Circle(12)
t1 = Triangle(5, 12, 13)
e1 = Ellipse(3, 4)
#abstarct class
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("concrete method")
#interface-- all methods are strictly abstract,we cant create object of interface if u need different implementation fot different objects
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    @abstractmethod
    def greet(self):
        print("hello")

# A simple Python function to demonstrate  
# Polymorphism 
  
def add(x, y, z = 0):  
    return x + y+z 
  
# Driver code  
print(add(2, 3)) 
print(add(2, 3, 4)) 



class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
  
    def language(self): 
        print("Hindi is the most widely spoken language of India.") 
  
    def type(self): 
        print("India is a developing country.") 
  
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
  
    def language(self): 
        print("English is the primary language of USA.") 
  
    def type(self): 
        print("USA is a developed country.") 
  
obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type() 



class Bird: 
  def intro(self): 
    print("There are many types of birds.") 
      
  def flight(self): 
    print("Most of the birds can fly but some cannot.") 
    
class sparrow(Bird): 
  def flight(self): 
    print("Sparrows can fly.") 
      
class ostrich(Bird): 
  def flight(self): 
    print("Ostriches cannot fly.") 
      
obj_bird = Bird() 
obj_spr = sparrow() 
obj_ost = ostrich() 
  
obj_bird.intro() 
obj_bird.flight() 
  
obj_spr.intro() 
obj_spr.flight() 
  
obj_ost.intro() 
obj_ost.flight() 

#Modularity refers to the concept of making multiple modules first and then linking and combining them to form a 
# complete system (i.e, the extent to which a software/Web 
# application may be divided into smaller modules is called modularity). Modularity enables re-usability 
# and will minimize duplication.

#all methods are virtual in python.

