# Баянов Дияз, ИУ7-14Б, Лаб 6, Зад 1а
# Добавить элемент в заданное место списка (по индексу) с использованием
# любых средств Python.
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
        element = input(f"{i+1} элемент массива > ")
        if element.isdigit():
            arr.append(int(element))
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

# while True:
#     indx = input("Индекс вводимого элемента > ")
#     if indx.isdigit() and 0 <= int(indx) <= len(arr):
#         indx = int(indx)
#         break
#     else:
#         print("Индекс вне допустимого диапазона или ошибка ввода индекса. Ожидается целое число.")

indx = int(input("Индекс вводимого элемента > "))


arr.insert(indx, num)
print(arr)
