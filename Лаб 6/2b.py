# Баянов Дияз, ИУ7-14Б, Лаб 6, Зад 2б
# Удалить элемент с заданным индексом алгоритмически.

arr = []
while True:
    length = input("Длина массива: ")
    if length.isdigit() and int(length) >= 0:
        length = int(length)
        break
    else:
        print("Ошибка ввода длины массива. Ожидается неотрицательное целое число.")

for i in range(length):
    while True:
        eee = input(f"{i+1} элемент массива > ")
        if eee.isdigit():
            arr.append(int(eee))
            break
        else:
            print("Ошибка ввода элемента массива. Ожидается целое число.")

print(arr)

indx = None
while True:
    indx = input("Индекс удаляемого элемента > ")
    if indx.isdigit() and 0 <= int(indx) < len(arr):
        indx = int(indx)
        break
    else:
        print("Индекс вне допустимого диапазона или ошибка ввода индекса. Ожидается целое число.")

if indx < len(arr) // 2:
    for i in range(indx, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr = arr[:len(arr) - 1]
else:
    for i in range(indx, 0, -1):
        arr[i] = arr[i - 1]
    arr = arr[1:]

print(arr)
