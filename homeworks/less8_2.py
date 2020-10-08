# Azamat Khankhodjaev
# 04.10.2020
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class DevideZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':

    print('Выход из программы: q')
    while True:
        number_input = input(f'Введите два числа через пробел\n')
        if number_input == "q":
            exit()
        try:
            a, b = number_input.split()
            a, b = float(a), float(b)
            if b == 0:
                raise DevideZeroException('Деления на 0 невозможно')
            print(a / b)

        except DevideZeroException as ex:
            print(ex)
            continue
        except ValueError:
            print('Ошибка введенно не число')
            continue
