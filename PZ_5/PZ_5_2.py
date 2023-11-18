#В6 Описать функцию InvertDigits(K), меняющую порядок следования цифр целого положительного числа K на обратный (K - параметр целого типа,являющийся одновременно входным и выходным).
# С помощью этой функции поменять порядок следования цифр на обратный для каждого из пяти данных целых чисел.


def InvertDigits(K):
    reversed_str = str(K)
    return reversed_str[::-1]  

try:
    print(InvertDigits(9406))
    print(InvertDigits(3474))
    print(InvertDigits(1112))
    print(InvertDigits(4326))
    print(InvertDigits(7453))

except:
    print('Нужно ввести целое положительное число!')