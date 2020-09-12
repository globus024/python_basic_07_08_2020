# Azamat Khankhodjaev
# 12.09.2020
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
while True:
    string_input = input(f'Введите несколько слов\n')
    string_input_list = string_input.split()
    if len(string_input_list) < 2:
        print("Вы ввели только одно слово")
        continue
    break

for pos, word in enumerate(string_input_list):
    pos += 1
    if len(word) > 10:
        word = word[0:10]
    print(f'{pos}) {word}')
