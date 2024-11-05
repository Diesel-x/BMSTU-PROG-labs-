# Баянов Дияз ИУ7-14Б, Лаб 8, зад 2, вар 2
# Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.

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

max_minus_count = float("-inf")
index_min_count = 0
min_minus_count = float("inf")
index_max_count = 0

for index_n, n in enumerate(matrix):
    minus_count = 0
    for m in n:
        if m < 0:
            minus_count += 1
    print(
        f"Количество отрицательных элементов в строке {index_n+1}: {minus_count}")
    if minus_count > max_minus_count:
        max_minus_count = minus_count
        index_max_count = index_n
    if minus_count < min_minus_count:
        min_minus_count = minus_count
        index_min_count = index_n

print("\nМин кол-во отрицательных элементов в строке", index_min_count+1)
print("Макс кол-во отрицательных элементов в строке", index_max_count+1)

# Перестановка строк
matrix[index_min_count], matrix[index_max_count] = matrix[index_max_count], matrix[index_min_count]

print("\nМатрица после перестановки строк:")
for row in matrix:
    print(" ".join(f"{element:>6.6g}" for element in row))
