# Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и
# В. Вывести все матрицы в виде матриц.

def input_matrix(name):
    matrix = []
    while True:
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
    return matrix

def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        print("Ошибка: Матрицы несовместимы для умножения.")
        return None
    
    num_rows_A = len(A)
    num_cols_B = len(B[0])
    
    # Создаем пустую матрицу для результата
    C = [[0 for _ in range(num_cols_B)] for _ in range(num_rows_A)]
    
    # Перемножение матриц
    for i in range(num_rows_A):
        for j in range(num_cols_B):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def print_matrix(aboba):
    for row in aboba:
        print(' '.join(map(str, row)))

A = [
    [1, 2, 4],
    [3, 4, 5]
]
B = [
    [5, 6, 7],
    [7, 8, 9],
    [1, 3, 8]
]

# A = input_matrix("A")
# B = input_matrix("B")

C = matrix_multiplication(A, B)
print("Матрица A:")
print_matrix(A)
print("\nМатрица B:")
print_matrix(B)
if C != None:
    print("\nМатрица C (произведение A и B):")
    print_matrix(C)