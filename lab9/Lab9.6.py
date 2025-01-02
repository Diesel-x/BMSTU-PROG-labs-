# Дана матрица символов. Преобразовать её следующим образом: заменить все
# согласные латинские букв на заглавные, а все гласные латинские буквы на
# строчные. Вывести матрицу до преобразования и после.

from Matrix import *
# Функция создания и заполнения матрицы
def fill_matrix(f_row, f_column):
    f_matrix = []
    for i in range(f_row):
        line = list(input(f"Введите значения матрицы {i + 1} строки через пробел: ").split())
        while len(line) != f_column:
            print(f"Введите {f_column} чисел")
            line = list(input(f"Введите значения матрицы {i + 1} строки через пробел: ").split())
        f_matrix.append(line)
    return f_matrix

# Функция вывода матрицы
def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]:>10}", end="")
        print()

# Изменение матрицы
def matrix_edit(row, column, matrix):
    vowels = "AEYUIO"
    for i in range(row):
        for j in range(column):
            if matrix[i][j].isalpha():
                if matrix[i][j].upper() in vowels:
                    matrix[i][j] = matrix[i][j].lower()
                else:
                    matrix[i][j] = matrix[i][j].upper()

row, column = input_matrix()
matrix = fill_matrix(row, column)

print_matrix(matrix)

matrix_edit(row, column, matrix)

print("Измененная матрица: ")
print_matrix(matrix)