# Azamat Khankhodjaev
# 30.09.2020
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from typing import List
from functools import reduce


class Matrix:
    __slots__ = ('__elements')
    '''
        the Matrix class. which should accepts data (list of lists) to form a matrix
    '''

    def __init__(self, elements: List) -> None:
        '''
        :param elements: List
        '''
        self.__elements = elements

    def __row_len(self):
        return max([len(n) for n in self.__elements])

    def __max_el_len(self):
        return max([max(n) for n in self.__elements])


    def __str__(self):
        str_list = []
        lht = len(str(self.__max_el_len()))
        # self.__max_field_len()
        string = ''
        for els in self.__elements:
            els = list(els) if isinstance(els, tuple) else els
            els = [].append(els) if isinstance(els, (int, float, str)) else els

            if len(els) < self.__row_len():
                diff = self.__row_len() - len(els)
                for i in range(diff):
                    els.append(0)
            i = 1
            for el in els:
                if i == 1:
                    string = f'|{el:{lht}}'
                elif i == len(els):
                    string = f'{string} {el:{lht}}|'
                else:
                    string = f'{string} {el:{lht}}'
                i += 1

            str_list.append(string)

        return '\n'.join(str_list)


# a = Matrix([(2, 22, 3), (3, 24), (4, 23, 6)])
# print(a)
b = Matrix([(1,), (3, 24), (4, 2223, 222)])
print(b)
