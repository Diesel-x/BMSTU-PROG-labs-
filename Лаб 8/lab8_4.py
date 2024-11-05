# Баянов Дияз ИУ7-14Б, Лаб 8, зад 4
# Переставить местами столбцы с максимальной и минимальной суммой элементов.

# Ввод матрицы
rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))

matrix = []
for i in range(rows):
    while True:
        row_input = input(f"Введите элементы строки {i+1} через пробел: ")
        row_elements = row_input.split()
        if len(row_elements) != cols:
            print(f"Ошибка: необходимо ввести {cols} элементов.")
            continue
        valid = True
        for element in row_elements:
            if not (element.replace('.', '', 1).replace('-', '', 1).isdigit() and element.count('.') <= 1 and element.count('-') <= 1 and (element[0] == '-' or element[0].isdigit())):
                valid = False
                break
        if not valid:
            print("Ошибка: все элементы должны быть числами (целыми или дробными).")
            continue
        row = [float(element) for element in row_elements]
        matrix.append(row)
        break

print("\nВведенная матрица:")
for row in matrix:
    print(" ".join(f"{element:>6.6g}" for element in row))

# Найти столбцы с максимальной и минимальной суммой элементов
max_sum = float("-inf")
min_sum = float("inf")
index_max_sum = 0
index_min_sum = 0

for col in range(cols):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    if col_sum > max_sum:
        max_sum = col_sum
        index_max_sum = col
    if col_sum < min_sum:
        min_sum = col_sum
        index_min_sum = col

print(
    f"\nМаксимальная сумма элементов в столбце {index_max_sum + 1}: {max_sum}")
print(f"Минимальная сумма элементов в столбце {index_min_sum + 1}: {min_sum}")

# Перестановка столбцов
for row in range(rows):
    matrix[row][index_min_sum], matrix[row][index_max_sum] = matrix[row][index_max_sum], matrix[row][index_min_sum]

print("\nМатрица после перестановки столбцов:")
for row in matrix:
    print(" ".join(f"{element:>6.6g}" for element in row))
