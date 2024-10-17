# Баянов Дияз ИУ7-14Б, Лаб 5, Вар 39
# Написать программу, которая для заданных по варианту
# функций выведет таблицу значений этих функций на некотором отрезке
# и построит график одной из них. Программа должна позволить
# ввести начальное значение аргумента, конечное значение
# и шаг разбиения данного отрезка и вывести таблицу значений вида:
import math as m

# Ввод параметров
x_start = float(input("Введите начальное значение x: "))
x_end = float(input("Введите конечное значение x: "))
step = float(input("Введите шаг разбиения: "))

# Ввод количества засечек с проверкой на целочисленность и диапазон
while True:
    try:
        ticks = int(input("Введите кол-во засечек от 4 до 8: "))
        if 4 <= ticks <= 8:
            break
        else:
            print("Ошибка: введите число от 4 до 8.")
    except ValueError:
        print("Ошибка: введите целое число.")

width = 80  # Ширина графика в символах

print("*" * 40)
print("| {x:^11} | {y1:^11} | {y2:^11}".format(x="x", y1="y1", y2="y2"))
print("*" * 40)

min_y = float('inf')
max_y = float('-inf')
y2_min = float('inf')
x_min = float('inf')

# Построение таблицы и определение минимального и максимального значений
x = x_start
while x <= x_end:
    y1 = x**2 - m.sin(m.pi * x)
    y2 = 7.5 * x**4 - 11 + x**3 + 3.8 * x**2 + 0.4 * x - 0.98
    print(f"| {x:^10.6g} | {y1:>10.6g} | {y2:>10.6g} |")

    if y1 < min_y:
        min_y = y1
    if y1 > max_y:
        max_y = y1

    # Доп задание
    if y2 < y2_min:
        y2_min = y2
        x_min = x

    x += step

print("*" * 40)
print(f"Значение y2_min = {y2_min} при x_min == {x_min}")

# Масштабирование графика
tick_step = (max_y - min_y) / (ticks - 1)
tick_length = width // ticks

# Вывод горизонтальных засечек
value = min_y

print(" " * 7, end="")
for j in range(ticks):
    print(f"{value:^{tick_length + 1}.2f}", end="")
    value += tick_step
    print(f" ", end="")
print()

# Построение графика
x = x_start
while x <= x_end:
    y1 = x**2 - m.sin(m.pi * x)
    scaled_y = int((y1 - min_y) / (max_y - min_y) * (width - 1))

    # Вывод значения аргумента
    print(f"{x:>8.2f} |", end="")

    # Построение строки графика
    for j in range(width):
        if j == scaled_y:
            print("*", end="")
        elif min_y <= 0 <= max_y and j == int((0 - min_y) / (max_y - min_y) * (width - 1)):
            print("|", end="")
        else:
            print(" ", end="")
    print()
    x += step
