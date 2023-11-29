#В6 Дан список размера N. Найти максимальный из его локальных
#минимумов (локальный минимум - это элемент, которыйы меньше любого из своих соседей).

def find_local_min(lst):
    local_mins = []
    for i in range(1, len(lst) - 1):
        if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
            local_mins.append(lst[i])
    return max(local_mins)

lst = [3, 2, 5, 1, 4, 6]
max_local_min = find_local_min(lst)
print(max_local_min)