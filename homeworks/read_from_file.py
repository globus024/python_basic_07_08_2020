# Azamat Khankhodjaev
# 24.09.2020

from typing import Dict, Type

def read_file(path: str,  type:Type, delimeter='') -> Dict:
    '''
    The program reads from the data file and generates a dictionary where the key is the first value in the string
    :param path: str. Full path to the file
    :param type: Type - cast to type
    :param delimeter: str. Default value delimeter whitespace
    :return:
    '''
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            string_list = {}
            for line in file:
                l = line.split() if not delimeter else line.split(str(delimeter))
                if len(l) == 2:
                    try:
                        string_list[l[0]] = type(l[1])
                    except ValueError:
                        continue
                else:
                    continue
        return string_list
    except FileNotFoundError:
        return {}