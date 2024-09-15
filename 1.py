#Вариант 15
import math as m
print("Введите радиус")
R = float(input())
print("Введите высоту нижнего пересечения плоскости")
H1 = float(input())
print("Введите высоту верхнего пересечения плоскости")
H2 = float(input())

# Функция для вычисления объёма усечённого цилиндра
def volume():
    V = m.pi * R ** 2 * (H2 + H1)/2
    return V

# Функция для вычисления площади боковой поверхности
def square():
    S = m.pi * R * (H2 + H1)
    return S

print(f"Объём усечённого цилиндра: {round(volume(), 2)}")
print(f"Площадь боковой поверхности: {round(square(), 2)}")
