#В7 Дана строка, содержащая полное имя файла, то есть имя диска,
#список каталогов (путь), собственно имя и расширение. Выделить
#из этой строки расширение файла (без предшествующей точки).
import re

str = '/home/shaqs/project/main.js, /home/shaqs/project/index.html, /home/shaqs/project/style.css '
pattern = r'(?<=.)[a-z]+(?=,| )'

print('Строка: ', {str}, '\nРасширения из данной строки: ', re.findall(pattern, str))
