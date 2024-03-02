#Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0

import random


matrix = [[random.randint(1, 20) for _ in range(3)] for _ in range(3)]

print("Исходная матрица:")
for row in matrix:
    print(row)


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 10:
            matrix[i][j] = 0


print("\nМатрица после замены элементов больше 10 на 0:")
for row in matrix:
    print(row)