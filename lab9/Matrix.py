# Функция создания и заполнения матрицы
def fill_matrix(f_row, f_column):
    f_matrix = []
    for i in range(f_row):
        line = list(map(int, input(f"Введите значения матрицы {i + 1} строки через пробел: ").split()))
        while len(line) != f_column:
            print(f"Введите {f_column} чисел")
            line = list(map(int, input(f"Введите значения матрицы {i + 1} строки через пробел: ").split()))
        f_matrix.append(line)
    return f_matrix

# Функция вывода матрицы
def print_matrix(f_matrix):
    max_length = len(str(f_matrix[0][0]))
    for i in range(len(f_matrix)):
        for j in range(len(f_matrix[i])):
            if len(str(f_matrix[i][j])) > max_length:
                max_length = len(str(f_matrix[i][j]))
    for i in range(len(f_matrix)):
        for j in range(len(f_matrix[i])):
            print(f"{f_matrix[i][j]:>{max_length+2}}", end=" ")
        print()