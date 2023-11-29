#В6 Дан список размера N. Возвести в квадрат все его локальные минимумы
#(то есть числа, меньшие своих соседей).

def square_local_min(lst):
    result = []
    for i in range(1, len(lst) - 1):
        if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
            result.append(lst[i]**2)
    return result

lst = [3, 2, 5, 1, 4, 6]
squared_local_mins = square_local_min(lst)
print(squared_local_mins)