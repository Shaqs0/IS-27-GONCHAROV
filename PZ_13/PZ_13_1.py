#В6 В матрице элементы первого столбца возвести в куб
import random

rows = 3
cols = 3

matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

print('\nИсходная матрица:')
for row in matrix:
    print(row)

def cube(x):
    return x ** 3

matrix = list(map(lambda row: [cube(row[0]), row[1], row[2]], matrix))

print('\nМатрица после возведения в куб первого столбца:')
for row in matrix:
    print(row)
    
    
    
    
    