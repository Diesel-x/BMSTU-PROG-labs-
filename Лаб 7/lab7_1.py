# Баянов Дияз, ИУ7-14Б, звд 1, вар 3
# Удалить все нечётные элементы целочисленного списка за один цикл. Без del pop remove срезов

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


k = 0
for elem in arr:
    if elem % 2 == 0:
        arr[k] = elem
        k += 1

print("[", end="")
for i in range(k):
    print("{}".format(arr[i]), end="")
    if (i < k-1):
        print(", ", end="")
print("]")
