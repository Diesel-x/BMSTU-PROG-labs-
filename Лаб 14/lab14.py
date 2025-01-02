#Баянов Дияз ИУ7-14Б лаб 14

import os
import struct
import re

RECORD_FORMAT = 'i 20s 20s 20s'  # id (int), фамилия, имя, отчество
RECORD_SIZE = struct.calcsize(RECORD_FORMAT)

def select_file():
    filename = input("Введите полный путь к файлу для работы: ")
    if (os.path.exists(filename)):
        return filename
    else:
        print("Файл не существует.")
        return None
    

def validate_id():
    while True:
        try:
            id = int(input("Введите id (целое число): "))
            return id
        except ValueError:
            print("ID должен быть целым числом. Попробуйте снова.")

def validate_name(field_name):
    while True:
        name = input(f"Введите {field_name} (до 20 символов): ")
        if len(name) <= 20 :
            return name
        else:
            print(f"{field_name.capitalize()} не превышать 20 символов. Попробуйте снова.")

    
def is_valid_database_file(filename):
    try:
        with open(filename, 'rb') as f:
            bytes_read = f.read(RECORD_SIZE)
            if len(bytes_read) != RECORD_SIZE:
                return False
            record = struct.unpack(RECORD_FORMAT, bytes_read)
            try:
                record[1].decode('utf-8')
                record[2].decode('utf-8')
                record[3].decode('utf-8')
            except UnicodeDecodeError:
                return False
        return True
    except (struct.error, OSError):
        return False

def init_database(filename):
    n = int(input("Введите количество записей для инициализации: "))
    with open(filename, 'wb') as f:
        for _ in range(n):
            id = validate_id()
            last_name = validate_name("фамилию")
            first_name = validate_name("имя")
            patronymic = validate_name("отчество")

            record = struct.pack(
                RECORD_FORMAT,
                id,
                last_name.encode('utf-8').ljust(20)[:20],
                first_name.encode('utf-8').ljust(20)[:20],
                patronymic.encode('utf-8').ljust(20)[:20]
            )
            f.write(record)
    print("База данных инициализирована успешно.")


def print_database(filename):
    if not os.path.exists(filename):
        print("Файл не существует.")
        return
    with open(filename, 'rb') as f:
        index = 1
        header = "{:<5} {:<10} {:<20} {:<20} {:<20}".format("№", "ID", "Фамилия", "Имя", "Отчество")
        print(header)
        print("-" * len(header))
        while True:
            bytes_read = f.read(RECORD_SIZE)
            if not bytes_read:
                break
            record = struct.unpack(RECORD_FORMAT, bytes_read)
            id = record[0]
            last_name = record[1].decode('utf-8').strip()
            first_name = record[2].decode('utf-8').strip()
            patronymic = record[3].decode('utf-8').strip()
            row = "{:<5} {:<10} {:<20} {:<20} {:<20}".format(index, id, last_name, first_name, patronymic)
            print(row)
            index += 1

def add_record(filename):
    pos = int(input("Введите позицию для вставки записи: "))
    with open(filename, 'rb+') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()
        total_records = file_size // RECORD_SIZE
        if pos < 1 or pos > total_records + 1:
            print("Некорректная позиция.")
            return
        # Сдвиг записей для вставки
        for i in range(total_records, pos - 1, -1):
            f.seek((i - 1) * RECORD_SIZE)
            data = f.read(RECORD_SIZE)
            f.seek(i * RECORD_SIZE)
            f.write(data)
        # Добавление новой записи
        f.seek((pos - 1) * RECORD_SIZE)

        id = validate_id()
        last_name = validate_name("фамилию")
        first_name = validate_name("имя")
        patronymic = validate_name("отчество")

        record = struct.pack(
            RECORD_FORMAT,
            id,
            last_name.encode('utf-8').ljust(20)[:20],
            first_name.encode('utf-8').ljust(20)[:20],
            patronymic.encode('utf-8').ljust(20)[:20]
        )
        f.write(record)
    print("Запись добавлена успешно.")

def delete_record(filename):
    pos = int(input("Введите позицию для удаления записи: "))
    with open(filename, 'rb+') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()
        total_records = file_size // RECORD_SIZE
        if pos < 1 or pos > total_records:
            print("Некорректная позиция.")
            return
        # Сдвиг записей для удаления
        for i in range(pos, total_records):
            f.seek(i * RECORD_SIZE)
            data = f.read(RECORD_SIZE)
            f.seek((i - 1) * RECORD_SIZE)
            f.write(data)
        f.truncate((total_records - 1) * RECORD_SIZE)
    print("Запись удалена успешно.")

def search_one_field(filename):
    search_id = int(input("Введите id для поиска: "))
    found = False
    with open(filename, 'rb') as f:
        index = 1
        header = "{:<5} {:<10} {:<20} {:<20} {:<20}".format("№", "ID", "Фамилия", "Имя", "Отчество")
        print(header)
        print("-" * len(header))
        while True:
            bytes_read = f.read(RECORD_SIZE)
            if not bytes_read:
                break
            record = struct.unpack(RECORD_FORMAT, bytes_read)
            id = record[0]
            if id == search_id:
                last_name = record[1].decode('utf-8').strip()
                first_name = record[2].decode('utf-8').strip()
                patronymic = record[3].decode('utf-8').strip()
                row = "{:<5} {:<10} {:<20} {:<20} {:<20}".format(index, id, last_name, first_name, patronymic)
                print(row)
                found = True
            index += 1
    if not found:
        print("Запись с таким ID не найдена.")

def search_two_fields(filename):
    search_first_name = input("Введите имя для поиска: ").strip().lower()
    search_last_name = input("Введите фамилию для поиска: ").strip().lower()
    found = False
    with open(filename, 'rb') as f:
        index = 1
        header = "{:<5} {:<10} {:<20} {:<20} {:<20}".format("№", "ID", "Фамилия", "Имя", "Отчество")
        print(header)
        print("-" * len(header))
        while True:
            bytes_read = f.read(RECORD_SIZE)
            if not bytes_read:
                break
            record = struct.unpack(RECORD_FORMAT, bytes_read)
            id = record[0]
            last_name = record[1].decode('utf-8').strip()
            first_name = record[2].decode('utf-8').strip()
            if first_name.lower() == search_first_name and last_name.lower() == search_last_name:
                patronymic = record[3].decode('utf-8').strip()
                row = "{:<5} {:<10} {:<20} {:<20} {:<20}".format(index, id, last_name, first_name, patronymic)
                print(row)
                found = True
            index += 1
    if not found:
        print("Запись с такими именем и фамилией не найдена.")

def main():
    filename = ''
    is_valid = False
    while True:
        print("\nМеню:")
        print("1. Выбрать файл для работы")
        print("2. Инициализировать базу данных")
        print("3. Вывести содержимое базы данных")
        print("4. Добавить запись")
        print("5. Удалить запись")
        print("6. Поиск по одному полю (ID)")
        print("7. Поиск по двум полям (Имя и Фамилия)")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            filename = select_file()
            if filename != '':
                print(f"Файл '{filename}' выбран для работы.")
                is_valid = is_valid_database_file(filename)
            else:
                print("Файла нету")
            print()
            
        elif choice == '2':
            if filename:
                init_database(filename)
                is_valid = True
            else:
                print("Сначала выберите файл для работы (опция 1).")
        elif choice == '3':
            if filename:
                if is_valid == True:
                    print_database(filename)
                else:
                    print("Файл не рассчитан на использование как бд")
            else:
                print("Сначала выберите файл для работы (опция 1).")
        elif choice == '4':
            if filename:
                if is_valid == True:
                    add_record(filename)  
                else:
                    print("Файл не рассчитан на использование как бд")
            else:
                print("Сначала выберите файл для работы (опция 1).")
        elif choice == '5':
            if filename:
                if is_valid == True:
                    delete_record(filename)  
                else:
                    print("Файл не рассчитан на использование как бд")
            else:
                print("Сначала выберите файл для работы (опция 1).")
        elif choice == '6':
            if filename:
                if is_valid == True:
                    search_one_field(filename)  
                else:
                    print("Файл не рассчитан на использование как бд")
            else:
                print("Сначала выберите файл для работы (опция 1).")
        elif choice == '7':
            if filename:
                if is_valid == True:
                    search_two_fields(filename)  
                else:
                    print("Файл не рассчитан на использование как бд")
            else:
                print("Сначала выберите файл для работы (опция 1).")
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()