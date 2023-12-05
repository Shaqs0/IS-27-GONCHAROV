#В6 Дан список размера N. Возвести в квадрат все его локальные минимумы
#(то есть числа, меньшие своих соседей).

def find_local_minima(lst):
    n = len(lst)
    if n < 3:
        return []  

    minima_list = []

    for i in range(1, n - 1):
        if lst[i - 1] > lst[i] < lst[i + 1]:
            minima_list.append(lst[i] ** 2)

    return minima_list

original_list = [4, 2, 1, 3, 5, 1, 7, 2, 8]
local_minima_list = find_local_minima(original_list)

print("Исходный список:", original_list)
print("Локальные минимумы:", local_minima_list)