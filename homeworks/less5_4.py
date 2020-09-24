# Azamat Khankhodjaev
# 23.09.2020
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

from homeworks.read_from_file import read_file
from homeworks.write_to_file import write_file
import os

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    path = os.path.join(current_path,'files', 'less5_4.txt')
    new_path = os.path.join(current_path,'files' ,'less5_4_ru.txt')
    en_num_list = read_file(path, int, '-')
    number_list = [en_num_list[key] for key in en_num_list]
    ru_num_spell_list = {1: 'Раз', 2: 'Два', 3: 'Три', 4: 'Четыри'}
    result_list = []
    for number in number_list:
        try:
            string = f'{ru_num_spell_list[number]} - {number}'
            result_list.append(string)
        except:
            continue
    if result_list:
        text = '\n'.join(result_list)
        if write_file(new_path,text):
            print('Данные успешно сохранены')
        else:
            print('Не удалось записать в файл')
    else:
        print(f'Соответсвие списка с файлом не обнаружена')