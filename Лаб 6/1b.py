# Баянов Дияз, ИУ7-14Б, Лаб 6, Зад 1б
# Добавить элемент в заданное место списка (по индексу) алгоритмически
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

while True:
    num = input("Элемент > ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Ошибка ввода элемента. Ожидается целое число.")

while True:
    indx = input("Индекс вводимого элемента > ")
    if indx.isdigit() and 0 <= int(indx) <= len(arr):
        indx = int(indx)
        break
    else:
        print("Индекс вне допустимого диапазона или ошибка ввода индекса. Ожидается целое число.")

arr.append(0)
for i in range(len(arr) - 1, indx, -1):
    arr[i] = arr[i - 1]
arr[indx] = num
print(arr)
