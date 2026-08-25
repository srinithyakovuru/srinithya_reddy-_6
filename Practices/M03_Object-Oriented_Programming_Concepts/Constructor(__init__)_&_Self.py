'''#count no.of objects created for a class
class A:
    count=0
    def __init__(self):
        A.count+=1
a=A()
b=A()
c=A()
print("object count is:",A.count)'''

'''from math import pi
class circle:
    def __init__(self.r):
        self.r=r
    def Area(self):
        return pi*self.r*self.r
    def perimeter(self):
        return 2*pi*self.r
c=circle(7)
c1=circle(10)
c2=circle(15)
print(c.Area())
print(c.perimeter())
print(c1.Area())
print(c1.perimeter())
print(c2.Area())
print(c2.perimeter())'''

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small
    def addCar(self, carType: int) -> bool:
        if carType==1:
            if self.big>0:
                self.big-=1
                return True
            return False


        elif carType==2:
            if self.medium>0:
                self.medium-=1
                return True
            return False
        else:
            if self.small>0:
                self.small-=1
                return True
            return False
  

        

