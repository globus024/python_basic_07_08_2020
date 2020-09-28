# Azamat Khankhodjaev
# 27.09.2020
# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). # Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
import random
class Stationery:
    '''
    class Stationery (stationery). Define the title attribute in it
    # and the draw() method. # The method displays the message “starting rendering.”
    '''
    def __init__(self, title):
        self._title = title

    def get_title(self) -> str:
        '''
        returns the names of the picture title (type :str)
        :return str
        '''
        return self._title

    def draw(self) -> None:
        '''
        method for starting rendering.
        Displays information on the screen that drawing has started, the drawing method, and the name of the picture
        :return:
        '''
        print(f'Запуск отрисовки. {self} - {self.get_title()}')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def __str__(self):
        return 'Рисование ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def __str__(self):
        return 'Рисование карандашом'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def __str__(self):
        return 'Рисование маркером'

if __name__ == '__main__':
    draw_list = [Pen, Pencil, Handle]
    title_list =['Сосновый бор', 'Чёрный квадрат','Девочка на шаре']
    for dr in draw_list:
        draw = dr(random.choice(title_list))
        draw.draw()