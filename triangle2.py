#Переписать треугольник и круг так же, как мы переписали прямоугольник на паре.
#Сделать проверку валидации фигуры. 
#У треугольника ещё нужно проверить, можно ли из этих трёх сторон собрать треугольник.
#проверить, что сумма длин  двух сторон больше длины 3 стороны

#Rectangle, св-ва: a, b, c, методы: периметр, площадь)
# get_perimetr, get_square

from math import sqrt
class NotValidFigure(Exception):
    pass

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise NotValidFigure

    def is_valid(self):
        sides = [self.a, self.b, self.c]
       
        if all([isinstance(side, (int, float)) for side in sides]):
            if all([side > 0 for side in sides]):
                return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a
   
    def get_perimetr(self):
        return round(self.a + self.b + self.c, 2)

    def get_square(self):
        p = self.get_perimetr()
        return round(sqrt(p * p - self.a) * (p - self.b) * (p - self.c), 2)

triangle = Triangle(4, 4, 2)
print(triangle.get_perimetr())
print(triangle.get_square())
