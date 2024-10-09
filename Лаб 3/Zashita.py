import math

# Параметры графика
x_start = 0     # Начало отрезка
x_end = 2       # Конец отрезка
step = 0.5      # Шаг изменения аргумента
ticks = 4       # Количество засечек
width = 40      # Ширина графика в символах

# Найдём минимум и максимум функции для масштабирования
x = x_start
y_min = math.sin(x) - 0.5
y_max = y_min
while x <= x_end:
    y = math.sin(x) - 0.5
    if y < y_min:
        y_min = y
    if y > y_max:
        y_max = y
    x += step

# Вычисление диапазона значений по оси Y
y_range = y_max - y_min
tick_step = y_range / (ticks - 1)

# Выводим масштабную линейку (значения по оси Y)
y_tick = y_min
tick_width = width // (ticks - 1)
print(" " * 5, end="")
for i in range(ticks):
    print(f"{y_tick:^ {tick_width}.2f}", end="")
    y_tick += tick_step
print()

# Печать графика
x = x_start
while x <= x_end:
    y = math.sin(x) - 0.5

    # Определение позиции звёздочки на графике
    tick_position = int((y - y_min) / y_range * (width - 1))

    # Построение строки графика
    for i in range(width):
        if i == tick_position:
            print("*", end="")
        elif y_min <= 0 <= y_max and i == int((0 - y_min) / y_range * (width - 1)):
            print("|", end="")
        else:
            print(" ", end="")

    # Вывод строки с осью X
    print(f" {x:<5.1f}")

    # Переход к следующему значению x
    x += step
