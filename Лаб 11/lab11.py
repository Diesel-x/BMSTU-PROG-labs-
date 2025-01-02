# Лабараторная работа №11, Баянов Дияз, группа ИУ7-14Б
# Метод сортировки вставками с барьером

import time
import random
from inputs4labs import input_float_array

def insertion_sort_with_barrier(arr):
    # Добавляем барьер в начало массива
    arr = [0] + arr
    permutations = 0  # Инициализируем счетчик перестановок

    # Начинаем сортировку с второго элемента (индекс 2), так как первый элемент - барьер
    for i in range(2, len(arr)):
        if arr[i - 1] > arr[i]:
            arr[0] = arr[i]  # Барьер
            j = i - 1
            permutations += 1  # Учитываем перестановку при сравнении

            # Сдвигаем элементы вправо, пока не найдем правильное место для вставки arr[0]
            while arr[j] > arr[0]:
                arr[j + 1] = arr[j]  # Сдвигаем элемент вправо
                j -= 1  # Переходим к предыдущему элементу
                permutations += 1  # Учитываем перестановку

            arr[j + 1] = arr[0]  # Вставляем arr[0] на правильное место

    return arr[1:], permutations  # Возвращаем отсортированный массив (без барьера) и количество перестановок

# Функция, чтобы числа в табличке были красивыми
def format_number(num):
    if isinstance(num, float) and num.is_integer():
        return int(num)
    else:
        return num

def measure_sort_time(arr):
    start_time = time.time()
    sorted_arr, permutations = insertion_sort_with_barrier(arr)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    return elapsed_time, permutations

def print_table(headers, table):
    # Заголовки таблицы
    print(f"{'Тип списка':<25}", end="")
    for header in headers:
        print(f"{header:<30}", end="")
    print()
    # Подзаголовки 
    print(f"{'':<25}", end="")
    for _ in headers:
        print(f"{'Время (милисек.)':<15}{'Перестановки':<15}", end="")
    print()
    # Данные таблицы
    for row in table:
        print(f"{row[0]:<25}", end="")
        for cell in row[1:]:
            print(f"{cell[0]:<15}{cell[1]:<15}", end="")
        print()

def main():
    # Этап 1:
    user_array = input_float_array()
    print("\nПользовательский массив:", [format_number(x) for x in user_array])
    sorted_user_array, _ = insertion_sort_with_barrier(user_array)
    print("Отсортированный пользовательский массив:", [format_number(x) for x in sorted_user_array])

    # Этап 2:
    while True:
        try:
            sizes = list(map(int, input("Введите три размерности списков через пробел: ").split()))
            if len(sizes) != 3 or any(size <= 0 for size in sizes):
                raise ValueError
            break
        except ValueError:
            print("Ошибка: введите три положительных целых числа через пробел.")

    headers = [f"Размер {size}" for size in sizes]

    table = [
        ["Случайный список"],
        ["Отсортированный список"],
        ["Обратный порядок"]
    ]

    for size in sizes:
        random_list = [random.uniform(0, 100) for _ in range(size)]
        sorted_list = list(range(size))
        reverse_sorted_list = sorted_list[::-1]

        random_time, random_permutations = measure_sort_time(random_list)
        sorted_time, sorted_permutations = measure_sort_time(sorted_list)
        reverse_time, reverse_permutations = measure_sort_time(reverse_sorted_list)

        table[0].append((f"{random_time:.7f}", random_permutations))
        table[1].append((f"{sorted_time:.7f}", sorted_permutations))
        table[2].append((f"{reverse_time:.7f}", reverse_permutations))

    print()
    print_table(headers, table)

if __name__ == "__main__":
    main()
    