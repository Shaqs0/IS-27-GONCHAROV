#В6 Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов.

def print_string(numbers_of_symbols):
    return f'{"*" * numbers_of_symbols} - количество символов: {numbers_of_symbols}'

try:
    count_symbols = int(input('Введите число символов: '))
    print(print_string(count_symbols))
except ValueError:
    print('Нужно ввести число!')