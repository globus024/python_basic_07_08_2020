# Azamat Khankhodjaev
# 12.09.2020
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

print('Выход из программы: q')
while True:
    month_number_input = input(f'Введите целое число номер мясяца (1-12)\n')
    if month_number_input == "q":
        exit()
    if not month_number_input.isdigit() or int(month_number_input) < 1 or int(month_number_input) > 12:
        print('Набранная значения не является номером месяца')
        continue
    break

month_number_input = int(month_number_input)
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {'winter': 'Зима', 'spring': 'Весна', 'summer': 'Лето', 'autumn': 'Осень'}

month_number = month_number_input
# first solution
if month_number == 12:
    month_number = 0

season_part = month_number // 3
print(f'Времени года: {season_list[season_part]}')

# second solution
print('Второе решение')
month_number = month_number_input

if month_number > 2 and month_number < 6:
    month_str = season_dict['spring']
elif month_number > 5 and month_number < 9:
    month_str = season_dict['summer']
elif month_number > 8 and month_number < 12:
    month_str = season_dict['autumn']
else:
    month_str = season_dict['winter']

print(f'Времени года: {month_str}')
