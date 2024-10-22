# Баянов Дияз, ИУ7-14Б, Зад 3, вар 1
# Поиск элемента, содержащего наибольшее кол-во английских гласных букв

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
print(arr)

eng_bukas = "eyuioa"
max_index = -1
max_k = 0
for elem in arr:
    bukas_elem = list(elem)
    k = 0
    for buka in bukas_elem:
        if buka in eng_bukas:
            k += 1
    if k > max_k:
        max_k = k
        max_index = arr.index(elem)

if max_index > -1:
    print("Строка, содержащая макс кол-во гласных:", arr[max_index])
else:
    print("Гласные отсутвуют")
