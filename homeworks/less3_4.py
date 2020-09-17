# Azamat Khankhodjaev
# 17.09.2020
# 4. Программа принимает действительное положительное число x и целое отрицательное число  y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x: float, y: int) -> float:
    ''' The program my_func() required 2 arguments
         a positive float value x and a negative integer y
        and returned raises the number x to the degrees of y
        if the arguments do not meet the condition a ValueError is generated
    '''
    if x <= 0:
        raise ValueError('In parameter x < 0. Required more then 0')
    if y > 0:
        raise ValueError('In parameter y > 0. Required less then 0')

    return x ** y


def my_func2(x: float, y: int) -> float:
    ''' The program my_func() required 2 arguments
         a positive float value x and a negative integer y
        and returned raises the number x to the degrees of y
        if the arguments do not meet the condition a ValueError is generated
    '''
    if x <= 0:
        raise ValueError('In parameter x < 0. Required more then 0')
    if y > 0:
        raise ValueError('In parameter y > 0. Required less then 0')
    r = 1
    for _ in range(abs(y)):
        r *= 1 / x
    return r


print(my_func(2.2, -5))
print(my_func2(2.2, -5))
