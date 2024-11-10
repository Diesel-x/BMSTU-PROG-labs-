# Баянов Дияз ИУ7-14Б, Лаб 8, зад 6 Все задания сданы
# Выполнить транспонирование квадратной матрицы.

# Ввод матрицы
use_test_data = input(
    "Использовать тестовые данные? (да/нет): ").strip().lower()

if use_test_data == "да":
    size = 4
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
else:
    size = int(input("Введите размер квадратной матрицы: "))
    matrix = []
    for i in range(size):
        while True:
            row_input = input(f"Введите элементы строки {i+1} через пробел: ")
            row_elements = row_input.split()
            if len(row_elements) != size:
                print(f"Ошибка: необходимо ввести {size} элементов.")
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

# Транспонирование матрицы
for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print("\nТранспонированная матрица:")
for row in matrix:
    print(" ".join(f"{element:>6.6g}" for element in row))
