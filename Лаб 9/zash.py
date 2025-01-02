def reflect_matrix(matrix):
    n = len(matrix)
    
    for i in range(n):

        for j in range((n // 2 + 1) - i):
            matrix[i][j], matrix[i][-(j+1)] = matrix[i][-(j+1)], matrix[i][j]
            
    return matrix

matrix = []
print("Введите элементы матрицы построчно, разделяя их пробелом:")



matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]


reflected_matrix = reflect_matrix(matrix)
for row in reflected_matrix:
    print(row)