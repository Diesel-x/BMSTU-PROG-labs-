# Баянов Дияз, ИУ7-14Б, Зад 2, вар 2
# После каждого чётного элемента целочисленного списка добавить его удвоенное значение, без использования вложенных


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
        if eee.lstrip("-").isdigit():
            arr.append(int(eee))
            break
        else:
            print("Ошибка ввода элемента массива. Ожидается целое число.")
print(arr)

old_len = len(arr) - 1  # последний индекс текущего массива, который исзменится
k = 0  # кол-во чётных элементов
for elem in arr:
    if elem % 2 == 0:
        k += 1

arr += [""] * k
print(arr)

for i in range(len(arr) - k - 1, -1, -1):
    if arr[i] % 2 == 0:
        arr[old_len + k] = arr[i] * 2
        k -= 1
    arr[old_len + k] = arr[i]
    old_len -= 1

print(arr)
