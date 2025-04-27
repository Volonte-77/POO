# les durcharge
from abc import ABC # permet de definir des classes de base

class Shape(ABC):
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length=length
    
    def area(self):
        return self.length * self.length
    
square=Square(4)
square_area=square.area()
print(square_area)
#creons une classe Triangle qui va herite de shape

class Triangle(Shape):
    def __init__(self,hauteur,base):
        self.base=base
        self.hauteur=hauteur
    def surface(self):
        return (self.base*self.hauteur)/2

#implementation
triangle1=Triangle(5,7)
triangle2=Triangle(10,15)
#trangle1_area=trangle1.perimetre()
print(triangle1.area())
print(triangle1.surface())
print(triangle2.area())
print(triangle2.surface())