# Azamat Khankhodjaev
# 12.09.2020
# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('Выход из программы: q')
while True:
    string_input = input(f'Введите несколько значений разделеные "," (Например: 1, aaaa, bbb, 22)\n')
    # string_input = string_input.strip()
    if string_input == "q":
        exit()

    if not string_input:
        print('Вы ввели пустое значение')
        continue
    else:
        change_pos_input_list = string_input.split(",")
        if len(change_pos_input_list) < 2:
            print("Вы ввели не список")
            continue
        break

input_list_count = len(change_pos_input_list);
change_pos_input_list_copy = change_pos_input_list.copy()
for pos in range(0, input_list_count, 2):
    first_el = change_pos_input_list[pos]
    next_pos = pos + 1
    if next_pos < input_list_count:
        change_pos_input_list_copy[pos] = change_pos_input_list[next_pos]
        change_pos_input_list_copy[next_pos] = first_el

print(",".join(change_pos_input_list_copy))
