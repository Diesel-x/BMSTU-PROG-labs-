# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.

def input_matrix(name):
    matrix = []
    while True:
        try:
            rows = int(input(f"Введите количество строк для матрицы {name}: "))
            cols = int(
                input(f"Введите количество столбцов для матрицы {name}: "))
            for i in range(rows):
                row = list(
                    map(int, input(f"Введите элементы строки {i + 1} для матрицы {name}: ").split()))
                if len(row) != cols:
                    raise ValueError(
                        "Количество элементов в строке должно совпадать с количеством столбцов.")
                matrix.append(row)
            break
        except ValueError as e:
            print(f"Ошибка: {e}\n")
    return matrix


def input_array(name):
    while True:
        try:
            array = list(
                map(int, input(f"Введите элементы массива {name}: ").split()))
            return array
        except ValueError as e:
            print(f"Ошибка: {e}\n")


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def max_elements(matrix, indices):
    return [max(matrix[i]) for i in indices]


def average(values):
    return sum(values) / len(values)


# Ввод матрицы D и массива I
D = input_matrix("D")
I = input_array("I")

# Определение максимальных элементов для строк, указанных в массиве I
R = max_elements(D, I)

# Определение среднего арифметического вычисленных максимальных значений
avg = average(R)

# Вывод матрицы D, массивов I и R, среднего арифметического значения
print("\nМатрица D:")
print_matrix(D)

print("\nМассив I:")
print(" ".join(map(str, I)))

print("\nМассив R:")
print(" ".join(map(str, R)))

print(f"\nСреднее арифметическое значение: {avg:.2f}")
