# Azamat Khankhodjaev
# 26.09.2020
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    '''
    Road class, in which to define the attributes: length (length), width (width).
    Defines the method for calculating the mass of asphalt required to
    Cover the entire roadbed according to the formula use the formula:
    length * width * mass of asphalt to cover one square meter of road with asphalt,
    1 cm thick * Chi slo cm thickness of the roadbed
    '''

    def __init__(self, length: float, width: float):
        self.__length = float(length)
        self.__width = float(width)

    def get_weight(self, weight_for: float, layer: float) -> float:
        '''
        :param weight_for: float parameter. mass of asphalt for covering one square meter of road with asphalt, 1 cm thick
        :param layer: float parameter. the thickness of the coating asphalt
        :return: float.  the mass of asphalt
        '''
        return round((self.__width * self.__length * float(weight_for) * float(layer)) / 1000, 2)


if __name__ == '__main__':

    try:
        road = Road('10000', 25)
        print(f'Масса асфальта: {road.get_weight(25, 5)} т')
    except ValueError:
        pass
