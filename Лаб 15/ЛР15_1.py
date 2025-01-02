# Баянов Дияз. ИУ7-14Б
# ЛР 15. Программа для пункта 1
# Удалить все чётные числа

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


def remove_even_numbers(file_name):
    with open(file_name, 'r+b') as f:
        file_size = os.path.getsize(file_name)
        n = file_size // 4  # Количество чисел в файле

        write_pos = 0  # Позиция записи
        for read_pos in range(n):
            num = read_number(f, read_pos)
            if num % 2 != 0:  # Оставляем только нечетные числа
                write_number(f, write_pos, num)
                write_pos += 1

        f.truncate(write_pos * 4)


if __name__ == "__main__":
    file_name = "user_data.bin"

    numbers = [34, 7, 23, 32, 5, 62]

    create_binary_file(file_name, numbers)

    print("До удаления четных:")
    with open(file_name, 'rb') as f:
        print([read_number(f, i) for i in range(len(numbers))])

    remove_even_numbers(file_name)

    print("После удаления четных:")
    with open(file_name, 'rb') as f:
        file_size = os.path.getsize(file_name)
        print([read_number(f, i) for i in range(file_size // 4)])
