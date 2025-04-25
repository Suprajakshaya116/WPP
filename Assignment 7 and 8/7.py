# 7. Create a class for representing any 2-D point or vector. The methods inside this class include
# its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
# calculating the distance between two vectors, dot product, cross product of two vectors. Extend
# the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
# D.
import math
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    @property
    def magnitude(self):
        return ((self.x**2 )+(self.y **2))**0.5
    
    @property
    def rotation(self):
        return math.degrees(math.atan(self.y/self.x))
    
    def distance(self,other):
        l=[self.x,self.y]
        m=[other.x,other.y]
        return math.dist(l,m)

    def dot(self,other):
         return (self.x*other.x )+(self.y*other.y)
    
    def crossproduct(self, other):
        return f"{(self.x * other.y)-(self.y * other.x)}k"
    
    def display(self):
        return f"{self.x}i+{self.y}j" if self.y>0 else f"{self.x}i{self.y}j" 

v=vector(3,4)
print(v.display())
s=vector(4,-5)
print(s.display())
print(s.dot(v))
print(s.crossproduct(v))
print(s.distance(v))

# print(format(v.magnitude,"0.2f"),"units"," ",format(v.rotation(),".2f"),"degrees")
 
 