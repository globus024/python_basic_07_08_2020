# Azamat Khankhodjaev
# 12.09.2020
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

start_list = [15, 14, 13, 9, 7]
print('Выход из программы: q')
i = 0
while True:
    number_input = input(f'Введите целое число\n')
    if number_input == "q":
        exit()
    if not number_input.isdigit():
        print('Набранная значения не является целом числом')
        continue
    number = int(number_input)
    if number in start_list:
        pos = start_list.index(number)
        start_list.insert(pos, number)
    else:
        new_pos_flag = False
        first = start_list[0]
        if first < number:
            start_list.insert(0, number)
        else:
            for p, item in enumerate(start_list):
                if item < number:
                    new_pos_flag =True
                    start_list.insert(p, number)
                    break
            if not new_pos_flag:
                start_list.insert(len(start_list), number)

    print(start_list)
    if i > 10:
        break
    i += 1
