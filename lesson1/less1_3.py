# Azamat Khankhodjaev
# 09.09.2020
# Homework 3:
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_input_string = f'Введите целое число\n'
number_input = input(number_input_string)
if number_input.isdigit():
    number_input = int(number_input)
    nn_number = str(number_input) + str(number_input)
    nnn_number = str(number_input) + str(number_input) + str(number_input)
    sum = number_input + int(nn_number) + int(nnn_number)
    print(f'{number_input} + {nn_number} + {nnn_number} = {sum}')
else:
    print('Вы указали не число')