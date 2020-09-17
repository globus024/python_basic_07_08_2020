# Azamat Khankhodjaev
# 17.09.2020
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

from typing import Text, Dict, Callable


# first solution
def int_func(word: Text) -> Text:
    return word.title()


# second solution
def chars_dict() -> Dict:
    dic = {
        'a': 'A',
        'b': 'B',
        'c': 'C',
        'd': 'D',
        'e': 'E',
        'f': 'F',
        'g': 'G',
        'h': 'H',
        'i': 'I',
        'j': 'J',
        'k': 'K',
        'l': 'L',
        'm': 'M',
        'n': 'N',
        'o': 'P',
        'q': 'Q',
        'r': 'R',
        's': 'S',
        't': 'T',
        'u': 'U',
        'v': 'V',
        'w': 'W',
        'x': 'X',
        'y': 'Y',
        'z': 'Z',
        'а': 'А',
        'б': 'Б',
        'в': 'В',
        'г': 'Г',
        'д': 'Д',
        'е': 'Е',
        'ё': 'Ё',
        'ж': 'Ж',
        'з': 'З',
        'и': 'И',
        'й': 'Й',
        'к': 'К',
        'л': 'Л',
        'м': 'М',
        'о': 'О',
        'п': 'П',
        'р': 'Р',
        'с': 'С',
        'т': 'Т',
        'у': 'Н',
        'ф': 'Ф',
        'х': 'Х',
        'ц': 'Ц',
        'ш': 'Ш',
        'щ': 'Щ',
        'ь': 'Ь',
        'ы': 'Ш',
        'ъ': 'Ъ',
        'э': 'Э',
        'ю': 'Ю',
        'я': 'Я',
    }

    return dic


def int_func2(word: Text) -> Text:
    char_list = chars_dict()
    chr_get = char_list.get(word[0])
    first_chr = chr_get if chr_get else word[0]
    return f'{first_chr}{word[1:]}'


def letter_title(letter: Text, func: Callable) -> Text:
    letter_list = letter.split()
    res = []
    for word in letter_list:
        res.append(func(word))
    new_letter = ' '.join(res)
    return new_letter


if __name__ == '__main__':
    letter = letter_title('chr() method takes a single parameter, an integer', int_func)
    print(letter)
    letter = letter_title('chr() method takes a single parameter, an integer', int_func2)
    print(letter)
