#Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0

import random

def generate_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

matrix = generate_matrix(3, 3, 0, 20)

new_matrix = [[0 if element > 10 else element for element in row] for row in matrix]

print("\nИсходная матрица:")
for row in matrix:
    print(row)

print("\nНовая матрица:")
for row in new_matrix:
    print(row)
