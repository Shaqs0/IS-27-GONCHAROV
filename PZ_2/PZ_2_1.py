#Дано расстояние L В САНТИМЕТРАХ, Используя операцию деления нацело, найти количество полных метров в нём

try:
    L = int(input('Введите расстояние L в сантиметрах: '))
    print(f'Вы ввели {L} сантиметров\nКоличество полных метров в расстоянии L = {L//100}')
except ValueError:
    print('Нужно ввести число!')