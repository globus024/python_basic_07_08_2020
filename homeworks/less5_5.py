# Azamat Khankhodjaev
# 24.09.2020
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint
from functools import reduce
from homeworks.write_to_file import write_file
import os

if __name__ == "__main__":
    number_list = [str(randint(10, 100)) for _ in range(10)]
    text = ' '.join(number_list)
    current_path = os.path.join(os.path.dirname(__file__), 'files', 'less5_5.txt')
    try:
        if write_file(current_path, text):
            with open(current_path, 'r', encoding='UTF-8') as file:
                number_str = file.read()
                number_list = []
                if number_str:
                    number_str_list = number_str.split()
                    for num in number_str_list:
                        try:
                            number_list.append(int(num))
                        except:
                            continue

                if number_list:
                    sum_numbers = reduce(lambda x, y: x + y, number_list)
                    print(f'Сумма чисел - {sum_numbers}')

    except FileNotFoundError:
        print(f'Не удалось прочитать файл')
