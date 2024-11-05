# Баянов Дияз, ИУ7-14Б, Зад 4, вар 5 ВСЁ СДЕЛАНО
# Замена всех идущих подряд цифр на последнюю цифру их суммы

arr = []
while True:
    length = input("Длина массива: ")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("Ошибка ввода длины массива. Ожидается неотрицательное целое число.")

for i in range(length):
    arr.append(input(f"{i+1} элемент массива > "))
print("Исходный массив:", arr)

for idx, elem in enumerate(arr):
    bukas_elem = list(elem)
    i = 0  # Индекс символа
    while i < len(bukas_elem):
        char = bukas_elem[i]
        if char.isdigit():
            elem = elem[:i] + " " + elem[i+1:]
        i += 1
    arr[idx] = elem

print("Измененный массив:", arr)
