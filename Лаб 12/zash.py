# Баянов Дияз, защита 12 лабы; 6 пункт (все математические операции + степень) 

import re

def print_text(text: list[str]):
    for line in text:
        print(line.strip())

def evaluate_expression(expr: str) -> str:
    try:
        result = eval(expr)
        return str(int(result)) if result == int(result) else str(result)
    except Exception:
        return expr

def do_math(text: list[str]) -> list[str]:
    pattern = re.compile(r'\b\d+\s*[\+/]\s*\d+\b')
    for i, line in enumerate(text):
        expressions = pattern.findall(line)
        for expr in expressions:
            result = evaluate_expression(expr)
            line = line.replace(expr, result)
        text[i] = line
    return text

def main():
    text = [
            "Бу, испугался 1+1-1? Не бойся 8*9! Я друг! Я тебя не обижу!",
            "Иди сюда, иди ко мне, сядь рядом со мной. 38 +  /1      78 Посмотри мне в глаза. Ты видишь 4**2**0.5?",
            "Я тоже тебя вижу! 3*4/ 3 /0 Давай смотреть  7*7 на друг друга до тех 7**3 пор, пока наши глаза не устанут.",
            "Ты не хочешь? Почему? Что-то не так? 10  /2"
    ]

    print_text(text)
    text = do_math(text)
    print("\nТекст после выполнения математических операций:")
    print_text(text)

if __name__ == "__main__":
    main()