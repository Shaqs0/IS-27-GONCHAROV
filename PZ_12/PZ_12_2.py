#Составить генератор (yield), который преведет символы строки из
#верхнего регистра в нижний

string = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
def generation(string):
    for symbol in string:
        yield symbol.lower()


total_stirng = ''.join(generation(string))

print(f'\nДана строка: {string}\nСтрока, переведённая из верхнего регистра в нижний: {total_stirng}\n')    