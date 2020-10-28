# Методы строк

# text = 'Hello ma Nigga'
# print(text.split('_'))

# Метод isdigit проверяет все ли символы в строке числа
# num = (input('Ввведите число: '))
# print(num.isdigit)


#method is alpha проверяет все ли символы в строке буквы
# text = input("Введите текст: ")
# print(text.isalpha())

#method isalnum проверяет все ли символы цифры и буквы
# new_text = input("Введите данные: ")
# print(new_text.isalnum())

# Метод replace заменяет часть строки
# stry = 'Hello World'
# print(stry.replace('Hello', 'Nigga'))


# # Метод isupper проверяет все ли символы в верхнем регистре
# text = input('input: ')
# print(text.isupper())

# Метод islower проверяет все ли символы в верхнем регистре
# text = input('input: ')
# print(text.islower())


# Метод isspace() проверяет все ли пробелы, табы либо перевод строки
# text = input('Input: ')
# print(text.isspace())

# istitle проверяет являутся ли первыя буква в строке заглавной
# text = input('Input: ')
# print(text.istitle())

# Методы lower() and upper() перевод букв в верхний или нижний
# text = input('Введите данные: ')
# if text.islower():
#     print(text.upper())
# else:
#     print(text.lower())

# Метод startswith проверяет начинается ли строка с опред. символов
# some_text = input('Введите текст: ').lower()
# print(some_text.startswith('а'))

# Метод  endswith проверяет заканчивается ли строка на какие то символы
# mail = input('Введите данные: ')
# if mail.endswith('@gmail.com'):
#     print('Это gmail!')
# elif mail.endswith('@mail.ru'):
#     print('Это email!')
# else:
#     print(f'Программа не распознает этот {mail} email')


# Метод join склеивает строку
# names = ['John', 'Raychel', 'Peter']
# text = '...'.join(names)
# print(text)

# Метод ord узнать индекс символа  в глобальной таблице (ASCII)
# print(ord('F'))

# Метод count считает колличество символов которые передаем в скобках
# text = 'Hello World'
# print(text.count('l'))

# Метод strip удаляет лишнии пробелы вначале и конце строки (Lstrip пробелы слева, Rstrip пробелы справа)
# strip = input('Введите данные: ')
# print(strip.strip())

# Метод swapcase меняет регистр букв на противоположный
# text = input('Введите текст: ')
# print(text.swapcase())


# Срезы строк
# text = 'Hello World'
# print(text[0:6:2])
