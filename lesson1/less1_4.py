# Azamat Khankhodjaev
# 09.09.2020
# Homework 4:
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number_input_string = f'Введите целое число\n'
number_input = input(number_input_string)

if number_input.isdigit():
    number = int(number_input)
    prev_char = 0
    max_number = number
    while number:
        last_char = number % 10
        number = number // 10
        if last_char > prev_char:
            max_number = last_char
            prev_char = last_char
        else:
            max_number = prev_char
    else:
        print(f'Самая большая цифра в числе {number_input} - {max_number}')
else:
    print('Вы указали не число')
