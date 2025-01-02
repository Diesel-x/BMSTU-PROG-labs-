# Даны две матрицы A и B, в которых количество столбцов одинаково.
# Подсчитать для каждого столбца матрицы А количество элементов, больших
# среднего арифметического элементов соответствующего столбца матрицы В.
# Вывести полученные значения. Затем преобразовать матрицу В путем
# умножения всех элементов столбца матрицы на посчитанное для этого столбца
# значение, если оно ненулевое. Вывести преобразованную матрицу в виде
# матрицы.

from Matrix import *

# Ввод данных первой матрицы
row_a, column = input_matrix()
matrix_a = fill_matrix(row_a, column)

# Ввод данных второй матрицы
row_b = int(input("Введите количество строк для второй матрицы: "))
while row_b < 0:
    print("Количество строк должно быть больше или равно нулю")
    row_b = int(input("Введите количество строк для второй матрицы: "))

matrix_b = fill_matrix(row_b, column)

list_cnt = []
for j in range(column):
    sum = 0
    for i in range(row_b):
        sum += matrix_b[i][j]
    arithmetic_mean = sum / row_b
    cnt = 0
    for i in range(row_a):
        if matrix_a[i][j] > arithmetic_mean:
            cnt += 1
    list_cnt.append(cnt)
    if cnt != 0:
        for i in range(row_a):
            matrix_b[i][j] *= cnt

print("Количества элементов первой матрицы, которые больше среднего арифметического второго (по столбцам): ", end="")
print(*list_cnt, sep=", ")
print("Преобразованная матрица: ")
print_matrix(matrix_b)