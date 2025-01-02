# Баянов Дияз. ИУ7-14Б
# ЛР 15. Программа для пункта 3
# Сортировка чисел методом вставок с барьером и работа с одним файлом

import struct
import os

def create_binary_file(file_name, numbers):
    with open(file_name, 'wb') as f:
        for num in numbers:
            f.write(struct.pack('i', num)) 


def read_number(file, pos):
    file.seek(pos * 4)
    return struct.unpack('i', file.read(4))[0]


def write_number(file, pos, number):
    file.seek(pos * 4)
    file.write(struct.pack('i', number))


def sort_binary_file(file_name):
    with open(file_name, 'r+b') as f:
        file_size = os.path.getsize(file_name)
        n = file_size // 4  # Количество чисел в файле

        for i in range(1, n):
            # Считываем текущее число
            current = read_number(f, i)

            # Барьер: считываем предыдущее число
            j = i - 1
            while j >= 0 and read_number(f, j) > current:
                # Сдвигаем число вправо
                temp = read_number(f, j)
                write_number(f, j + 1, temp)
                j -= 1

            # Вставляем текущее число в правильную позицию
            write_number(f, j + 1, current)


if __name__ == "__main__":
    file_name = "user_data.bin"
    numbers = [34, 7, -23, 32, 5, 62]

    create_binary_file(file_name, numbers)

    print("До сортировки:")
    with open(file_name, 'rb') as f:
        print([read_number(f, i) for i in range(len(numbers))])

    sort_binary_file(file_name)
    print("После сортировки:")
    with open(file_name, 'rb') as f:
        print([read_number(f, i) for i in range(len(numbers))])
