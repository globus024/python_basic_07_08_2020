# Azamat Khankhodjaev
# 17.09.2020
# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def is_number(*args) -> bool:
    try:
        for i in args:
            i = float(i)
        return True
    except ValueError:
        return False


def sum_number(*args) -> float:
    try:
        number = 0
        for n in args:
            n = float(n)
            number += n
    except ValueError:
        pass
    return number


number = 0
print('Чтобы завершить программу нажмите q')
while True:
    number_list_input = input(f'Введите через пробел несколько чисел\n')
    if number_list_input.lower() == 'q':
        break
    number_list = number_list_input.split()

    number += sum_number(*number_list)
    if not is_number(*number_list):
        break
    print(number)
print(number)
