#В6 Даны целые числа  A и B. Сформировать и вывести целочисленный список
#размера 10, первый элемент которого равен A, второй равен B, а каждый последующий
#элемент равен сумме всех предыдущих.

def generate_list(a, b):
    result = [a, b] 
    for _ in range(1, 10):
        next_elem = a + b 
        result.append(next_elem) 
        a, b = b, next_elem
    return result

A = 3
B = 4

if A > 2 and B > 2:
    lst = generate_list(A, B)
    print("Сформированный список: ", lst)
else:
    print("Числа A и B должны быть больше 2.")