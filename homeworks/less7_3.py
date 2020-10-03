# Azamat Khankhodjaev
# 30.09.2020
# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
# (не целочисленное) # деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества
# ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
# деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
# аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n*****.
import copy
class Cell:
    def __init__(self, cells):
        if cells <= 0:
            raise ValueError('Количество клеток должно быть больше 0')
        self.__cells = cells

    def __str__(self):
        return str(self.__cells)

    def __add__(self, other):
        return Cell(self.__cells + other.__cells)

    def __sub__(self, other):
        cells = self.__cells - other.__cells
        if cells <= 0:
           raise ValueError('Количество клеток должно быть больше 0')
        return Cell(cells)

    def __mul__(self, other):
        return Cell(self.__cells * other.__cells)

    def __truediv__(self, other):
        return Cell(self.__cells // other.__cells)

    def __lt__(self, other):
        return True if self.__cells < other.__cells else False

    def __le__(self, other):
        return True if self.__cells <= other.__cells else False

    def __eq__(self, other):
        return True if self.__cells == other.__cells else False

    def __ne__(self, other):
        return True if self.__cells != other.__cells else False

    def __gt__(self, other):
        return True if self.__cells > other.__cells else False

    def __ge__(self, other):
        return True if self.__cells >= other.__cells else False

    def make_order(self, field):
        if field <= 0:
            raise ValueError('Значения должно быть больше 0')
        rows = (self.__cells // field)+1
        cells = copy.copy(self.__cells)
        for r in range(rows):
            if cells >= field:
                print(f'{"*"*field}')
            else:
                print(f'{"*" * cells}')
            cells -= field

if __name__=='__main__':
    cell = Cell(15)
    cell.make_order(5)
    cell2 = Cell(13)
    cell2.make_order(5)
    if cell > cell2:
        print(cell-cell2)
    print(cell + cell2)
    print(cell * cell2)
    print(cell / cell2)
