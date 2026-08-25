'''
class-binding of data and methods

'''
class Example:
    x=100#--class variables
    def display(self):
        print("This is example  class display method")
obj=Example()#--obj creation
print(obj.x)
obj.display()
#Create class circle with to method called area and perimeter
from math import pi
class Circle:
    r=7
    def area(self):
        print(pi*self.r*self.r)
    def perimeter(self):
        print(2*pi*self.r)
obj=Circle()
obj.area()
obj.perimeter()
#constructors are used to initialize 