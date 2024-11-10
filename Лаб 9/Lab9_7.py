# Баянов Дияз ИУ7-14Б зад 1-7 сданы
# Ввести трёхмерный массив(массив матриц размера X*Y*Z). Вывести срез
# массива по большему измерению, индекс среза– середина размерности с
# округлением в меньшую сторону.

def input_3d_array():
    while True:
        try:
            x = int(input("Введите размер X: "))
            y = int(input("Введите размер Y: "))
            z = int(input("Введите размер Z: "))
            array = np.zeros((x, y, z), dtype=int)
            for i in range(x):
                for j in range(y):
                    row = list(map(int, input(
                        f"Введите элементы строки {j + 1} для матрицы {i + 1} через пробел: ").split()))
                    if len(row) != z:
                        raise ValueError(
                            "Количество элементов в строке должно совпадать с размером Z.")
                    array[i, j, :] = row
            break
        except ValueError as e:
            print(f"Ошибка: {e}\n")
    return array


def print_3d_array(array):
    x, y, z = array.shape
    for i in range(x):
        print(f"Матрица {i + 1}:")
        for j in range(y):
            print(" ".join(map(str, array[i, j, :])))
        print()


def get_max_dimension(x, y, z):
    if x >= y and x >= z:
        return 'x', x
    elif y >= x and y >= z:
        return 'y', y
    else:
        return 'z', z


def get_slice(array):
    x, y, z = array.shape
    max_dim, max_size = get_max_dimension(x, y, z)
    index = max_size // 2
    if max_dim == 'x':
        return array[index, :, :]
    elif max_dim == 'y':
        return array[:, index, :]
    else:
        return array[:, :, index]


# Ввод трехмерного массива
array = input_3d_array()

# Вывод трехмерного массива
print("\nТрехмерный массив:")
print_3d_array(array)

# Получение и вывод среза массива по большему измерению
slice_array = get_slice(array)
print("\nСрез массива по большему измерению:")
print(slice_array)
