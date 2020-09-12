# Azamat Khankhodjaev
# 12.09.2020
# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
print('Необходимо ввести 4 товарных позиций')
print('Выход из программы: q')

character_name_list = ['наименование товара', 'цена', 'количество', 'eд']
character_dict = {}
result_list = []
for i in range(1, 5):
    print(f'Товарная позиция №{i}')
    for character in character_name_list:
        while True:
            character_input = input(f'Введите {character}\n')
            if character_input == 'q':
                exit()
            if (character == 'цена' or character == 'количество') and not character_input.isdigit():
                print(f'{character}: значения должно быть число')
                continue
            character_dict[character] = character_input
            break
    character_dict_copy = character_dict.copy()
    result_list.append((i, character_dict_copy))

print('-'*50)
print('Результирующий список')
print(result_list)

# analitics block
print('-'*50)
print('Блок аналитики')
analitics_dict = {}
for default in character_name_list:
    analitics_dict.setdefault(default, [])

if result_list:
    for row in result_list:
        key, val = list(row)
        for character in character_name_list:
            vv = analitics_dict[character]
            vv.append(val[character])
            if character in 'eд':
                vv = list(set(vv))
            analitics_dict.update({character: vv})

print(analitics_dict)
