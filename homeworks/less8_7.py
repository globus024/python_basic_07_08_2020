# Azamat Khankhodjaev
# 04.10.2020
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.
# z=z1*z2=(a1*a2−b1*b2)+(a1*b2+b1*a2)i

class Complex:
    def __init__(self, complex: str):
        self.__operator = ''
        self.__number = 0
        self.__i = ''

        if '+' in complex:
            self.__operator = '+'
            self.__number = complex.split('+')[0]
            self.__i = complex.split('+')[1]
        elif '-' in complex:
            self.__operator = '-'
            self.__number = complex.split('-')[0]
            self.__i = complex.split('-')[1]
        else:
            if 'i' in complex:
                self.__i = complex.split('i')[0]
            else:
                raise ValueError('не комплексное число')
        print(self.__number,self.__operator, self.__i)

    def __add__(self, other):
        self.__number + other.__number

if __name__ == '__main__':
    с = Complex('1+2i')