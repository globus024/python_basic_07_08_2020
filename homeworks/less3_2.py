# Azamat Khankhodjaev
# 17.09.2020
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def contact_info(name: str, last_name: str, birth_year: int, city: str, email='', phone='') -> str:
    return f'{name} {last_name} {birth_year} {city} {email} {phone}'


if __name__=='__main__':
    users = [
        {'name': 'Boris', 'last_name': 'Britva', 'city': 'London', 'birth_year': '1976', 'phone': '+44 (0) 20 7229 64 12',
         'email': 'borisb@mail.ru'},
        {'name': 'Mihail', 'last_name': 'Jvaneckiy', 'phone': '8 800 700-68-41', 'city': 'Moskva', 'birth_year': '1934',
         }
    ]
    for user in users:
        print(contact_info(**user))
