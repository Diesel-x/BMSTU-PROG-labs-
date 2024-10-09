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
x_end = 1.5
ticks = 8       # Количество засечек
width = 80      # Ширина графика в символах

# Ввод количества засечек
ticks = int(input("Введите количество засечек (от 4 до 8): "))
while ticks < 4 or ticks > 8:
    print("Некорректное значение. Введите число от 4 до 8.")
    ticks = int(input("Введите количество засечек (от 4 до 8): "))

# Вычисление значений функции и определение минимального и максимального значений
min_y = float('inf')
max_y = float('-inf')
y2_min = float('inf')
x_min = None

for i in range(int(x_start * 100), int(x_end * 100) + int(step * 100), int(step * 100)):
    x = i / 100.0
    y = x**2 - m.sin(m.pi * x)
    y2 = 7.5 * x**4 - 11 + x**3 + 3.8 * x**2 + 0.4 * x - 0.98
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y
    if y2 < y2_min:
        y2_min = y2
        x_min = x

# Масштабирование графика
tick_step = (max_y - min_y) / (ticks - 1)

# Вывод шкалы
print(" " * 10, end="")
for i in range(ticks + 1):
    value = min_y + i * tick_step
    print(f"{value:>8.2f}", end="")
print()

# Построение графика
for i in range(int(x_start * 100), int(x_end * 100) + int(step * 100), int(step * 100)):
    x = i / 100.0
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

# Вывод минимального значения y2 и соответствующего x
print(f"\nМинимальное значение y2: {y2_min:.2f} достигается при x: {x_min:.2f}")
