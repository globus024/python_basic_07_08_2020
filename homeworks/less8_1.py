# Azamat Khankhodjaev
# 04.10.2020
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date_str: str) -> None:
        self.__date_str = date_str

    @classmethod
    def get_date_int(cls, param: str):
        date_str = param.split('-')
        d_int = int(date_str[0])
        m_int = int(date_str[1])
        y_int = int(date_str[2])
        return (d_int, m_int, y_int)

    @staticmethod
    def validate_date(d_int: int, m_int: int, y_int: int):
        if len(str(y_int)) != 4:
            return False
        if not (m_int > 0 and m_int < 13):
            return False
        if not (d_int > 0 and d_int < 32):
            return False
        return True

if __name__ == '__main__':
    a = Date.get_date_int('12-12-2020')
    print(Date.validate_date(*a))
