# Баянов Дияз ИУ7-14Б, Лаб 8, зад 1
# Найти столбец, имеющий определённое свойство по варианту.
# Вар 2 - Поиск максимального и минимального значений осуществлять алгоритмически.

# Ввод матрицы
use_test_data = input(
    "Использовать тестовые данные? (да/нет): ").strip().lower()

if use_test_data == "да":
    rows = 4
    cols = 4
    matrix = [
        [4, -2, 3.5, 1],
        [-1, 5, -6, 2],
        [3, 7, -8, 4],
        [-5, 6, 2.5, -3]
    ]
else:
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

# Поиск максимального и минимального значений в столбцах
max_value = float("-inf")
min_value = float("inf")
index_max_col = 0
index_min_col = 0

for col in range(cols):
    for row in range(rows):
        if matrix[row][col] > max_value:
            max_value = matrix[row][col]
            index_max_col = col
        if matrix[row][col] < min_value:
            min_value = matrix[row][col]
            index_min_col = col

print(
    f"\nМаксимальное значение {max_value} в столбце номер {index_max_col + 1}")
print(f"Минимальное значение {min_value} в столбце номер {index_min_col + 1}")
