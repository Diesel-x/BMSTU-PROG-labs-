def is_number(s):
    # Проверка, является ли строка числом
    if s.count('.') <= 1 and s.replace('.', '', 1).replace('-', '', 1).isdigit():
        # Проверка наличия одного символа '-' и что он в начале
        return s[1:].isdigit() if s.startswith('-') else s.isdigit()
    return False


def input_matrix():
    # Ввод количества строк и столбцов
    rows = input("Введите количество строк матрицы: ")
    cols = input("Введите количество столбцов матрицы: ")

    # Проверка, что размеры матрицы являются положительными целыми числами
    if not rows.isdigit() or not cols.isdigit() or int(rows) <= 0 or int(cols) <= 0:
        print("Ошибка: размеры матрицы должны быть положительными целыми числами.")
        return None

    rows, cols = int(rows), int(cols)
    matrix = []

    # Ввод элементов матрицы
    print("Введите элементы матрицы построчно, разделяя числа пробелами:")
    for i in range(rows):
        while True:
            row_input = input(f"Строка {i+1}: ").split()

            # Проверка, что строка имеет правильное количество элементов
            if len(row_input) != cols:
                print(
                    f"Ошибка: в строке {i+1} должно быть ровно {cols} элементов.")
                continue

            # Проверка, что все элементы строки - числа
            if all(is_number(element) for element in row_input):
                row = [float(element) for element in row_input]
                matrix.append(row)
                break
            else:
                print("Ошибка: все элементы строки должны быть числами.")

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{element:>6.6g}" for element in row))
