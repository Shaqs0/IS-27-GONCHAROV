#В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности
#писателя (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту).
#Посчитать количество полученный элементов
import re

pattern = r'\d{4} год[ау]?'

with open('./PZ_14/Dostoevsky.txt', 'r', encoding='utf-8') as file_txt:
    text = file_txt.read()
    
matches = re.findall(pattern, text)

print("Найденные годы деятельности писателя:")
for match in matches:
    print(match)
print("Общее количество:", len(matches))