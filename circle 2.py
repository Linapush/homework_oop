# Переписать треугольник и круг так же, как мы переписали прямоугольник на паре
# Сделать проверку валидации фигуры. 
# У круга это только проверка радиуса на число и положительное значение (геттер и сеттер)

# Круг: 
# аттрибуты: радиус
# методы: длина окружности и площадь

import math
class NotValidFigure(Exception):
    pass

class Circle:
    def __init__(self, radius):
        self.radius = radius
        if not self.is_valid():
            raise NotValidFigure

    def is_valid(self):
        if isinstance(self.radius, (int, float)):
            return self.radius > 0

circle = Circle(5) 
print(circle.radius)

