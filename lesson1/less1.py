# Azamat Khankhodjaev
# 09.09.2020
# Homework 1:
#1. Поработайте с переменными, создайте несколько, выведите на экран,
#  запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = "Azamat"
age = 36
is_male = True

print('Меня зовут ', name)
print(f'Мне {age} лет')
# print(is_male)

input_string = f'Как Вас зовут?\n'
name_input = input(input_string)
if name_input.isalpha():
    print('Привет, ', name_input)
else:
    print('Вас так назвали родители?')
    exit()

city_input = input(f'В каком городе Вы живёте?\n')
if city_input.isalpha():
    print(f'Вы живёте в {city_input}')
else:
    print(f'Такого города не существует!')
    exit()

age_input_string = f'Сколько Вам лет? \n'
age_input = input(age_input_string)
if age_input.isdigit() and int(age_input) > 0 and int(age_input) < 150:
    age_input = int(age_input)
    if age > age_input:
        diff = age - age_input
        text = f'Вам {age_input}, я старше Вас на {diff}'
    elif age < age_input:
        diff = age_input - age
        text = f'Вам {age_input}, Вы старше меня на {diff}'
    else:
        text = f'Вам {age_input}, Мы ровесники'

    if age != age_input:
        diff_str = str(diff)
        diff_len = len(diff_str)
        diff_last_sym = diff_str[diff_len - 1]
        diff_last_sym_int = int(diff_last_sym)
        if diff_last_sym_int > 1 and diff_last_sym_int < 5:
            age_letter = 'года'
        else:
            if diff_last_sym_int ==1:
                age_letter = 'год'
            else:
                age_letter = 'лет'
    else:
        age_letter =''

    print(text, age_letter)
else:
    if age_input.isdigit() and int(age_input) > 130:
        print('Вы Дункан Маклауд!!!')
        exit()
    else:
        print('Вы указали не правильный возраст')
        exit()

number_input = input(f'Загодайте целое число от 1 до 100\n')
if number_input.isdigit():
    number_input = int(number_input)
    if number_input >= 1 and number_input <= 100:
        print(f'Ваше число ', number_input)
    elif number_input < 1:
        print('Ваше число меньше 1')
    else:
        print('Ваше число больше 100')
else:
    if number_input.isdecimal():
        print('Вы указали не целое число')
        exit()
    else:
        print('Вы указали не число')
