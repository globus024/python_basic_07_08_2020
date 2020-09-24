# Azamat Khankhodjaev
# 23.09.2020
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from functools import reduce
import os
from homeworks.read_from_file import read_file

if __name__ == "__main__":
    try:
        path = os.path.join(os.path.dirname(__file__), 'files', 'less5_3.txt')
        staffs = read_file(path, float)
        staffs_more_amt = {}
        if staffs:
            staffs_more_amt = [key for key in staffs if staffs[key] < 20000]
            salary_list = [staffs[key] for key in staffs]
            salary_avg = round(reduce(lambda x, y: x + y, salary_list) / len(salary_list), 2)
            if staffs_more_amt:
                print(f'Оклад сотрудников менее 20 тыс: {", ".join(staffs_more_amt)}')

            print(f'Средняя величина дохода сотрудников: {salary_avg}')
        else:
            print('Формат файла не верный, либо пустой')
    except:
        print('Что-то пошло не так, извините')
