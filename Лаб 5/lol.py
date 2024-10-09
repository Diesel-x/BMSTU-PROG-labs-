import math

# Начальные условия
x_start = 0
x_end = 1.5
step = 0.05
width = 80  # ширина графика
min_y = -1  # минимальное значение функции
max_y = 1   # максимальное значение функции

# Ввод количества засечек
num_ticks = 8

# Масштабирование графика
tick_step = (max_y - min_y) / (num_ticks - 1)

# Вывод шкалы
print("Масштабная линейка:")
for i in range(num_ticks):
    tick_value = min_y + i * tick_step
    print(f"{tick_value:6.2f}", end=" ")
print(f"{max_y:6.2f}")
print(" " * 7 + "-" * width)

# Построение графика
x = x_start
while x <= x_end:
    y = math.sin(x)  # фиксированная функция sin(x)

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
