#Баянов Дияз ИУ7-14Б
#Срез матрицы

def fill_matrix(f_row, f_column):
    f_matrix = []
    for i in range(f_row):
        line = list(map(int, input(f"Введите значения матрицы {i + 1} строки через пробел: ").split()))
        while len(line) != f_column:
            print(f"Введите {f_column} чисел")
            line = list(map(int, input(f"Введите значения матрицы {i + 1} строки через пробел: ").split()))
        f_matrix.append(line)
    return f_matrix

def print_matrix(m, c):
    for i in range(len(m)):
        print(f"{m[i]:>10}", end="")
        if (i + 1) % c == 0:
            print()

x = int(input("Введите размер Х для матрицы: "))
while x < 0:
    print("Размер должен быть больше или равен нулю")
y = int(input("Введите размер Y для матрицы: "))
while x < 0:
    print("Размер должен быть больше или равен нулю")
z = int(input("Введите размер Z для матрицы: "))
while x < 0:
    print("Размер должен быть больше или равен нулю")

# Создание и заполнение матрицы
# mega_matrix = []
# for i in range(x):
#     matrix = fill_matrix(y, z)
#     mega_matrix.append(matrix)

# Определение большего измерения
max_measurement = 0
matrix = []
if x > y:
    if x > z:
        max_measurement = (x - 1) // 2
        for j in range(y):
            for k in range(z):
                matrix.append(mega_matrix[max_measurement][j][k])
        print_matrix(matrix, y)
    else:
        max_measurement = (z - 1) // 2
        for i in range(x):
            for j in range(y):
                matrix.append(mega_matrix[i][j][max_measurement])
        print_matrix(matrix, x)
else:
    if y > z:
        max_measurement = (y - 1) // 2
        for i in range(x):
            for k in range(z):
                matrix.append(mega_matrix[i][max_measurement][k])
        print_matrix(matrix, x)
    else:
        max_measurement = (z - 1) // 2
        for i in range(x):
            for j in range(y):
                matrix.append(mega_matrix[i][j][max_measurement])
        print_matrix(matrix, x)