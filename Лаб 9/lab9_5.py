# Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и
# В. Вывести все матрицы в виде матриц.

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


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError(
            "Количество столбцов матрицы A должно быть равно количеству строк матрицы B.")

    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


# Ввод матриц A и B
A = input_matrix("A")
B = input_matrix("B")

# Вычисление произведения матриц A и B
C = multiply_matrices(A, B)

# Вывод матриц A, B и C
print("\nМатрица A:")
print_matrix(A)

print("\nМатрица B:")
print_matrix(B)

print("\nМатрица C (произведение A и B):")
print_matrix(C)
