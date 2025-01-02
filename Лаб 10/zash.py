# интегралл методом 3/8 F(x, y)dx 
# y = 1, 2, 3 ... 10
# F(x,y) = 2x^3 - 7*x*y + y^2
# ввод a, b, n
# найти F(x,y)

def F(x, y):
    return 2 * x**3 - 7 * x * y + y**2

def method_3_8(a, b, n, y_range):
    h = (b - a) / n
    integral = 0
    for y in range(y_range):
        integral_y = F(a, y) + F(b, y)
        for i in range(1, n):
            if i % 3 == 0:
                integral_y += 2 * F(a + i * h, y)
            else:
                integral_y += 3 * F(a + i * h, y)
        integral_y *= 3 * h / 8
        integral += integral_y
    return integral

def main():
    a = float(input("Введите начало интегрирования a: "))
    b = float(input("Введите конец интегрирования b: "))
    n = 0

    while True:
        n = int(input("Введите кол-во отрезков n (кратное 3): "))
        if n % 3 == 0:
            break
        else:
            print("Ошибка: n должно быть кратно 3. Попробуйте снова.")
    
    y_range = 11

    result = method_3_8(a, b, n, y_range)
    print(f"Приближённое значение двойного интеграла: {result}")

if __name__ == "__main__":
    main()