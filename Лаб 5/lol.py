def choice_input(): 
    # ввод числа для выбора команды с проверкой диапазона 
    print('Введите номер команды: ', end='') 
    try: 
        n = int(input()) 
        if 0 <= n <= 6: 
            return n 
        else: 
            print('Значения вне промежутка доступных команд, попробуйте ещё раз. ',) 
            return choice_input() 
    except ValueError: 
        print('Введено некорректное значение, введите ещё раз. ') 
        return choice_input() 
 
 
def int_input(): 
    # ввод целого числа без проверки диапазона 
    try: 
        n = int(input()) 
        return n 
    except ValueError: 
        print('Введено некорректное значение, введите ещё раз: ', end='') 
        return int_input() 
 
 
def str_input(): 
    # ввод строки с проверкой на пустоту 
    n = input() 
    if len(n) != 0: 
        return n 
    else: 
        print('Некорректный ввод, попробуйте ещё раз: ', end='') 
        return str_input() 
 
 
def database_menu(choice=1, file=None): 
    # главное меню программы 
    match choice: 
        case 0: 
            print('Вы вышли из программы.') 
        case 1: 
            print('1. Выбор файла.') 
            file = file_selection() 
            menu_output() 
            database_menu(choice_input(), file) 
        case 2: 
            print('2. Инициализация базы данных.\n') 
            data_head_output() 
            database_init(file) 
            menu_output() 
            database_menu(choice_input(), file) 
        case 3: 
            print('3. Вывод базы данных.\n') 
            file_output(file) 
            menu_output() 
            database_menu(choice_input(), file) 
        case 4: 
            print('Добавление данных в базу.\n') 
            data_head_output() 
            database_add_data(file) 
            menu_output() 
            database_menu(choice_input(), file) 
        case 5: 
            if is_file_not_empty(file): 
                print('Поиск по возрасту.\n') 
                print('Введите возраст, по которому хотите начать поиск: ', end='') 
                target_age = int_input() 
                filter_by_age(file, target_age) 
            else: 
                print('База данных пуста, искать нечего.') 
            menu_output() 
            database_menu(choice_input(), file) 
        case 6: 
            if is_file_not_empty(file): 
                print('Поиск по возрасту и должности.\n') 
                print('Введите возраст, по которому хотите начать поиск: ', end='') 
                target_age = int_input() 
                print('Введите должность, по которой хотите вести поиск: ', end='') 
                target_post = str_input() 
                filter_by_age_and_post(file, target_age, target_post) 
            else: 
                print('База данных пуста, искать нечего.') 
            menu_output() 
            database_menu(choice_input(), file) 
 
 
def file_selection(): 
    # выбор файла 
    print('Для выбора файла введите его название.') 
    print('Поддерживаются как относительные, так и абсолютные пути.') 
    print('Введите название файла: ', end='') 
    file = input() 
    return file 
 
 
def data_head_output(): 
    # вывод описания структуры базы данных 
    print('База данных представляет из себя информацию о сотрудниках: ') 
    print('Их ID (число), Имя (слово), Возраст (число), Должность (слово).\n') 
 
 
def line_output(line): 
    # создание строки с выравниванием данных 
    id_person, name, age, post = line.split(';') 
 
    def align_data_left(string, width): 
        string = str(string) 
        if len(string) > width: 
            return string[:width] 
        return string + ' ' * (width - len(string)) 
 
    line = f' {align_data_left(id_person, 10)} |' 
    line += f' {align_data_left(name, 20)} |'

    line += f' {align_data_left(age, 8)} |' 
    line += f' {align_data_left(post, 15)}' 
    return line 
 
 
def file_write(f): 
    # добавление строки в файл c проверкой на ввод 
    unprocessed_line = input('Введите элементы строки: ') 
    if unprocessed_line != '': 
        if unprocessed_line.count(';') != 3: 
            print('Введено некорректное количество данных.') 
            return file_write(f) 
 
        try: 
            id_person, _, age, _ = unprocessed_line.split(';') 
            id_person = int(id_person) 
            age = int(age) 
        except ValueError: 
            print('ID и возраст должны быть числами. Введите данные снова.') 
            return file_write(f) 
 
        f.write('\n' + unprocessed_line) 
        return file_write(f) 
 
 
def description(): 
    # вывод описания формата ввода данных 
    print('Ввод элементов строки происходит через ; в следующем виде:') 
    print('name1;name2;name3;name4') 
    print('Для завершения ввода нажмите клавишу enter.\n') 
 
 
def database_init(file): 
    # инициализация базы данных с добавлением заголовков 
    description() 
    with open(file, 'w', encoding='utf-8') as f: 
        f.write('ID;Имя;Возраст;Должность') 
        file_write(f) 
 
 
def database_add_data(file): 
    # добавление новых записей в базу данных 
    description() 
    with open(file, 'a', encoding='utf-8') as f: 
        file_write(f) 
 
 
def file_output(file): 
    # вывод содержимого базы данных 
    with open(file, 'r', encoding='utf-8') as f: 
        for line in f: 
            print(line_output(line).strip()) 
 
 
def find_info_from_data_lines(file, target_age): 
    # поиск записей в базе данных по возрасту 
    print('Строки, найденные по запросу:') 
    with open(file, 'r', encoding='utf-8') as f: 
        next(f) 
        for line in f: 
            print(line) 
            parts = line.split('|') 
            get_age = int(parts[2].strip()) 
            if get_age == target_age: 
                print(line.strip()) 
 
 
def filter_by_age(file, target_age): 
    # фильтрация записей по возрасту 
    print('Строки, найденные по запросу:') 
    with open(file, 'r', encoding='utf-8') as f: 
        next(f) 
        l = [line.strip() for line in f] 
        for line in l: 
            parts = str(line).split(';') 
            get_age = int(parts[2].strip()) 
            if get_age == target_age: 
                print(line_output(line.strip())) 
 
 
def is_file_not_empty(file): 
    # проверка, что файл содержит данные помимо заголовка 
    with open(file, 'r', encoding='utf-8') as f: 
        lines = f.readlines() 
        return len(lines) > 1 
 
 
def filter_by_age_and_post(file, target_age, target_post): 
    # фильтрация записей по возрасту и должности 
    print('Строки, найденные по запросу:') 
    with open(file, 'r', encoding='utf-8') as f: 
        next(f) 
        for line in f: 
            parts = line.split(';') 
            get_age = int(parts[2].strip()) 
            get_post = parts[3].strip() 
            if (get_age == target_age) and (get_post == target_post): 
                print(line_output(line.strip())) 
 
 
def menu_output(): 
    # вывод списка доступных команд 
    print('''    
    0. Выйти из программы. 
    1. Выбрать файл для работы. 
    2. Инициализировать базу данных. 
    3. Вывести содержимое базы данных. 
    4. Добавить запись в конец базы данных. 
    5. Поиск по одному полю. 
    6. Поиск по двум полям. 
    ''') 
 
 
database_menu() 
