# Azamat Khankhodjaev
# 30.09.2020
# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth_expense(self):
        pass


class Jacket(Clothes):
    def __init__(self, height:int):
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def cloth_expense(self):
        return (2 * self.__height + 0.3)

class Coat(Clothes):
    def __init__(self, size:int):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def cloth_expense(self):
        return (self.__size/6.5 + 0.5)

if __name__=='__main__':
    j = Jacket(178)
    c = Coat(45)

    print(j.height)
    print(j.cloth_expense())
    print(c.size)
    print(c.cloth_expense())