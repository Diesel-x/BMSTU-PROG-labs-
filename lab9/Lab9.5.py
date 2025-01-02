# Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и
# В. Вывести все матрицы в виде матриц.

from Matrix import *



row_a, column_a = input_matrix()
matrix_a = fill_matrix(row_a, column_a)

row_b, column_b = input_matrix()
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