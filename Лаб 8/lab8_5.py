# Баянов Дияз ИУ7-14Б, Лаб 8, зад 5
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю.

# Ввод матрицы
use_test_data = input(
    "Использовать тестовые данные? (да/нет): ").strip().lower()

if use_test_data == "да":
    size = 4
    # matrix = [
    #     [4, -2, 3.5, 13],
    #     [-1, 5, -6, 2],
    #     [3, 7, -8, 4],
    #     [-5, 6, 2.5, -3]
    # ]
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [-5, 0, 0, 5]
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

# Найти максимальное значение над главной диагональю и минимальное значение под побочной диагональю
max_above_main_diag = float("-inf")
min_below_secondary_diag = float("inf")

for i in range(size):
    for j in range(size):
        if j > i:  # Над главной диагональю
            if matrix[i][j] > max_above_main_diag:
                max_above_main_diag = matrix[i][j]
        if j > size - 1 - i:  # Под побочной диагональю
            if matrix[i][j] < min_below_secondary_diag:
                min_below_secondary_diag = matrix[i][j]

print(f"\nМаксимальное значение над главной диагональю: {max_above_main_diag}")
print(
    f"Минимальное значение под побочной диагональю: {min_below_secondary_diag}")
