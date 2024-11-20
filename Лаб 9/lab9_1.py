# Даны два одномерных целочисленных массива A и B. Сформировать матрицу
# M, такую что
# 𝑚.𝑖𝑗 = 𝑎.𝑖 * 𝑏.𝑗
# Определить количество полных квадратов в каждой строке матрицы.Записать
# значения в массив S. Напечатать матрицу M в виде матрицы и рядом столбец S.

import math

def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


A, B = [], []

# while True:
#     try:
#         A = list(map(int, input("Ввод A: ").split()))
#         if not A:
#             raise ValueError("Массив не должен быть пустым")
#         break
#     except ValueError as e:
#         print(f"Ошибка: {e}\n")

# while True:
#     try:
#         B = list(map(int, input("Ввод B: ").split()))
#         if not B:
#             raise ValueError("Массив не должен быть пустым")
#         break
#     except ValueError as e:
#         print(f"Ошибка: {e}\n")


A = [2, 4, 6]
B = [1, 3, 5, 7]

print("\nМатрица A:")
print(A)

print("\nМатрица B:")
print(B)

M = [[a * b for b in B] for a in A]

print("\nМатрица M:")
print_matrix(M)

S = [sum(1 for element in row if is_perfect_square(element)) for row in M]

print("\nСтолбец S:")
for s in S:
    print(s)
