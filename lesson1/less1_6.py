# Azamat Khankhodjaev
# 09.09.2020
# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.


man_distance_one_day = input(f'Сколько км пробегает спортсмен в день?\n')
if man_distance_one_day.isdigit():
    man_distance_one_day = int(man_distance_one_day)
else:
    print('Введёное значения не является числом')
    exit()

man_distance_require = input(f'Сколько км должен пробежать спортсмен в день?\n')
if man_distance_require.isdigit():
    man_distance_require = int(man_distance_require)
else:
    print('Введёное значения не является числом')
    exit()

if man_distance_one_day > man_distance_require:
    print('Спортсмен уже пробегает больше')
    exit()
elif man_distance_one_day == man_distance_require:
    print('Спортсмен уже столько пробегает в день')
    exit()

day = 1
while man_distance_one_day < man_distance_require:
    man_distance_one_day = man_distance_one_day + (man_distance_one_day * 0.1)
    day += 1
else:
    print('Необходимое количество дней -',day)
