# Дана матрица символов. Преобразовать её следующим образом: заменить все
# согласные латинские букв на заглавные, а все гласные латинские буквы на
# строчные. Вывести матрицу до преобразования и после.

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

# Ввод данных матрицы
row = int(input("Введите количество строк: "))
while row < 0:
    print("Количество строк должно быть больше или равно нулю")
    row = int(input("Введите количество строк: "))
column = int(input("Введите количество столбцов: "))
while column < 0:
    print("Количество столбцов должно быть больше или равно нулю")
    column = int(input("Введите количество столбцов: "))

# Создание и заполнение матрицы
matrix = fill_matrix(row, column)

print_matrix(matrix)

vowels = "AEYUIO"
for i in range(row):
    for j in range(column):
        if matrix[i][j].isalpha():
            if matrix[i][j].upper() in vowels:
                matrix[i][j] = matrix[i][j].lower()
            else:
                matrix[i][j] = matrix[i][j].upper()

print("Измененная матрица: ")
print_matrix(matrix)