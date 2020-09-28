# Azamat Khankhodjaev
# 26.09.2020
# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        if not str(name).isalpha():
            raise ValueError('name parameter must be alfa')
        if not str(surname).isalpha():
            raise ValueError('surname parameter must be alfa')
        if not str(position).isalpha():
            raise ValueError('position parameter must be alfa')
        try:
            wage = float(wage)
        except ValueError:
            raise ValueError('wage parameter must be float')
        try:
            bonus = float(bonus)
        except ValueError:
            raise ValueError('bonus parameter must be float')

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    try:
        position = Position('Ivan', 'Ivanov', 'programer', 120999, 40000)
        print(f'Cотрудник: {position.get_full_name()}')
        print(f'Доход сотрудника: {position.get_total_income()}')
    except ValueError as ex:
        print(ex)
