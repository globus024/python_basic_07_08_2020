# Azamat Khankhodjaev
# 24.09.2020
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re, os
from homeworks.read_from_file import read_file

if __name__ == '__main__':
    current_path = os.path.join(os.path.dirname(__file__), 'files', 'less5_6.txt')
    try:
        lessons = read_file(current_path, str, ':')
        res = {}
        if lessons:
            for les in lessons:
                line = lessons[les]
                matches = re.split(r'\D', line)
                cnt = 0
                if matches:
                    for m in matches:
                        try:
                            cnt += int(m)
                        except ValueError:
                            continue
                res[les] = cnt
            print(res)
        else:
            print('Не найдено не одного предмета')
    except:
        print('Не удалось прочитать файл')
