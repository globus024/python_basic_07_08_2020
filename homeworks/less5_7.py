# Azamat Khankhodjaev
# 24.09.2020
# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

from typing import List
from statistics import mean
import os, json


def read_from_file(path: str) -> List:
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            res_list = []
            for line in file:
                row = []
                l = line.split()
                if l:
                    len_l = len(l)
                    comp_name = ' '.join(l[:-3])
                    other = l[len_l - 3:len_l]
                    row.append(comp_name)
                    row.extend(other)
                    res_list.append(row)
        return res_list
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    current_path = os.path.join(os.path.dirname(__file__), 'files', 'less5_7.txt')
    ll = read_from_file(current_path)
    res, avg_dict = {}, {}

    company_list = []
    if ll:
        for l in ll:
            try:
                name, incoming, outlay = l[0], float(l[2]), float(l[3])
                diff = incoming - outlay
                res[name] = diff
            except IndexError:
                continue
            except ValueError:
                continue
        if res:
            vals = res.values()
            loc_average = round(mean(list(vals)), 2)
            avg_dict['average_profit'] = loc_average
            company_list = [res, avg_dict]

            path = os.path.join(os.path.dirname(__file__), 'files', 'my_file.json')
            with open(path, "w", encoding='UTF-8') as write_f:
                json.dump(company_list, write_f, ensure_ascii=False)
