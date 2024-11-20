# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.

def input_matrix(name):
    matrix = []
    while True:
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
    return matrix


def find_max_elements(D, I):
    R = []
    
    for i in I:
        max_value = max(D[i])
        R.append(max_value)
        
    return R

def average_of_max_values(R):
    if len(R) == 0:
        return None
    else:
        return sum(R) / len(R)

# Тестовые данные
D = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

I = [0, 2]

R = find_max_elements(D, I)

average = average_of_max_values(R)

print("Матрица D:")
for row in D:
    print(row)

print("\nМассив I:", I)
print("\nМассив R:", R)
print(f"\nСреднее арифметическое: {average}")