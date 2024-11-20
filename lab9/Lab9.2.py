# Баянов Дияз ИУ7-14Б, Лаб 9, зад
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
# вводить. Транспонирование не применять.

from Matrix import *

# Ввод данных матрицы
row = int(input("Введите количество строк: "))
while row < 0:
    print("Количество строк должно быть больше или равно нулю")
    row = int(input("Введите количество строк: "))
column = int(input("Введите количество столбцов: "))
while column < 0:
    print("Количество столбцов должно быть больше или равно нулю")
    column = int(input("Введите количество столбцов: "))

matrix = fill_matrix(row, column)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# row = len(matrix[0])
# column = len(matrix)


print("Исходная матрица: ")
print_matrix(matrix)

# Поворот матрицы на 90 градусов по часовой стрелке
for i in range(row // 2):
    for j in range(i, column - i - 1):
        (matrix[j][-i - 1], matrix[-i - 1][-j - 1],
         matrix[-j - 1][i], matrix[i][j]) = (matrix[i][j], matrix[j][-i - 1],
                                             matrix[-i - 1][-j - 1], matrix[-j - 1][i])

print("Поворот на 90 градусов: ")
print_matrix(matrix)

# Поворот матрицы на 90 градусов против часовой стрелки
for i in range(row // 2):
    for j in range(i, column - i - 1):
        (matrix[i][j], matrix[j][-i - 1],
         matrix[-i - 1][-j - 1], matrix[-j - 1][i]) = (matrix[j][-i - 1], matrix[-i - 1][-j - 1],
                                                       matrix[-j - 1][i], matrix[i][j])
print("Поворот на -90 градусов: ")
print_matrix(matrix)