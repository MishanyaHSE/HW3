from random import randint
from transport_error import *


# number.py - содержит процедуры связанные с обработкой обобщенной фигуры и создания произвольной фигуры.

class Transport:

    def __init__(self) -> None:
        self.speed = None
        self.distance = None

    # Ввод обобщенного транспорта.
    def read_transport_parameters(self, *args):
        self.speed = args[0]
        self.distance = args[1]
        if self.speed <= 0:
            raise Incorrect_transport_speed(args[0])
        if self.distance <= 0:
            raise Incorrect_transport_distance(args[1])

    # Генерация параметров транспорта.
    def generate_parameters(self):
        pass

    # Вывод обобщенного транспорта в консоль.
    def print(self):
        pass

    # Вывод обобщенного транспорта в файл.
    def write(self, output_stream):
        pass

    # Вычисление вещественного представления обобщенного транспорта.
    def get_perfect_time(self):
        return self.distance / self.speed
