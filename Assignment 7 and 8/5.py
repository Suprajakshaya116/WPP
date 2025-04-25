# 5. Create a base class "Shape" with methods to calculate the area and perimeter. Implement
# derived classes "Rectangle" and "Circle" that inherit from "Shape" and provide their own area
# and perimeter calculations.
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class square(shape):
    def __init__(self,a):
        self.side=a
    def area(self):
         return self.side**2
    def perimeter(self):
        return self.side*4
class rectangle(shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return  self.breadth*self.length
    def perimeter(self):
         return 2*(self.length+self.breadth)
sq=int(input("enter the side of square:"))
s=square(sq)
print("Square:")
print("area:",s.area()," ","perimeter:",s.perimeter())
l,b=map(int,input("enter length and breadth of rectangle:").split())
r=rectangle(l,b)
print("Rectangle:")
print("area:",r.area()," ","perimeter:",r.perimeter())
