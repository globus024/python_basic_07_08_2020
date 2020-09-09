# Azamat Khankhodjaev
# 09.09.2020
# Homework 2:
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

second_input_string = f'Введите время в секундах\n'
second_input = input(second_input_string)

if second_input.isdigit() and int(second_input) < 86400:
    second_input = int(second_input)

    hour = second_input // 3600
    min = (second_input - (hour * 3600)) // 60
    second = (second_input - (hour * 3600) - (min * 60))

    hour_str = str(hour)
    hour_len = len(hour_str)
    if hour_len < 2:
        hour_str = '0' + hour_str

    min_str = str(min)
    min_len = len(min_str)
    if min_len < 2:
        min_str = '0' + min_str

    sec_str = str(second)
    sec_len = len(sec_str)
    if sec_len < 2:
        sec_str = '0' + sec_str

    print(hour_str, min_str, sec_str, sep=':')
else:
    if (int(second_input) > 86400):
        print('Вы ввели слишком большое число')
    else:
        print('Вы ввели не секунды')
