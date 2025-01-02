import re

VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

def print_text(text: list[str]):
    print(" | " + '-' * 80 + " | ")
    for line in text:
        print(" | " + line + " | ")
    print(" | " + '-' * 80 + " | ")

def justify_line(line, width=80):
    words = line.split()
    if not words:
        return ' ' * width
    if len(words) == 1:
        return line.ljust(width)
    total_spaces = width - sum(len(word) for word in words)
    spaces_between = len(words) - 1
    spaces = [' ' * (total_spaces // spaces_between + (i < total_spaces % spaces_between))
              for i in range(spaces_between)]
    justified = ''.join(word + space for word, space in zip(words, spaces + ['']))
    return justified

def process_text(text):
    i = 0
    while i < len(text):
        line = text[i].strip()
        # Если длина строки больше 80, разбиваем
        if len(line) > 80:
            cut_index = 80
            for idx in range(80, 0, -1):
                if line[idx - 1] in VOWELS:
                    cut_index = idx
                    break
            first_part = line[:cut_index].rstrip()
            second_part = line[cut_index:].lstrip()
            text[i] = first_part
            text.insert(i + 1, second_part)
            # Проверяем текущую строку снова
            continue
        # Если длина строки меньше 40, добавляем слова из следующей строки
        elif len(line) < 40:
            if i + 1 < len(text):
                next_line = text[i + 1]
                words = next_line.split()
                while len(line) < 40 and words:
                    line += ' ' + words.pop(0)
                text[i] = line.strip()
                text[i + 1] = ' '.join(words)
                if not text[i + 1]:
                    text.pop(i + 1)
                    # После изменения следующей строки, нужно проверить её снова
                    continue
            else:
                text[i] = line
        else:
            text[i] = line
        i += 1
    return text

def main():
    text = [
        "Бу, испугался? Не бойся! Я друг! Я тебя не обижу! Иди сюда, иди ко мне, сядь рядом со мной.",
        "Посмотри мне в глаза. Ты видишь? Я тоже тебя вижу! Давай смотреть на друг друга до тех пор",
        ", пока наши глаза не устанут. Ты не хочешь? Почему? Что-то не так?",
    ]
    processed_text = process_text(text)
    justified_lines = [justify_line(line) for line in processed_text]
    print_text(justified_lines)

if __name__ == "__main__":
    main()