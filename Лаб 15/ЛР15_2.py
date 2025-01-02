# Баянов Дияз. ИУ7-14Б
# ЛР 15. Программа для пункта 2
# После каждого числа кратного трём добавить его удвоенное значение
import struct
import os

def write_numbers_to_file(filename, numbers):
    with open(filename, 'wb') as f:
        for number in numbers:
            f.write(struct.pack('i', number))

def read_and_process_file(filename):
    # Шаг 1. Подсчитать общее количество чисел (original_count) и количество чётных (even_count).
    original_count = 0
    even_count = 0
    with open(filename, 'rb') as f:
        while (chunk := f.read(4)):
            # chunk = f.read(4)
            # if not chunk:
            #     break
            if len(chunk) < 4:
                print("Неполные данные в файле, оставшиеся байты будут проигнорированы.")
                break
            number = struct.unpack('i', chunk)[0]
            original_count += 1
            if number % 3 == 0:
                even_count += 1

    # Вычислим, сколько в итоге будет 32-битных чисел
    final_count = original_count + even_count
    final_size = final_count * 4

    # Если в файле нет чисел или нет кратных трём — делать нечего
    if original_count == 0 or even_count == 0:
        return

    # Шаг 2. Расширить файл до нужного размера и выполнять "расстановку" с конца.
    with open(filename, 'r+b') as f:
        # Увеличиваем файл до final_size
        f.truncate(final_size)

        # Позиции для чтения и записи (в 4-байтовых ячейках, не в байтах!)
        read_index = original_count - 1      # последний индекс исходных чисел
        write_index = final_count - 1       # последний индекс в расширенном файле

        # Двигаемся от конца исходного массива к началу
        while read_index >= 0:
            # Переходим к позиции read_index и читаем 4 байта
            f.seek(read_index * 4)
            data = f.read(4)
            number = struct.unpack('i', data)[0]

            # Если число кратное 3 — сначала записываем его удвоенную копию
            if number % 3 == 0:
                doubled = number * 2
                f.seek(write_index * 4)
                f.write(struct.pack('i', doubled))
                write_index -= 1

            # Теперь записываем исходное число
            f.seek(write_index * 4)
            f.write(struct.pack('i', number))
            write_index -= 1
            read_index -= 1

def print_file_contents(filename):
    with open(filename, 'rb') as f:
        print(f"Содержимое файла '{filename}':")
        index = 0
        while True:
            chunk = f.read(4)
            if not chunk:
                break
            if len(chunk) < 4:
                print("Неполные данные в конце файла, пропускаем их.")
                break
            number = struct.unpack('i', chunk)[0]
            print(f"[{index}] -> {number}")
            index += 1

def main():
    numbers = [2, 5, 3, 6, 7, 9, 10, 13]  # 6, 10 - чётные
    filename = 'user_data.bin'

    write_numbers_to_file(filename, numbers)
    print("До обработки:")
    print_file_contents(filename)

    read_and_process_file(filename)

    print("После обработки (добавили удвоенное значение после каждого кратного трём элемента):")
    print_file_contents(filename)

if __name__ == "__main__":
    main()