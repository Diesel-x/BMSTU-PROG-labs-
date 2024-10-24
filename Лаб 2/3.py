# Баянов Дияз Гайсаевич ИУ7-14Б
# Лаб работа №2,; Часть 2; Задание 3
# Написать программу, которая по введенным значениям x и y определяет принадлежность точки области заменутой области, включая границы.

# Ввод данных
x = float(input(f"Введите x: "))
y = float(input(f"Введите y: "))

# Вычисление
isOnArea = False
if x >= -9:
    if x < -8:
        if 7 * (x + 8) ** 2 + 1 <= y <= -1/8 * (x + 9) ** 2 + 8:
            isOnArea = True
    elif x <= -2:
        if 1/3 * (x + 5) ** 2 - 7 <= y <= -1/16 * x ** 2 or 1/49 * (x + 1) ** 2 <= y <= -1/8 * (x + 9) ** 2 + 8:
            isOnArea = True
    elif x < -1:
        if any(-2 * (x + 1) ** 2 - 2 <= y <= -1/16 * x ** 2,
                1/49 * (x + 1) ** 2 <= y <= -1/8 * (x + 9) ** 2 + 8,
                y == -3/2 * x + 2):
            isOnArea = True
    elif x == -1:
        if -2 <= y <= 0 or y == 3.5:
            isOnArea = True
    elif x <= 0:
        if 4 * x ** 2 - 6 <= y <= -4 * x ** 2 + 2 or y == -3/2 * x + 2:
            isOnArea = True
    elif x < 1:
        if 4 * x ** 2 - 6 <= y <= -4 * x ** 2 + 2 or y == 3/2 * x + 2:
            isOnArea = True
    elif x == 1:
        if -2 <= y <= 0 or y == 3.5:
            isOnArea = True
    elif x <= 2:
        if any(-2 * (x - 1) ** 2 - 2 <= y <= -1/16 * x ** 2,
                1/49 * (x - 1) ** 2 <= y <= -1/8 * (x - 9) ** 2 + 8,
                y == 3/2 * x + 2):
            isOnArea = True
    elif x <= 8:
        if 1/3 * (x - 5) ** 2 - 7 <= y <= -1/16 * x ** 2 or 1/49 * (x - 1) ** 2 <= y <= -1/8 * (x - 9) ** 2 + 8:
            isOnArea = True
    elif x <= 9:
        if 7 * (x - 8) ** 2 + 1 <= y <= -1/8 * (x - 9) ** 2 + 8:
            isOnArea = True

# Блок 3: Вывод
print('Точка принадлежит области' if isOnArea else "Точка не принадлежит области")
