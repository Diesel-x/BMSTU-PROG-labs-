# Баянов Дияз ИУ7-14Б, Вар 39
# Написать программу, которая для заданных по варианту
# функций выведет таблицу значений этих функций на некотором отрезке
# и построит график одной из них. Программа должна позволить
# ввести начальное значение аргумента, конечное значение
# и шаг разбиения данного отрезка и вывести таблицу значений вида:
import math as m
# Параметры
step = 0.05
x_start = 0
x = x_start
x_end = 1.5
eps = 1e-7
ticks = 10       # Количество засечек
width = 80      # Ширина графика в символах
eps = 1e-7

# Вычисление значений функции и определение минимального и максимального значений
min_y = -1  # минимальное значение функции
max_y = 1   # максимальное значение функции


for x in range(int(x_start * 100), int(x_end * 100) + int(step * 100), int(step * 100)):
    x = x / 100.0
    y = x**2 - m.sin(m.pi * x)
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

# Масштабирование графика
tick_step = (max_y - min_y) / (ticks - 1)

# Вывод шкалы
print("Масштабная линейка:")
for i in range(ticks):
    tick_value = min_y + i * tick_step
    print(f"{tick_value:6.2f}", end=" ")
print(f"{max_y:6.2f}")
print(" " * 7 + "-" * width)

# Построение графика
x = x_start
while x <= x_end:
    y = m.sin(x)  # фиксированная функция sin(x)

    # Масштабирование значения y на ширину графика
    y_scaled = int((y - min_y) / (max_y - min_y) * (width - 1))

    # Определение положения оси абсцисс
    zero_position = int((0 - min_y) / (max_y - min_y) * (width - 1))

    # Печать значения x и графика
    print(f"{x:6.2f} ", end="")

    if y_scaled == zero_position:
        print(" " * y_scaled + "*", end="")
    elif y_scaled > zero_position:
        print(" " * zero_position + "|" + " " *
              (y_scaled - zero_position - 1) + "*", end="")
    else:
        print(" " * y_scaled + "*" + " " *
              (zero_position - y_scaled - 1) + "|", end="")

    print()  # Перенос строки для нового значения x

    x += step
