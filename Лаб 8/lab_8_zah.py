# Дана квадратная матрица n x n, в котором столбцы, которые начинается от 0 и заканчивается 1.
# Проверить по строками сверху вниз в какой строке встречается раньше всего 1
# Баянов Дияз ИУ7-14Б ЗАшита лаба 8

matrix = [
    [0, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

print("\nВведенная матрица:")
for row in matrix:
    print(" ".join(f"{element:>6.6g}" for element in row))

first_row = -1
found = False

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 1:
            first_row = row
            found = True
            break
    if found:
        break

# Вывод результата
if found:
    print(
        f"\nПервое вхождение 1 найдено в строке {first_row + 1}")
else:
    print("\nВ матрице нет 1")
