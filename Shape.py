class Shape: #Parent class
    shape_type = 'shape'
    def calculate_area(self):
        pass
    def print_results(self):
        print('The area of a', self.shape_type, 'is', self.calculate_area())

#Inheritance - A mechanism in OOP that allows you to create a new class from an existing class. 
#Polymorphism - Method overloading or method overriding

class Circle(Shape): #Child class of Shape
    shape_type = 'Circle'
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2 #Override
    
class Square(Shape): #Child class of Shape
    shape_type = 'Square'
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width 

class Triangle(Shape): #Child of Shape class
    shape_type = 'Triangle'
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

lil_circle = Circle(10)
square = Square(5, 4)
triangle = Triangle(4, 6)

# print('The area of a circle is', lil_circle.calculate_area())
# print('The area of a square is', square.calculate_area())
# print('The area of a triangle is', triangle.calculate_area())

lil_circle.print_results()
square.print_results()
