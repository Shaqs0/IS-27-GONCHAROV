#Даны три словаря на три элемента каждый. Объединить все словари в один. Вывести исходные словари и результирующий.

first_dict = {'one': 1, 'two': 2, 'three': 3}
second_dict = {'four': 4, 'five': 5, 'six': 6}
third_dict = {'seven': 7, 'eight': 8, 'nine' : 9}

try:
    def merge(dictionaries):
        result = {}
        for dictionary in dictionaries:
            for key, value in dictionary.items():
                if key in result:
                    result[key].add(value)
                else:
                    result[key] = {value}
        return result
    
    result = merge([first_dict, second_dict, third_dict])
    
    print(f'Исходные словари:\n{first_dict};\n{second_dict};\n{third_dict};\nРезультирующий словарь:\n{result}')
except ValueError:
    print('Ошибка')