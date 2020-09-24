# Azamat Khankhodjaev
# 22.09.2020
# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
import os
from typing import List
from homeworks.write_to_file import write_file

def input_msg(msg=[]) -> List:
    '''
    The program asks the user to enter any text until an empty string is entered
    :param msg: List. List of strings entered by the user
    :return: List. List of strings entered by the user
    '''
    try:
        text = input(f'Введите произвольный текст (Закончить ввод пустая строка):\n')
        if not text:
            return msg
        else:
            msg.append(text)
            return input_msg(msg)
    except:
        return []


if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__),'files', 'new.txt')
    msg = input_msg()
    if msg:
        text = '\n'.join(msg)
        if write_file(path, text):
            print('Данные успешно сохранены')
        else:
            print('Не удалось записать данные в файл')
    else:
        print('Отсутствуют данные для записи')
