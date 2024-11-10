# Вводится список из float элементов. Поменять второй и третий максимум
# Лаба 6 защита Баянов Дияз
while True:
    input_str = input("Введите список из float элементов через пробел: ")
    lst = list(map(float, input_str.split()))
    if len(lst) > 2:
        break
    print("Список должен быть больше 3 элементов")

print("\nВведенный список:")
print(" ".join(f"{element:.2f}" for element in lst))

if len(lst) >= 3:
    max_indices = [-1] * 3
    for i, num in enumerate(lst):
        if max_indices[0] == -1 or num > lst[max_indices[0]]:
            max_indices[2] = max_indices[1]
            max_indices[1] = max_indices[0]
            max_indices[0] = i
        elif max_indices[1] == -1 or num > lst[max_indices[1]]:
            max_indices[2] = max_indices[1]
            max_indices[1] = i
        elif max_indices[2] == -1 or num > lst[max_indices[2]]:
            max_indices[2] = i

if max_indices[1] != -1 and max_indices[2] != -1:
    lst[max_indices[1]], lst[max_indices[2]
                             ] = lst[max_indices[2]], lst[max_indices[1]]
    print("\nИзмененный список:")
    print(" ".join(f"{element:.2f}" for element in lst))
    print(
        f"{max_indices[1] + 1} элемент обменялся местом с {max_indices[2] + 1} элементом")
else:
    print("Нет второго или третьего максимума")
