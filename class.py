import math
class Circle:
    def __init__(self, radius):
        self.radius=radius


    def area(self):
         return math.pi*(self.radius**2)
        
    def circumference(self):
        return math.pi*(2*self.radius)

my_circle= Circle(4)
print(my_circle.area())
print(my_circle.circumference())
