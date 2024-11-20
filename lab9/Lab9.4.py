# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.

from Matrix import *

# matrix = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# r_list = [0, 2]

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

# Создание и заполнение массива I
i_list = []
while True:
    x = input("Введите индекс строк по одному, ввод всего массива заканчивается пустой строкой: ")
    if x == "":
        break
    elif int(x) >= row:
        print("Индекс должен быть меньше количества строк")
    else:
        i_list.append(int(x))

# Создание и заполнение массива R
r_list = []
for i in i_list:
    max_elem = matrix[i][0]
    for j in range(1, column):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]
    r_list.append(max_elem)

# Нахождение среднего арифметического
summa = 0
for x in r_list:
    summa += x
arithmetic_mean = summa / len(r_list)

print_matrix(matrix)
print("Массив L: ", end="")
print(*i_list, sep=", ")
print("Массив R: ", end="")
print(*r_list, sep=", ")
print("Среднее арифметическое: ", end="")
print(arithmetic_mean)