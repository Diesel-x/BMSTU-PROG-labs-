# Баянов Дияз, ИУ7-14Б, Лаб 6, Зад 3
# Найти экстремум

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

ecs = []
for i in range(1, len(arr) - 2):
    if (arr[i - 1] < arr[i] > arr[i - 1] or arr[i - 1] > arr[i] < arr[i - 1]):
        ecs.append(arr[i])

indx = None
while True:
    indx = input(f"Введите номер экстремума из {len(ecs)}> ")
    if indx.isdigit() and 0 <= int(indx) <= len(ecs):
        indx = int(indx)
        break
    else:
        print("Номер вне допустимого диапазона или ошибка ввода. Ожидается целое число.")

print(ecs[indx - 1])
