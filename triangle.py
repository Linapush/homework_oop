#проверить, что сумма длин жвух сторон больше длины 3 стороны
#если сумма равна, получится линия

#Rectangle, св-ва: a, b, c, методы: периметр, площадь)
# get_perimetr, get_square
class Not(Exception):
    pass
from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimetr(self):
        res = round(self.a + self.b + self.c, 2)
        return res

    def get_square(self):
        p = self.get_perimetr()
        return round(sqrt(p * p - self.a) * (p - self.b) * (p - self.c), 2)
    

triangle = Triangle(3, 2, 7)
print(triangle.get_perimetr())
print(triangle.get_square())
