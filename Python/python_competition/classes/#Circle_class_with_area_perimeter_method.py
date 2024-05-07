#Circle_class_with_area_perimeter_methods
import math

class Circle:
    def __init__(self, radius) -> None:
        self.radius = float(radius)
        
    def area(self):
        return f"radius is {math.pi * (self.radius ** 2)}"
    
    def perimeter(self):
        return f"perimeter is {2 * math.pi * self.radius}"
    
circle = Circle(input("Input radius\n>>>"))

print(circle.area())
print(circle.perimeter())