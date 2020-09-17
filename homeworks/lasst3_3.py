# Azamat Khankhodjaev
# 17.09.2020
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num1: float, num2: float, num3: float) -> float:
    if (num1 + num2) > (num2 + num3):
        x = num1
        y = num2 if num2 >= num3 else num3
    else:
        x = num3
        y = num1 if num1 >= num2 else num2

    return x + y


if __name__=='__main__':
    number_list = [(5, 1, 3), (1, 2, 1), (0, 3, 6), (3, 2, 2), (7, 3, 5), (0, 0, 0), (1.2, -2, 6.8)]
    for l in number_list:
        print(my_func(*l))
