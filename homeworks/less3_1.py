# Azamat Khankhodjaev
# 16.09.2020
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devide_number(first_number: float, second_number: float) -> float:
    return first_number / second_number


print('Программа делить первое число на второе')
print('Выход из программы: q')
first_number, second_number = 0, 0
while True:
    if not first_number:
        first_number_input = input(f'Введите первое число:\n')
        if first_number_input.lower() == 'q':
            exit()
    try:
        first_number = float(first_number_input)
        second_number_input = input(f'Введите второе число:\n')
        if second_number_input.lower() == 'q':
            exit()
        second_number = float(second_number_input)
        print(devide_number(second_number=second_number, first_number=first_number))
    except ValueError:
        print('Ошибка: Введённое значение не является числом')
        continue
    except ZeroDivisionError:
        print('Ошибка: Деления на ноль запрещено')
        continue
    # if not first_number_input.isdigit():
    #     print('Первое значение не является числом')
    #     continue

    # if not second_number_input.isdigit():
    #     print('Второе значение не является числом')
    #     continue

    break
