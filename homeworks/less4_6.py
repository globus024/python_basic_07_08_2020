# Azamat Khankhodjaev
# 20.09.2020
# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
from typing import List


def my_count(start: int) -> None:
    '''
    iterator that generates integers starting from the specified number to 10
    :param start: int parameter less 10 number
    :return: None print numbers
    '''
    if start > 10:
        print(start)
    for number in count(start):
        if number > 10:
            break
        print(number)


def my_cycle(number_list: List):
    '''
    an iterator that repeats elements of a pre-defined list.
    :param number_list: List parameter
    :return: None print element on list
    '''
    f = []
    for val in cycle(number_list):
        if not val in f:
            f.append(val)
            print(val)
        else:
            break


print('*' * 100)
my_count(2)
print('*' * 100)
my_cycle([1, 3, 5, 6, 7, 8, 99, 'ui'])
