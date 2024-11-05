# Баянов Дияз ИУ7-14Б, Лаб 8, зад 3
# Найти строку, имеющую определённое свойство по варианту.
# Вар 3 - наибольшее кол-во чётных элементов

# Ввод матрицы
rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))

matrix = []
for i in range(rows):
    while True:
        row_input = input(f"Введите элементы строки {i+1} через пробел: ")
        row_elements = row_input.split()
        if len(row_elements) != cols:
            print(f"Ошибка: необходимо ввести {cols} элементов.")
            continue
        valid = True
        for element in row_elements:
            if not (element.replace('.', '', 1).replace('-', '', 1).isdigit() and element.count('.') <= 1 and element.count('-') <= 1 and (element[0] == '-' or element[0].isdigit())):
                valid = False
                break
        if not valid:
            print("Ошибка: все элементы должны быть числами (целыми или дробными).")
            continue
        row = [float(element) for element in row_elements]
        matrix.append(row)
        break

print("\nВведенная матрица:")
for row in matrix:
    print(" ".join(f"{element:>6.6g}" for element in row))

max_even_count = 0
index_max_even = 0

for index_n, n in enumerate(matrix):
    even_count = 0
    for m in n:
        if m % 2 == 0:
            even_count += 1
    if even_count > max_even_count:
        max_even_count = even_count
        index_max_even = index_n

print("\nМаксимальное количество чётных элементов: {} в строке номер {}".format(
    max_even_count, index_max_even + 1))
