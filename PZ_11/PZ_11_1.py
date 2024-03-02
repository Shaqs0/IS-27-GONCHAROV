#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел.
#Сформировать новый текстовый файл (.txt) следующего вида, предварительно
#Выполнив требуемую обработку элементов:

#Исходные данные
#Количество элементов
#Произведение элементов
#Повторяющиеся элементы
#Количество повторяющихся элементов
#Элементы больше 5 увеличены в два раза

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 6, -3, -2, -1]
with open('input.txt', 'w') as f:
    for num in numbers:
        f.write(str(num) + '\n')

with open('input.txt', 'r') as f:
    lines = f.readlines()
    numbers = [int(line.strip()) for line in lines]

count = len(numbers)

product = 1
for num in numbers:
    product *= num

repeated_elements = {}
for num in numbers:
    if num not in repeated_elements:
        repeated_elements[num] = 1
    else:
        repeated_elements[num] += 1

filtered_numbers = [num for num in numbers if num > 5]

with open('output.txt', 'w') as f:
    f.write(f'Исходные данные: {numbers}\n')
    f.write(f'Количество элементов: {count}\n')
    f.write(f'Произведение элементов: {product}\n')
    f.write(f'Повторяющиеся элементы: {repeated_elements}\n')
    f.write(f'Количество повторяющихся элементов: {repeated_elements}\n')
    f.write(f'Элементы больше 5 увеличены в два раза: {filtered_numbers}\n')
