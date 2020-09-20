# Azamat Khankhodjaev
# 20.09.2020
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами
import sys


def staff_salary(pay_hours: float, hours: int) -> float:
    '''
    This function of the employee's salary
    :param pay_hours: float - rate per hour
    :param hours: int - working hours
    :return: ->float (working hours * rate per hour) + bonus.
    bonus - the bonus is calculated based on working hours, more than 160 hours per month +20% of salary
    '''

    bonus = pay_hours * hours * 0.2 if hours > 160 else 0

    return (pay_hours * hours) + bonus


if __name__ == '__main__':
    try:
        _, hours, pay_hours = sys.argv
        hours = int(hours)
        pay_hours = float(pay_hours)
        salary = staff_salary(pay_hours, hours)
        print(f'Зарплата сотрудника с учётом бонуса: {salary}')
    except ValueError:
        print('Входные параметры неверны')
