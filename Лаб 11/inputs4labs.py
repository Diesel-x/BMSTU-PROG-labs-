def input_float_array():
    arr = None
    while True:
        try:
            arr = list(map(float, input("Введите элементы массива через пробел: ").split()))
            if (len(arr) == 0):
                print("Массив должен быть больше 0")
                continue
            break
        except ValueError:
            print("Массив введён некорректно")
    return arr

def input_int_array():
    arr = None
    while True:
        try:
            arr = list(map(int, input("Введите целочисленные элементы массива через пробел: ").split()))
            if (len(arr) == 0):
                print("Массив должен быть больше 0")
                continue
            break
        except ValueError:
            print("Массив введён некорректно")
    return arr