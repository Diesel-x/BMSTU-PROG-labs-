# Даны два одномерных целочисленных массива A и B. Сформировать матрицу
# M, такую что
# 𝑚.𝑖𝑗 = 𝑎.𝑖 * 𝑏.𝑗
# Определить количество полных квадратов в каждой строке матрицы.Записать
# значения в массив S. Напечатать матрицу M в виде матрицы и рядом столбец S.

from math import sqrt
from Matrix import *

# a = [2, 4, 6]
# b = [1, 3, 5, 7]

a = list(map(int, input("Введите числа через пробел для массива а: ").split()))
b = list(map(int, input("Введите числа через пробел для массива b: ").split()))
matrix = [ [] for i in range(len(a))]
s = []

for i in range(len(a)):
    c = 0
    for j in range(len(b)):
        matrix[i].append(a[i] * b[j])
        if matrix[i][j] >= 0 and sqrt(matrix[i][j]) == int(sqrt(matrix[i][j])):
            c += 1
    s.append(c)

print_matrix(matrix)
print("Список полных квадратов в матрице: ", end="")
print(*s, sep=", ")