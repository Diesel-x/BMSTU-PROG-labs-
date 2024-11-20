# Дана матрица символов. Преобразовать её следующим образом: заменить все
# согласные латинские букв на заглавные, а все гласные латинские буквы на
# строчные. Вывести матрицу до преобразования и после.

def input_matrix(name):
    matrix = []
    while True:
        rows = int(input(f"Введите количество строк для матрицы {name}: "))
        for i in range(rows):
            row = list(
                input(f"Введите элементы строки {i + 1} для матрицы {name}: "))
            matrix.append(row)
        break
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


# matrix = input_matrix("символов")

matrix = [
    ['A', 'b', 'c', '5'],
    ['e', 'F', '2', 'H'],
    ['4', 'J', 'K', 'L']
]

print("\nМатрица до преобразования:")
print_matrix(matrix)

transformed_matrix = transform_matrix(matrix)

print("\nМатрица после преобразования:")
print_matrix(transformed_matrix)
