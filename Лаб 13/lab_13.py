# Баянов Дияз, ИУ7-14Б, Лаб 13 БДшечкааа
import os

def select_file_or_folder():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        items = os.listdir(current_dir)
        dirs = [d for d in items if os.path.isdir(os.path.join(current_dir, d))]
        files = [f for f in items if os.path.isfile(os.path.join(current_dir, f)) and f.endswith('.txt')]
        
        print(f"\nТекущая директория: {current_dir}")
        print("Папки:")
        for idx, d in enumerate(dirs, 1):
            print(f"{idx}. {d}")
        print("Файлы:")
        for idx, f in enumerate(files, 1 + len(dirs)):
            print(f"{idx}. {f}")
        print(f"{len(dirs) + len(files) +1}. / (Вверх)")
        print(f"{len(dirs) + len(files) +2}. Выбрать папку")
        print(f"{len(dirs) + len(files) +3}. Отмена выбора")
        
        try:
            choice = int(input("Выберите номер: "))
            if 1 <= choice <= len(dirs):
                current_dir = os.path.join(current_dir, dirs[choice -1])
            elif len(dirs) < choice <= len(dirs) + len(files):
                selected_file = os.path.join(current_dir, files[choice - len(dirs) -1])
                return ('file', selected_file)
            elif choice == len(dirs) + len(files) +1:
                parent_dir = os.path.dirname(current_dir)
                if parent_dir and parent_dir != current_dir:
                    current_dir = parent_dir
                else:
                    print("Вы уже в корневой директории.")
            elif choice == len(dirs) + len(files) +2:
                return ('folder', current_dir)
            elif choice == len(dirs) + len(files) +3:
                print("Выбор отменен.")
                return (None, None)
            else:
                print("Неверный выбор.")
        except ValueError:
            print("Неверный ввод.")

def int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")

def read_database(filename, delimiter='|'):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(delimiter)
            data.append(fields)
    return data

def write_database(filename, data, delimiter='|'):
    with open(filename, 'w', encoding='utf-8') as file:
        for record in data:
            file.write(delimiter.join(record) + '\n')

def initialize_database(directory, delimiter='|'):
    filename = os.path.join(directory)
    num_fields = int_input("Введите количество полей в записи: ")
    field_names = []
    for i in range(num_fields):
        field = input(f"Введите название поля {i +1}: ")
        field_names.append(field)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(delimiter.join(field_names) + '\n')
    
    print(f"База данных инициализирована в файле {filename} с полями: {', '.join(field_names)}")
    
    while True:
        add_now = input("Хотите добавить запись сейчас? (y/n): ").strip().lower()
        if add_now == 'y':
            record = []
            for field in field_names:
                value = input(f"Введите значение для '{field}': ")
                record.append(value)
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(delimiter.join(record) + '\n')
            print("Запись добавлена.")
        elif add_now == 'n':
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 'y' или 'n'.")

def add_entry(filename, delimiter='|'):
    with open(filename, 'r', encoding='utf-8') as file:
        field_names = file.readline().strip().split(delimiter)
    record = []
    for field in field_names:
        value = input(f"Введите значение для '{field}': ")
        record.append(value)
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(delimiter.join(record) + '\n')
    print("Запись добавлена.")

def display_fields(field_names):
    print("Доступные поля для поиска:")
    for idx in range(len(field_names)):
        print(f"{idx + 1}. {field_names[idx]}")

def print_database(filename, delimiter='|'):
    if not os.path.exists(filename):
        print("Файл базы данных не найден.")
        return

    data = read_database(filename, delimiter)
    
    if not data:
        print("База данных пуста.")
        return

    column_widths = [max(len(str(field)) for field in column) for column in zip(*data)]
    separator = "+-" + "-+-".join('-' * width for width in column_widths) + "-+"

    print(separator)
    for row in data:
        print(
            "| " +
            " | ".join("{:<{width}}".format(field, width=column_widths[i]) for i, field in zip(range(len(row)), row)) +
            " |"
        )
    print(separator)

def search_by_field(filename, delimiter='|'):
    with open(filename, 'r', encoding='utf-8') as file:
        field_names = file.readline().strip().split(delimiter)
        display_fields(field_names)
        while True:
            try:
                field_num = int(input("Введите номер поля для поиска: "))
                if 1 <= field_num <= len(field_names):
                    field_index = field_num - 1
                    break
                else:
                    print("Номер поля вне диапазона. Попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите номер поля.")

        search_value = input("Введите значение для поиска (подстрока): ").strip().lower()
        found = False
        print("\nНайденные записи:")
        for line in file:
            record = line.strip().split(delimiter)
            if search_value in record[field_index].lower():
                print(delimiter.join(record))
                found = True
        if not found:
            print("Записи не найдены.")

def search_by_two_fields(filename, delimiter='|'):
    with open(filename, 'r', encoding='utf-8') as file:
        field_names = file.readline().strip().split(delimiter)
        display_fields(field_names)
        while True:
            try:
                field_num1 = int(input("Введите номер первого поля для поиска: "))
                if 1 <= field_num1 <= len(field_names):
                    field_index1 = field_num1 - 1
                    break
                else:
                    print("Номер поля вне диапазона. Попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите номер поля.")

        while True:
            try:
                field_num2 = int(input("Введите номер второго поля для поиска: "))
                if 1 <= field_num2 <= len(field_names):
                    field_index2 = field_num2 - 1
                    break
                else:
                    print("Номер поля вне диапазона. Попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите номер поля.")

        search_value1 = input("Введите значение для первого поля (подстрока): ").strip().lower()
        search_value2 = input("Введите значение для второго поля (подстрока): ").strip().lower()
        found = False
        print("\nНайденные записи:")
        for line in file:
            record = line.strip().split(delimiter)
            if search_value1 in record[field_index1].lower() and search_value2 in record[field_index2].lower():
                print(delimiter.join(record))
                found = True
        if not found:
            print("Записи не найдены.")

def print_menu():
    print("\nМеню:")
    print("1. Выбрать файл или папку для работы")
    print("2. Инициализировать базу данных")
    print("3. Вывести содержимое базы данных")
    print("4. Добавить запись в конец базы данных")
    print("5. Поиск по одному полю")
    print("6. Поиск по двум полям")
    print("0. Выход")

def main():
    selected_type = None
    filename = ''
    foldername = ''
    while True:
        print_menu()
        choice = int_input("Выберите желаемое действие: ")
        match choice:
            case 1:
                selected_type, path = select_file_or_folder()
                if selected_type == 'file':
                    filename = path
                    print(f"Файл {filename} успешно загружен.")
                elif selected_type == 'folder':
                    foldername = path
                    base_filename = 'database.txt'
                    filename = os.path.join(foldername, base_filename)
                    if os.path.exists(filename):
                        i = 1
                        while True:
                            new_filename = os.path.join(foldername, f'database{i}.txt')
                            if not os.path.exists(new_filename):
                                filename = new_filename
                                break
                            i += 1
                    print(f"Файл {filename} будет использоваться для базы данных.")
                else:
                    print("Ничего не выбрано.")
            case 2:
                if filename:
                    initialize_database(filename)
                else:
                    print("Сначала выберите файл или папку для работы.")
            case 3:
                if filename:
                    db_file = filename if filename else os.path.join(filename)
                    print_database(db_file)
                else:
                    print("Сначала выберите файл или папку для работы.")
            case 4:
                if filename:
                    db_file = filename if filename else os.path.join(filename)
                    add_entry(db_file)
                else:
                    print("Сначала выберите файл или папку для работы.")
            case 5:
                if filename:
                    db_file = filename if filename else os.path.join(filename)
                    search_by_field(db_file)
                else:
                    print("Сначала выберите файл или папку для работы.")
            case 6:
                if filename:
                    db_file = filename if filename else os.path.join(filename)
                    search_by_two_fields(db_file)
                else:
                    print("Сначала выберите файл или папку для работы.")
            case 0:
                print("Выход из программы.")
                break
            case _:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()