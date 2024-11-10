# Баянов Дияз ИУ7-14Б, Лаб 9, зад
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
# вводить. Транспонирование не применять.

# Ввод матрицы
use_test_data = input(
    "Использовать тестовы�� данные? (да/нет): ").strip().lower()

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
                if not element.lstrip('-').replace('.', '', 1).isdigit():
                    valid = False
                    break
            if not valid:
                print("Ошибка: все элементы должны быть числами (целыми или дробными).")
                continue
            row = [int(element) for element in row_elements]
            matrix.append(row)
            break

print("\nИсходная матрица:")
for row in matrix:
    print(" ".join(f"{element:>6}" for element in row))

# Поворот матрицы на 90 градусов по часовой стрелке
for layer in range(size // 2):
    first = layer
    last = size - 1 - layer
    for i in range(first, last):
        offset = i - first
        top = matrix[first][i]
        matrix[first][i] = matrix[last - offset][first]
        matrix[last - offset][first] = matrix[last][last - offset]
        matrix[last][last - offset] = matrix[i][last]
        matrix[i][last] = top

print("\nМатрица после поворота на 90 градусов по часовой стрелке:")
for row in matrix:
    print(" ".join(f"{element:>6}" for element in row))

# Поворот матрицы на 90 градусов против часовой стрелки
for layer in range(size // 2):
    first = layer
    last = size - 1 - layer
    for i in range(first, last):
        offset = i - first
        top = matrix[first][i]
        matrix[first][i] = matrix[i][last]
        matrix[i][last] = matrix[last][last - offset]
        matrix[last][last - offset] = matrix[last - offset][first]
        matrix[last - offset][first] = top

print("\nМатрица после поворота на 90 градусов против часовой стрелки:")
for row in matrix:
    print(" ".join(f"{element:>6}" for element in row))
