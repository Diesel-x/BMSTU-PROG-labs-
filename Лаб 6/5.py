# Баянов Дияз, ИУ7-14Б, Лаб 6, Зад 5
# Поменять местами элементы с характеристиками максимальный положительный и миниальный положительный

arr = []
while True:
    length = float(input("Длина массива: "))
    if length % 1 == 0 and int(length) >= 0:
        length = int(length)
        break
    else:
        print("Ошибка ввода длины массива. Ожидается неотрицательное целое число.")

for i in range(length):
    while True:
        eee = float(input(f"{i+1} элемент массива > "))
        if eee % 1 == 0:
            arr.append(int(eee))
            break
        else:
            print("Ошибка ввода элемента массива. Ожидается целое число.")

print(arr)

max_pos = float('-inf')
min_pos = float('inf')
max_pos_index = -1
min_pos_index = -1

for i in range(len(arr)):
    if arr[i] >= 0:
        if arr[i] > max_pos:
            max_pos = arr[i]
            max_pos_index = i
        if arr[i] < min_pos:
            min_pos = arr[i]
            min_pos_index = i

if max_pos_index != -1 and min_pos_index != -1:
    arr[max_pos_index], arr[min_pos_index] = arr[min_pos_index], arr[max_pos_index]

print(arr)
