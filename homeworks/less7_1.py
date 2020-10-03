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
from copy import deepcopy


class Matrix:
    __slots__ = ('_elements')
    '''
        the Matrix class. which should accepts data (list of lists) to form a matrix
    '''

    def __init__(self, elements: List) -> None:
        '''
        :param elements: List
        '''
        self._elements = elements
        self.forming()

    def __row_len(self)->int:
        '''
         :return Maximal count in list:
        '''
        return max([len(n) for n in self._elements])

    def __max_el_len(self) -> (int, float):
        '''
        :return Maximal value in list:
        '''
        return max([max(n) for n in self._elements])

    def forming(self):
        elements = deepcopy(self._elements)
        for key, els in enumerate(elements):
            elem_copy = deepcopy(els)
            elem_copy = list(elem_copy) if isinstance(elem_copy, tuple) else elem_copy
            elem_copy = [].append(elem_copy) if isinstance(elem_copy, (int, float, str)) else elem_copy

            if len(elem_copy) < self.__row_len():
                diff = self.__row_len() - len(elem_copy)
                for i in range(diff):
                    elem_copy.append(0)
            self._elements.remove(els)
            self._elements.insert(key, elem_copy)

    def __str__(self):
        str_list = []
        lht = len(str(self.__max_el_len()))

        # self.__max_field_len()
        string = ''
        for els in self._elements:
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

    def __add__(self, other):
        result = []
        if not isinstance(other, Matrix):
            raise ValueError('Объект не принадлежит классу Matrix')
        if len(self._elements) != len(other._elements) or self.__row_len() != other.__row_len():
            raise ValueError('Размерность матрицы не совпадают')

        for key, _ in enumerate(self._elements):
            result.append(list(map(lambda x, y: x + y, self._elements[key], other._elements[key])))

        return Matrix(result)


if __name__ == '__main__':
    a = Matrix([(2,), [3, 24], (4, 23, 6)])
    print(a)
    print('-' * 56)
    b = Matrix([(9,), [3, 24], [4, 2223, 222.2]])
    print(b)
    print('-' * 56)
    print(a + b)
