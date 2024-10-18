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

primals = []
primals_f = []
is_end = False
for i in arr:
    d = 2

    while d * d <= i and i % d != 0:
        d+=1
    if d * d > i:
        if len(primals) == 0: #Если начало последовательности
            primals.append(i)
        elif primals[len[primals] - 2] < i: #Если больше последнего элемента посл-ти
            primals.append(i)
        elif len(primals_f) < len(primals): #Если текущая посл-ть больше прошлого
            primals_f = primals
        primals = []
            
    else:
        if len(primals_f) < len(primals):
            primals_f = primals
        primals = []
        # primals.clear() #Правильно ли?
if len(primals_f) > 1:
    print(primals_f)
else:
    print("Поледовательности не существует")


    
      
