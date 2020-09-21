# Azamat Khankhodjaev
# 20.09.2020
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

# number_list = [number for number in )]
number_list = [num for num in range(100,1001) if not num & 1 ]
compositions = reduce(lambda x, y: x*y, number_list)
