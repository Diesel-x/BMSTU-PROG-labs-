# Баянов Дияз Гайсаевич, ИУ7-14Б
# Лаб работа №3
# Написать программу, которая по введенным целочисленным
# координатам трех точек на плоскости вычисляет длины сторон
# образованного треугольника и длину биссектрисы, проведенной из
# наименьшего угла.
# Определить, является ли треугольник остроугольным.
# Далее вводятся координаты точки. Определить, находится ли точка
# внутри треугольника. Если да, то найти расстояние от точки до
# ближайшей стороны треугольника.

# Импорт библиотек
import math as m

eps = 1e-7  # Эпсилон

# Ввод координат точек
xA = float(input("Введите xA: "))
yA = float(input("Введите yA: "))

xB = float(input("Введите xB: "))
yB = float(input("Введите yB: "))

xC = float(input("Введите xC: "))
yC = float(input("Введите yC: "))

# Вычисление длин сторон треугольника
lengthAB = m.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
lengthBC = m.sqrt((xC - xB) ** 2 + (yC - yB) ** 2)
lengthAC = m.sqrt((xC - xA) ** 2 + (yC - yA) ** 2)

print(f"Длина стороны AB: {lengthAB:.7f}")
print(f"Длина стороны BC: {lengthBC:.7f}")
print(f"Длина стороны AC: {lengthAC:.7f}")
print()

# Вычисление углов треугольника
angleA = m.acos((lengthBC**2 + lengthAC**2 - lengthAB**2) /
                (2 * lengthBC * lengthAC))
angleB = m.acos((lengthAB**2 + lengthAC**2 - lengthBC**2) /
                (2 * lengthAB * lengthAC))
angleC = m.acos((lengthAB**2 + lengthBC**2 - lengthAC**2) /
                (2 * lengthAB * lengthBC))

print(f"Угол A: {m.degrees(angleA):.7f}")


# Вычисление биссектрисы, исходящего из минимального угла
if angleA < angleB and angleA < angleC:  # Если угол A минимальный
    bisector = (2 * lengthBC * lengthAC * m.cos(angleA / 2)) / \
        (lengthBC + lengthAC)
elif angleB < angleA and angleB < angleC:  # Если угол B минимальный
    bisector = (2 * lengthAB * lengthAC * m.cos(angleB / 2)) / \
        (lengthAB + lengthAC)
else:  # Если угол C минимальный
    bisector = (2 * lengthAB * lengthBC * m.cos(angleC / 2)) / \
        (lengthAB + lengthBC)

print(f"Длина биссектрисы: {bisector:.7f}")

# Проверка на остроугольность
if angleA < m.pi / 2 and angleB < m.pi / 2 and angleC < m.pi / 2:
    print("Треугольник остроугольный")

# Ввод координат точки
xZ = float(input("Введите x произвольной точки: "))
yZ = float(input("Введите y произвольной точки: "))

# Находиться ли точка внутри треугольника
# Вычисление площади исходного треугольника
s_ABC = abs((xA*(yB - yC) + xB*(yC - yA) + xC*(yA - yB)) / 2.0)

# Вычисление площадей треугольников, образованных точкой Z и сторонами исходного треугольника
s_ABZ = abs((xA*(yB - yZ) + xB*(yZ - yA) + xZ*(yA - yB)) / 2.0)
s_BCZ = abs((xB*(yC - yZ) + xC*(yZ - yB) + xZ*(yB - yC)) / 2.0)
s_ACZ = abs((xA*(yC - yZ) + xC*(yZ - yA) + xZ*(yA - yC)) / 2.0)

# Проверка, находится ли точка внутри треугольника
if abs(s_ABC - (s_ABZ + s_BCZ + s_ACZ)) < eps:
    # Вычисление расстояний от точки до сторон треугольника
    distance_to_AB = abs((yB - yA) * xZ - (xB - xA) * yZ +
                         xB * yA - yB * xA) / m.sqrt((yB - yA)**2 + (xB - xA)**2)
    distance_to_BC = abs((yC - yB) * xZ - (xC - xB) * yZ +
                         xC * yB - yC * xB) / m.sqrt((yC - yB)**2 + (xC - xB)**2)
    distance_to_AC = abs((yC - yA) * xZ - (xC - xA) * yZ +
                         xC * yA - yC * xA) / m.sqrt((yC - yA)**2 + (xC - xA)**2)

    # Нахождение минимального расстояния
    min_distance = min(distance_to_AB, distance_to_BC, distance_to_AC)

    print(
        f"Расстояние от точки до ближайшей стороны треугольника: {min_distance:.7f}")
else:
    print("Точка находится вне треугольника")
