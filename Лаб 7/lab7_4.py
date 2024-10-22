# Баянов Дияз, ИУ7-14Б, Зад 4, вар 5
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
    i_start = -1  # Начало последовательности
    digit_sum = 0  # Сумма цифр
    k = 0  # Текущая длина последовательности
    i = 0  # Индекс символа
    while i < len(bukas_elem):
        char = bukas_elem[i]
        if char.isdigit():
            if k == 0:
                i_start = i
            digit_sum += int(char)
            k += 1
        else:
            if k > 1:
                elem = elem[:i_start] + \
                    str(digit_sum % 10) + elem[i_start + k:]
                bukas_elem = list(elem)
                i = i_start  # Обновляем индекс после изменения строки
            k = 0
            digit_sum = 0
        i += 1
    if k > 1:
        elem = elem[:i_start] + str(digit_sum % 10) + elem[i_start + k:]
    arr[idx] = elem

print("Измененный массив:", arr)
