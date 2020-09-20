# Azamat Khankhodjaev
# 20.09.2020
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

# number_list = [number for number in )]
number_list = [reduce(lambda x, y: x if not x & 1 else y, [num, num+1]) for num in range(100,1001,2)]
print(number_list)