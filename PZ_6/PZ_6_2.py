#Дан список A размера N. Сформировать два новых списка B и C: в список B записать все положительные элементы список A, в список 
#C - все отрицательные (сохраняя исходный порядок следования элементов). Вывести вначале размер и содержимое списка B, а затем - размер и содержимое списка C

def split_list(input_list):
    positive_list = [x for x in input_list if x > 0]
    negative_list = [x for x in input_list if x < 0]
    return positive_list, negative_list

A = [1, 4, 8, -10, 11, 2, -6]

B, C = split_list(A)

print(f"Размер списка B: {len(B)}, Содержимое списка B: {B}")
print(f"Размер списка C: {len(C)}, Содержимое списка C: {C}")