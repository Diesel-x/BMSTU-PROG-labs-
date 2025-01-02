import numpy as np
import random as rnd

def main():
    text = "Бу, испугался? Не бойся! Я друг! Я тебя не обижу! Иди сюда, иди ко мне, сядь рядом со мной"
    matrix = matrix_gen(int(8))
    print("Исходная матрица:")
    print_matrix(matrix)

    matrix = holes_gen(matrix)
    print("\nПроколотая матрица:")
    print_matrix(matrix)
        
def rotate_grid(grid):
    return np.rot90(grid, -1)

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f'{num:2}' for num in row))

def matrix_gen(size):
    matrix = np.zeros((size, size), dtype=int)
    k = 1
    for i in range(size // 2):
        for j in range(size // 2):
            matrix[i][j] = k
            k += 1

    subgrid = [[matrix[i][j] for j in range(size // 2)] for i in range(size // 2)]

    rotated = rotate_grid(subgrid)
    for i in range(size // 2):
        for j in range(size // 2, size):
            matrix[i][j] = rotated[i][j - size // 2]

    rotated = rotate_grid(rotated)
    for i in range(size // 2, size):
        for j in range(size // 2, size):
            matrix[i][j] = rotated[i - size // 2][j - size // 2]

    rotated = rotate_grid(rotated)
    for i in range(size // 2, size):
        for j in range(size // 2):
            matrix[i][j] = rotated[i - size // 2][j]

    return matrix

def holes_gen(matrix):
    size = len(matrix)
    positions = {}
    for i in range(size):
        for j in range(size):
            num = matrix[i][j]
            if num not in positions:
                positions[num] = []
            positions[num].append((i, j))

    print(positions)

    for num, pos_list in positions.items():
        rnd_pos = rnd.choice(pos_list)
        matrix[rnd_pos[0], rnd_pos[1]] = 0
    
    return matrix

def matrix_fill(text, matrix):
    # size = 0
    # for i in range(size):
    #     for j in range(size):
    # i = 0
    while len(text) > i:



if __name__ == "__main__":
    main()
