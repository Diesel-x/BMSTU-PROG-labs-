import time
# сортировка расчёсткой, Баянов Дияз, ИУ7-14Б, защита лаб 12
def getNextgap(gap):
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap

def timer(function):
    # start_time = time.time()
    # sorted_arr = comb_sort(arr)
    # end_time = time.time()
    # elapsed_time = (end_time - start_time) * 1000000000000
    # return elapsed_time, sorted_arr

    def wrapper(*args, **kwargs):
        now = time.time()
        result = function(*args, **kwargs)
        print(time.time() - now)
        return result
    return wrapper

@timer
def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped == 1:
        gap = getNextgap(gap)
        swapped = False
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr


def input_int_array():
    arr = None
    while True:
        try:
            arr = list(map(int, input("Введите целочисленные элементы массива через пробел: ").split()))
            if (len(arr) == 0):
                print("Массив должен быть больше 0")
                continue
            break
        except ValueError:
            print("Массив введён некорректно")
    return arr

def main():
    array = input_int_array()
    print("Исходный список:", array)
    array = array * 100
    array = comb_sort(array)
    print("Отсортированный список:", array)

if __name__ == "__main__":
    main()