# Azamat Khankhodjaev
# 04.10.2020
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
from homeworks.less8_4 import OfficeEquipment, Printer, Scaner, Xerox


class Warehouse:
    __items = {}
    __departament_equipment = {}

    def add_warehouse(self, office_equipment: OfficeEquipment):
        if not isinstance(office_equipment, OfficeEquipment):
            raise ValueError('the object does not belong to the class OfficeEquipment')
        cnt = office_equipment.get_count()
        name = office_equipment.get_name()
        try:
            self.__items[name] = {'count': cnt + self.__items[name]['count']}
        except KeyError:
            self.__items[name] = {'count': cnt}

    def get_count(self, name):
        try:
            return self.__items[name]['count']
        except KeyError:
            return 0

    def give_deportament(self, deportament: str, office_equipment: OfficeEquipment):
        if not isinstance(office_equipment, OfficeEquipment):
            raise ValueError('the object does not belong to the class OfficeEquipment')
        name = office_equipment.get_name()
        cnt = office_equipment.get_count()
        if self.get_count(name) >= cnt:
            self.__items[name]['count'] -= cnt
            if self.get_count(name) == 0:
                del self.__items[name]
        try:
            self.__departament_equipment[deportament] = {name: self.__departament_equipment[deportament] + cnt}
        except KeyError:
            self.__departament_equipment[deportament] = {name: cnt}

    def get_warehouse(self):
        return self.__items

    def get_depor_items(self):
        return self.__departament_equipment

if __name__ == '__main__':
    p = Printer(12, 'цветной')
    p2 = Scaner(12)
    p3 = Xerox(21)
    w = Warehouse()
    w.add_warehouse(p)
    w.add_warehouse(p)
    w.add_warehouse(p)
    w.add_warehouse(p2)
    w.add_warehouse(p3)

    print(w.get_warehouse())
    w.give_deportament('it',p)
    print(w.get_depor_items())
    print(w.get_warehouse())