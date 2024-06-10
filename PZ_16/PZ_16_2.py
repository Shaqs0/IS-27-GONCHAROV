# Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.


class Animal:
    def __init__(self, animal_class, years_old):
        self.who = animal_class
        self.years_old = years_old

class Dog(Animal):
    def __init__(self, who, years_old, breed):
        super().__init__(who, years_old)
        self.breed = breed

class Cat(Animal):
    def __init__(self, animal_class, years_old, breed):
        super().__init__(animal_class, years_old)
        self.breed = breed

try:
    animal_class = input('Введите вид животного: ')
    years_old = int(input('Введите возраст животного: '))
    animal = Animal(animal_class, years_old)
    print('\n', animal.__dict__)

    years_old = int(input('Введите возраст собаки: '))
    breed = input('Введите породу собаки: ')
    dog = Dog('Собака', years_old, breed)
    print('\n', dog.__dict__)

    years_old = int(input('Введите возраст кошки: '))
    breed = input('Введите породу кошки: ')
    cat = Cat('Кот', years_old, breed)
    print('\n', cat.__dict__)
except:
    print('Введены неверные данные')