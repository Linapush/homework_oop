#Сделать так, чтобы файл не перезаписывался, а инфа добавлялась в конец

# Написать программу, предлагающую пользователю записывать данные о зданиях.
# Каждое здание имеет: кол-во этажей, высоту, ширину, название.
# Первые три свойства обязательно при инициализации должны быть числами, большими нуля.
# Хранить данные о зданиях в структурированном файле.
# Написать дополнительную программу (или написать 2 в 1 с меню выбора действий - по желанию),
# которая читает здания из файла и выводит информацию о текущих записанных зданиях.

from multiprocessing import Process

class NotValidBuilding(Exception):
    pass

class Building:

    def __init__(self, floors: int, high: int, width: int, name: str):
        self.floors = floors
        self.high = high
        self.width = width
        self.name = name

        if not self.is_valid():
            #raise NotValidBuilding
            print('Ошибка! Введите значение > 0')

    def is_valid(self):
        parametres = [self.floors, self.width, self.high]
        
        if all([isinstance(pm, int) for pm in parametres]):
            return all([pm > 0 for pm in parametres])
        return False

    def __str__(self):
        return f'Building: floor={self.floors}, high={self.high}, width={self.width}, name={self.name}'
    
    def to_tuple(self):
        return self.floors, self.high, self.width, self.name

    @classmethod
    def from_tuple(cls, data):
        try:
            parameters = int(data[0]), int(data[1]), int(data[2]), data[3],
        except:
            print('Ошибка чтения из файла')
        else:
            return cls(*parameters)


import csv 

def user():
    print('Введите 0 или 1 для создания или просмотра здания')
    change = input()
    if change == '0':
        with open('buldings_1', 'a') as file:

            print("Введите название здания: ")
            name = input()
            
            print("Введите высоту здания: ")
            high = input()
            
            print("Введите ширину здания: ")
            width = input()

            print("Введите количество этажей: ")
            floors = input()

            #building = Building(floors, high, width, name) #передать аргументы
            
            try:
                building = Building(int(floors), int(high), int(width), name)

            except ValueError:
                print("Ошибка! Введите значения высоты, ширины и количество этажей целым числом!")
                
            else:
                csv_writer = csv.writer(file)
                csv_writer.writerow([*building.to_tuple()])
            

        #try/except/else - try - , else - ошибка, int - запись в файл

    elif change == '1':
        with open('buldings_1', 'rt') as file:
            csv_reader = csv.reader(file)
            buildinds_csv=([Building.from_tuple(row) for row in csv_reader])
            for bd in buildinds_csv:
                print(bd)
user()



