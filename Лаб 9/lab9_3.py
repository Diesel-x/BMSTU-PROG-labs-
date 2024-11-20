# Даны две матрицы A и B, в которых количество столбцов одинаково.
# Подсчитать для каждого столбца матрицы А количество элементов, больших
# среднего арифметического элементов соответствующего столбца матрицы В.
# Вывести полученные значения. Затем преобразовать матрицу В путем
# умножения всех элементов столбца матрицы на посчитанное для этого столбца
# значение, если оно ненулевое. Вывести преобразованную матрицу в виде
# матрицы.

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

def count_and_transform(A, B):
    # Находим средние арифметические для каждого столбца матрицы B
    column_means_B = []
    
    for j in range(len(B[0])):
        col_sum = sum(row[j] for row in B)
        mean = col_sum / len(B)
        column_means_B.append(mean)
        
    # Подсчет количества элементов в каждом столбце матрицы A,
    # которые больше среднего арифметического соответствующего столбца в B
    counts = []
    
    for j in range(len(A[0])):
        count = 0
        for i in range(len(A)):
            if A[i][j] > column_means_B[j]:
                count += 1
        counts.append(count)
    
    print("Количество элементов в каждом столбце матрицы A, больших среднего арифметического соответствующих столбцов матрицы B:")
    print(counts)
    
    transformed_B = [[0] * len(B[0]) for _ in range(len(B))]
    
    for j in range(len(B[0])):
        if counts[j] != 0:
            for i in range(len(B)):
                transformed_B[i][j] = B[i][j] * counts[j]
                
    return transformed_B


A = [
    [2, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

B = [
    [2, 4, 15, 16],
    [1, 1, 0, 3],
    [100, 2, 1, 6]
]

result = count_and_transform(A, B)
print("\nПреобразованная матрица B:")
for row in result:
    print(row)