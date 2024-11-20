# Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и
# В. Вывести все матрицы в виде матриц.

from Matrix import *

# Ввод данных матрицы для матрицы А
row_a = int(input("Введите количество строк для матрицы А: "))
while row_a < 0:
    print("Количество строк должно быть больше или равно нулю")
    row_a = int(input("Введите количество строк для матрицы А: "))
column_a = int(input("Введите количество столбцов для матрицы А: "))
while column_a < 0:
    print("Количество столбцов должно быть больше или равно нулю")
    column_a = int(input("Введите количество столбцов для матрицы А: "))

# Создание и заполнение матрицы А
matrix_a = fill_matrix(row_a, column_a)

# Ввод данных для матрицы B
row_b = int(input("Введите количество строк для матрицы B: "))
while row_b < 0:
    print("Количество строк должно быть больше или равно нулю")
    row_b = int(input("Введите количество строк для матрицы B: "))
column_b = int(input("Введите количество столбцов для матрицы B: "))
while column_b < 0:
    print("Количество столбцов должно быть больше или равно нулю")
    column_b = int(input("Введите количество столбцов для матрицы B: "))

# Создание и заполнение матрицы B
matrix_b = fill_matrix(row_b, column_b)

print("Матрица A:")
print_matrix(matrix_a)
print("Матрица B:")
print_matrix(matrix_b)

# Создание и заполнение матрицы С
if column_a != row_b:
    print("Матрицу А нельзя умножить на матрицу B")
else:
    matrix_c = [[0] * column_b for i in range(row_a)]
    for i in range(row_a):
        for j in range(column_b):
            for k in range(column_a):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
    print("Матрица С: ")
    print_matrix(matrix_c)