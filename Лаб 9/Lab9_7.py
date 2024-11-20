#Баянов Дияз ИУ7-14Б
def create_3d_array(x, y, z):
    array = []
    for i in range(x):
        layer = []
        for j in range(y):
            while True:
                row_input = input(f"Введите строку {i+1}, {j+1}: ")
                row = list(map(int, row_input.split()))
                if len(row) == z:
                    break
                print(f"Ошибка: введено {len(row)} элементов вместо {z}. Попробуйте снова.")
            layer.append(row)
        array.append(layer)
    return array

def find_slice(array, x, y, z):
    max_dim = max(x, y, z)
    
    if max_dim == x:
        slice_index = x // 2
        return array[slice_index]
    elif max_dim == y:
        slice_index = y // 2
        sliced_layer = []
        for i in range(x):
            sliced_layer.append([array[i][slice_index]])
        return sliced_layer
    else:
        slice_index = z // 2
        sliced_row = []
        for i in range(x):
            sliced_row.extend([array[i][j][slice_index] for j in range(y)])
        return [sliced_row]

while True:
    try:
        x = int(input("Введите количество слоёв X: "))
        y = int(input("Введите количество строк Y: "))
        z = int(input("Введите количество столбцов Z: "))
        break
    except ValueError:
        print("Ошибка: введено некорректное значение. Попробуйте снова.")

# array = create_3d_array(x, y, z)
array = [
    ["11 12 13 14 15", "21 22 23 24 25", "31 32 33 34 35", "41 42 43 44 45"],
    ["51 52 53 54 55", "61 62 63 64 65", "71 72 73 74 75", "81 82 83 84 85"],
    ["91 92 93 94 95", "101 102 103 104 105", "111 112 113 114 115", "121 122 123 124 125"]
]

print("\nТрёхмерный массив:")
for i in range(x):
    print(f"Слой {i + 1}")
    
    for j in range(y):
        print(' '.join(map(str, array[i][j])))

slice_result = find_slice(array, x, y, z)

print("\nРезультат среза:")
for s in slice_result:
    print(s)