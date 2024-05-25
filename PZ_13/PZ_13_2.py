#Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0

import random

rows = 3
cols = 3
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

print('\nИсходная матрица:')
for row in matrix:
    print(row)

def cube_first_column(row):
    return [row[0] ** 3] + row[1:]

matrix = list(map(cube_first_column, matrix))

print('\nМатрица после возведения в куб первого столбца:')
for row in matrix:
    print(row)