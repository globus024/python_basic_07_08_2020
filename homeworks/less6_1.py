# Azamat Khankhodjaev
# 25.09.2020
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый)
# — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
import time
from datetime import datetime
from typing import List


class TrafficLight:
    __mode = ('красный', 'желтый', 'зеленый')
    __color = None
    __start_timer = 0.0

    def __init__(self):
        self.__set_timer()

    def __set_timer(self):
        now = datetime.now()
        self.__start_timer = datetime.timestamp(now)

    def get_timer(self) -> float:
        return self.__start_timer

    def _set_mode(self, color) -> None:
        if not color in self.__mode:
            raise ValueError('Параметр указан не верно')

        now = datetime.now()
        current_timer = datetime.timestamp(now)
        diff = (current_timer - self.get_timer()) % 15

        if color == 'красный':
            if not (diff >= 0 and diff < 7):
                raise ValueError('Режим передан не верно')
        elif color == 'желтый':
            if not (diff >= 7 and diff < 9):
                raise ValueError('Режим передан не верно')
        elif color == 'зеленый':
            if not (diff >= 9 and diff < 15):
                raise ValueError('Режим передан не верно')

        self.__color = color

    def get_color(self) -> str:
        return self.__color


class TrafficLightUser(TrafficLight):
    mode_timer_list = {'красный': 7, 'желтый': 2, 'зеленый': 6}

    def __init__(self, modes: List):
        super().__init__()
        self.__modes = modes

    def get_modes(self):
        return self.__modes

    def running(self) -> None:
        try:
            for mode in self.get_modes():
                self._set_mode(mode)
                print(self.get_color())
                time.sleep(self.mode_timer_list[mode])
        except ValueError as ex:
            print(ex)


if __name__ == '__main__':
    c = TrafficLightUser(['красный', 'желтый', 'зеленый', 'красный', 'желтый', 'зеленый','желтый'])
    c.running()
