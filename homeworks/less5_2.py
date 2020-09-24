# Azamat Khankhodjaev
# 23.09.2020
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
import os

if __name__ == '__main__':
    try:
        path = os.path.join(os.path.dirname(__file__),'files', 'less5_2.txt')
        with open(path, 'r', encoding='UTF-8') as file:
            word_cnt_list = []
            for f in file:
                word_count = f.split()
                if word_count:
                    word_cnt_list.append(len(word_count))

            if word_cnt_list:
                print(f'Количество строк: {len(word_cnt_list)}')
                for i, cnt in enumerate(word_cnt_list):
                    row = i + 1
                    print(f'Строка {row}, количество слов - {cnt}')
            else:
                print(f'Количество строк: 0\nКоличество слов 0')

    except FileNotFoundError:
        print('Не удалось обнаружить файл')
