#Книжные магазины предлагают следующие коллекции книг.
#Магистр - Лермонтов, Достоевский, Пушкин, Тютчев
#ДомКниги - Толстой, Грибоедов, Чехов, Пушкин.
#БукМаркет - Пушкин, Достоевский, Маяковский.
#Галерея - Чехов, Тютчев, Пушкин.
#Определить в каких магазинах 
#нельзя приобрести книги Грибоедова и Маяковского

magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
home_book = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
buk_market = {'Пушкин', 'Достоевский', 'Маяковский'}
gallery = {'Чехов', 'Тютчев', 'Пушкин'}

griboedov_and_mayakovsky = {'Грибоедов', 'Маяковский'}

no_in_magazine = set()

if not (griboedov_and_mayakovsky & magistr):
    no_in_magazine.add('Магистр')

if not (griboedov_and_mayakovsky & home_book):
    no_in_magazine.add('ДомКниги')

if not (griboedov_and_mayakovsky & buk_market):
    no_in_magazine.add('БукМаркет')

if not (griboedov_and_mayakovsky & gallery):
    no_in_magazine.add('Галерея')

print("Магазины, в которых нельзя приобрести книги Грибоедова и Маяковского:", no_in_magazine)