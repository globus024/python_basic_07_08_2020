# Azamat Khankhodjaev
# 04.10.2020
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
from abc import ABC, abstractmethod


class Warehouse:
    __items = {}

    def __init__(self, ):
        pass


class OfficeEquipment(ABC):
    __name = 'Офисная техника'
    _comp_interface = True
    _cartridge = True
    _matrix = True


    @abstractmethod
    def __init__(self, name: str, count: int):
        if not isinstance(count,int):
            str = f'Количество {name} должно быть целое число'
            raise ValueError(str)
        self.__name = name
        self.__count = count
        super().__init__()

    def get_count(self):
        return self.__count

    def get_name(self) -> str:
        return self.__name

    def get_cardridge(self) -> bool:
        return self._cartridge

    def get_matrix(self) -> bool:
        return self._matrix

    def get_comp_interface(self) -> bool:
        return self._comp_interface


class Printer(OfficeEquipment):
    def __init__(self, count, colored):
        colored_list = ('цветной', 'монохромный')
        if colored.lower() in colored_list:
            self.__colored = colored
        else:
            raise ValueError('тип печати неверный')

        super().__init__('printer', count)
        self._matrix = False

    def __str__(self):
        return 'принтер'


class Scaner(OfficeEquipment):
    def __init__(self,  count):
        super().__init__('scaner', count)
        self._cartridge = False

    def __str__(self):
        return 'сканер'


class Xerox(OfficeEquipment):
    def __init__(self, count):
        super().__init__('xerox', count)
        self._comp_interface = False

    def __str__(self):
        return 'ксерокс'


if __name__ == '__main__':
    a = Xerox( 12)
    print(a.get_name())
    print(isinstance(a, OfficeEquipment))
