#Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на одну позицию (при этом A1 перейдёт в A2, A2 - в A3,..., An - в A1)

def cyclic_shift_right(input_list):
    last_element = input_list[-1]
    
    for i in range(len(input_list) - 1, 0, -1):
        input_list[i] = input_list[i - 1]
    
    input_list[0] = last_element

A = [1, 4, 8, -10, 11, 2, -6]

cyclic_shift_right(A)


print(f"Список после циклического сдвига вправо: {A}")