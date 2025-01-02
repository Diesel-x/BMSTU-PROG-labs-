# Баянов Дияз ИУ7-14Б, зашита 12 лабы
# Шифр Цезаря

def caesar_cipher(text, shift, direction='encode'):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''

    if direction == 'decode':
        shift = -shift

    text = text.lower()
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = (char_index + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char

    return result

def caesar_cipher_freqently_analisys(text):
    abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    text = text.lower()
    letter_counts = {}
    for i in text:
        if i in abc:
            if i in letter_counts:
                letter_counts[i] += 1
            else:
                letter_counts[i] = 1

    print(letter_counts)
    table = {"а" : 0.062, "б": 0.}
    
    most_common_char = max(letter_counts, key=letter_counts.get)
    shift = (abc.index(most_common_char) - 15) % len(abc)
    return caesar_cipher(text, -shift, direction='decode')

    

def main():
    text = "БУ испугался? Не бойся. Это я, твой друг"

    while True:
        print(text)
        print("1. Зашифровать текст")
        print("2. Расшифровать текст")
        print("3. Выход")
        choice = input("Выберите опцию (1/2/3): ")

        match choice:
            case '1':
                try:
                    shift_value = int(input("Введите шаг сдвига: "))
                    text = caesar_cipher(text, shift_value, direction='encode')
                except ValueError:
                    print("Шаг должен быть числом. Попробуйте снова.")
            case '2':
                try:
                    shift_value = int(input("Введите шаг сдвига: "))
                    text = caesar_cipher(text, shift_value, direction='decode')
                except ValueError:
                    print("Шаг должен быть числом. Попробуйте снова.")
            case '3':
                text = caesar_cipher_freqently_analisys(text)
            case '4':
                print("Выход из программы.")
                break
            case _:
                print("Выход из программы.")
                break

if __name__ == "__main__":
    main()
