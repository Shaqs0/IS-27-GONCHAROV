#Даны температуры за месяц март. Необходимо найти количество положительных
#и отрицательных значений температур в месяце, самую низкую и самую высокую температуры,
#а также среднемесячное значение температуры
import random

temperature = [random.randrange(-8, 20) for i in range(30)]

negative_tepmerature = len([temp for temp in temperature if temp < 0])
positive_temperature = len([temp for temp in temperature if temp >= 0])
average_temperature = sum(temperature) / len(temperature)

print(f'Список температур за месяц март {temperature};',
      f'\nКоличество положительных значений температур в месяце: {positive_temperature};',
      f'\nКоличество негативных значений температур в месяце: {negative_tepmerature};',
      f'\nСамая низкая температура за месяц: {min(temp for temp in temperature)};',
      f'\nСамая высокая температура за месяц: {max(temp for temp in temperature)};',
      f'\nСреднемесячное значение температуры в марте: {round(average_temperature, 1)}')

