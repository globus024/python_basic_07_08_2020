# Azamat Khankhodjaev
# 20.09.2020
# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n: int) -> int:
    '''
    The function is responsible for getting the factorial of a number (the object-generator)
    :param n - int parameter:
    :return : int factorial of a number an iterable object
    '''
    res = 1
    for i in reversed([j for j in range(n, 0, -1)]):
        res *= i
        yield res


for el in fact(6):
    print(el)
