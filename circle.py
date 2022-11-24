# Сделать проверку валидации фигуры. 
# У круга это только проверка радиуса на число и положительное значение (геттер и сеттер)
# Круг: 
# аттрибуты: радиус
# методы: длина окружности и площадь

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_length(self, radius):
        return round(2 * math.pi * radius, 2)
    
    def get_square(self, radius):
        return round(math.pi * radius * radius, 2)

    @classmethod
    def from_area(cls, area):
        return cls(math.sqrt(area/math.pi))

    @classmethod
    def from_length(cls, length):
        return cls(length/(2*math.pi)) 

circle = Circle(5)
print(circle.get_length(5))
print(circle.get_square(5))

circle_from_length = Circle.from_length(31.42)
print(circle_from_length.radius)

circle_from_area = Circle.from_area(78.54)
print(circle_from_area.radius) 