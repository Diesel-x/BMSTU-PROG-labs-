# Дана матрица символов. Преобразовать её следующим образом: заменить все
# согласные латинские букв на заглавные, а все гласные латинские буквы на
# строчные. Вывести матрицу до преобразования и после.

def input_matrix(name):
    matrix = []
    while True:
        try:
            rows = int(input(f"Введите количество строк для матрицы {name}: "))
            for i in range(rows):
                row = list(
                    input(f"Введите элементы строки {i + 1} для матрицы {name}: "))
                matrix.append(row)
            break
        except ValueError as e:
            print(f"Ошибка: {e}\n")
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def transform_matrix(matrix):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in vowels:
                matrix[i][j] = matrix[i][j].lower()
            elif matrix[i][j] in consonants:
                matrix[i][j] = matrix[i][j].upper()
    return matrix


# Ввод матрицы символов
matrix = input_matrix("символов")

# Вывод матрицы до преобразования
print("\nМатрица до преобразования:")
print_matrix(matrix)

# Преобразование матрицы
transformed_matrix = transform_matrix(matrix)

# Вывод матрицы после преобразования
print("\nМатрица после преобразования:")
print_matrix(transformed_matrix)
