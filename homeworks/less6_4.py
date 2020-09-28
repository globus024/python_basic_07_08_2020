# Azamat Khankhodjaev
# 26.09.2020
# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import random


class Car:
    '''
    the base class Car. the following attributes are defined: speed, color, name, is_police (Boolean)
    consists of methods: go(), stop(), turn(), and getter methods
    '''
    def __init__(self, speed: float, color: str, name: str, is_police=False) -> None:
        self._speed = speed
        self.__color = color
        self.__name = name
        self.__is_police = is_police

    def go(self) -> None:
        print('Поехали!')

    def stop(self) -> None:
        print('Остановились!')

    def turn(self, direction) -> None:
        direction_list = {'left': 'на лево', 'right': 'на права'}
        if direction != 'left' and direction != 'right':
            raise ValueError(f'{direction} - Автомобиль может повернуть либо на лево, либо на права')
        print(f'Повернул {direction_list[direction]}')

    def show_speed(self) -> float:
        return self._speed

    def get_color(self) -> str:
        return self.__color

    def get_name(self) -> str:
        return self.__name

    def is_police(self) -> bool:
        return self.__is_police


class TownCar(Car):
    '''
    inherits a car from the base class Car
    overide method show_speed()
    '''
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self._speed > 60:
            raise ValueError('Вы привысили скорость. Допустимаяя скорость 60км/час')
        return self._speed

    def __str__(self):
        return 'Городской автомобиль'


class SportCar(Car):
    '''
       inherits a car from the base class Car
    '''
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)

    def __str__(self):
        return 'Спорткар'


class WorkCar(Car):
    '''
       inherits a car from the base class Car
       overide method show_speed()
    '''
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self._speed > 40:
            raise ValueError('Вы привысили скорость. Допустимаяя скорость 40км/час')
        return self._speed

    def __str__(self):
        return 'Служебный автомобиль'


class PoliceCar(Car):
    '''
          inherits a car from the base class Car
    '''
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, True)

    def __str__(self):
        return 'Полицейский автомобиль'


if __name__ == '__main__':
    color_list = ['красная', 'белая', 'синяя', 'черная', 'жёлтая']
    direction_list = ['left', 'right', 'drift']
    name_list = ['Chevrolet Nexia R3', 'Lada Granta', 'Kamaz', 'UAZ', 'Bugatti Veron']
    car_list = [TownCar, SportCar, WorkCar, PoliceCar]
    for car in car_list:
        print('-' * 50)
        c = car(random.randint(30, 100), random.choice(color_list), random.choice(name_list))
        print(c)
        print(f'Марка автомобиля: {c.get_name()}')
        print(f'Цвет автомобиля: {c.get_color()}')
        c.go()
        try:
            print(f'Скорость автомобиля {c.show_speed()}')
        except Exception as ex:
            print(ex)
        try:
            c.turn(random.choice(direction_list))
        except Exception as ex:
            print(ex)

        c.stop()
        if c.is_police():
            print('Полицеский автомобиль')
