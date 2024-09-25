# Баянов Дияз Гайсаевич ИУ7-14Б
# Лаб работа №2; Часть 2 Задание 2; Вариант 3

# Подключение библиотек
import math as m

# Ввод данных
x = float(input(f"Введите x: "))
y = float(input(f"Введите y: "))

#Вычисление
isOnArea = False
# красная линия
if -2 < x < 0:
    if y >= x and y >= x ** 2 - 6:
        isOnArea = True
# синяя линия
elif 0 <= x <= 2:
    if y >= -x and y >= x ** 2 - 6:
        isOnArea = True

elif -3 <= x <= 3:
    upper_boundary = m.sqrt(9 - x**2) + 3
    
    # Для x > 2 или x < -2, проверяем на параболу (фиолетовая дуга)
    if abs(x) > 2:
        lower_boundary = x**2 - 6
    # Внутри ломаной (между -2 и 2), проверяем по ломаной (красная и синяя линии)
    else:
        lower_boundary = -x if x >= 0 else x
    
    # Точка должна быть между верхней и нижней границей
    if lower_boundary <= y <= upper_boundary:
        isOnArea = True

# Вывод
print("Точка принадлежит области" if isOnArea else "Точка не принадлежит области")


