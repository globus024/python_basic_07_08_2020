# Azamat Khankhodjaev
# 09.09.2020
# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
# расчете на одного сотрудника.

income_input_string = f'Введите значения выручки\n'
income_input = input(income_input_string)

if income_input.isdigit():
    income_salary = int(income_input)
else:
    print('Введёное значения выручки не является числом')
    exit()

expense_input_string = f'Введите значения издержек\n'
expense_input = input(expense_input_string)

if expense_input.isdigit():
    expense_salary = int(expense_input)
else:
    print('Введёное значения издержек не является числом')
    exit()

diff = income_salary - expense_salary
if diff > 0:
    print(f'Ваша прибыль {diff}')
    profitability = (diff*100)//income_salary
    print(f'Ваша рентабильность {profitability}%')

    staff_input_string = f'Введите количество сотрудников\n'
    staff_input = input(staff_input_string)
    if expense_input.isdigit() :
        staff = int(staff_input)
        staff_profit = diff/staff
        print(f'Прибыль фирмы в расчете на одного сотрудника {staff_profit}')
    else:
        print('Введёное значения издержек не является числом')
else:
    print(f'Ваш убыток {diff}')


