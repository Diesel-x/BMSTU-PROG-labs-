# Даны две матрицы A и B, в которых количество столбцов одинаково.
# Подсчитать для каждого столбца матрицы А количество элементов, больших
# среднего арифметического элементов соответствующего столбца матрицы В.
# Вывести полученные значения. Затем преобразовать матрицу В путем
# умножения всех элементов столбца матрицы на посчитанное для этого столбца
# значение, если оно ненулевое. Вывести преобразованную матрицу в виде
# матрицы.

def input_matrix(name):
    matrix = []
    while True:
        try:
            rows = int(input(f"Введите количество строк для матрицы {name}: "))
            cols = int(
                input(f"Введите количество столбцов для матрицы {name}: "))
            for i in range(rows):
                row = list(
                    map(int, input(f"Введите элементы строки {i + 1} для матрицы {name}: ").split()))
                if len(row) != cols:
                    raise ValueError(
                        "Количество элементов в строке должно совпадать с количеством столбцов.")
                matrix.append(row)
            break
        except ValueError as e:
            print(f"Ошибка: {e}\n")
    return matrix


def column_average(matrix, col):
    return sum(row[col] for row in matrix) / len(matrix)


def transform_matrix_B(matrix_B, values):
    for j in range(len(matrix_B[0])):
        if values[j] != 0:
            for i in range(len(matrix_B)):
                matrix_B[i][j] *= values[j]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Ввод матриц A и B
A = input_matrix("A")
B = input_matrix("B")

# Подсчет количества элементов в каждом столбце матрицы A, которые больше среднего арифметического соответствующего столбца матрицы B
values = []
for j in range(len(A[0])):
    avg = column_average(B, j)
    count = sum(1 for i in range(len(A)) if A[i][j] > avg)
    values.append(count)

# Вывод полученных значений
print("\nПолученные значения для каждого столбца матрицы A:")
print(" ".join(map(str, values)))

# Преобразование матрицы B
transform_matrix_B(B, values)

# Вывод преобразованной матрицы B
print("\nПреобразованная матрица B:")
print_matrix(B)
