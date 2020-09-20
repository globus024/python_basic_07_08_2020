# Azamat Khankhodjaev
# 20.09.2020
# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].


number_list = [1, 2, 44, 55, 55, 22, 8, 7, 2, 41, 56, 21, 13, 16]

position_list = [pos for pos in range(0, len(number_list), 2)
                   if number_list[pos] < number_list[pos + 1]]
new_number_list = [val for pos, val in enumerate(number_list)
                    if pos in position_list or pos-1 in position_list ]


print(new_number_list)

# for pos in range(0, len(number_list), 2):
#     if number_list[pos] > number_list[pos + 1]:
#         a.append(number_list[pos])
#         a.append(number_list[pos + 1])
#         a.remove(number_list[pos])