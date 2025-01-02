#Баянов Дияз Гайсаевич, лаба 10, вар 6
#Левые прямоугольники и 3/8

# Требуется написать программу для вычисления приближённого значения интеграла
# известной, заданной в программе, функции двумя разными методами (по варианту).
# Программа должна позволять задать начало и конец отрезка интегрирования, а также
# N1 и N2 - количества участков разбиения.

# Далее на основе известной, заданной в программе, первообразной определить, какой
# метод является наиболее точным. Для этого требуется вычислить и отобразить
# абсолютную и относительную погрешности каждого из четырёх измерений. Метод,
# измерение которого с одним из разбиений дало самое близкое к первообразной
# значение, считается наиболее точным.
# Затем для другого, менее точного метода, итерационно вычислить количество участков
# разбиения, для которого интеграл будет вычислен с заданной точностью, на основе
# формулы:
# |𝐼(𝑁) − 𝐼(2𝑁)| < ε

# Вывести приближенное значение интеграла и количество отрезков, необходимых для
# его вычисления.
# Интегрируемую функцию и первообразную необходимо описать в виде программных
# функций, чтобы их можно было легко заменить на произвольные и убедиться, что
# программа работает корректно.
# Для методов интегрирования, использующих более двух точек на одной итерации
# вычислений, считать все отрезки между соседними точками за отдельные участки
# разбиения.
# Если один из методов невозможно применить на заданном количестве участков
# разбиения, в таблице ставится прочерк, однако сама таблица с остальными данными
# выводится.

def f(x):
    # Заданная функция
    return x**2

def F(x):
    # Первообразная функции f(x) = x^2
    return x**3 / 3

# Функция вычисления интегралла методом левых прямоугльников
def left_triangles(a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Функция вычисления интегралла методом 3/8
def method_3_8(a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 3 * f(a + i * h)
    integral *= 3 * h / 8
    return integral

#Функция вычисления абсолютной погрешности
def absolute_error(approx, exact):
    return abs(approx - exact)

#Функция вычисления относительной погрешности
def relative_error(approx, exact):
    return abs(approx - exact) / abs(exact)

# функция вычисления количества участков разбиения
def find_segments_for_accuracy(method, a, b, epsilon):
    n = 1
    while True:
        I_n = method(a, b, n)
        I_2n = method(a, b, 2 * n)
        if abs(I_n - I_2n) < epsilon:
            return n
        n *= 2

def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное числовое значение.")

def int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Ошибка: введите значение больше нуля.")
        except ValueError:
            print("Ошибка: введите корректное целое значение.")

def print_results_table(a, b, n1, n2, integral_left, integral_3_8, exact_value):
    absolute_error_left = absolute_error(integral_left, exact_value)
    relative_error_left = relative_error(integral_left, exact_value)
    absolute_error_3_8 = absolute_error(integral_3_8, exact_value)
    relative_error_3_8 = relative_error(integral_3_8, exact_value)
    print("\nРезультаты вычислений:")
    print(f"{'Метод':<30}{'Количество участков':<25}{'Приближённое значение':<30}{'Абсолютная погрешность':<30}{'Относительная погрешность':<30}")
    print("-" * 160)
    print(f"{'Левые прямоугольники':<30}{n1:<25}{integral_left:<30.7g}{absolute_error_left:<30.7g}{relative_error_left:<30.7g}")
    if n2 % 3 == 0:
        print(f"{'Метод 3/8':<30}{n2:<25}{integral_3_8:<30.7g}{absolute_error_3_8:<30.7g}{relative_error_3_8:<30.7g}")
    else:
        print(f"{'Метод 3/8':<30}{'-':<25}{'-':<30}{'-':<30}{'-':<30}")

def main():
    a = float_input("Введите начало отрезка интегрирования: ")
    b = float_input("Введите конец отрезка интегрирования: ")
    n1 = int_input("Введите количество участков разбиения для метода левых прямоугольников: ")
    
    while True:
        n2 = int_input("Введите количество участков разбиения для метода 3/8 (должно быть кратно 3): ")
        if n2 % 3 == 0:
            break
        else:
            print("Ошибка: количеcтво участков разбиения для метода 3/8 должно быть кратно 3. Попробуйте снова.")

    integral_left_triangles = left_triangles(a, b, n1)
    integral_3_8 = method_3_8(a, b, n2)

    print(f"Приближённое значение интеграла методом левых прямоугольников: {integral_left_triangles:.7g}")
    print(f"Приближённое значение интеграла методом 3/8: {integral_3_8:.7g}")

    exact_value = F(b) - F(a)

    abs_error_left = absolute_error(integral_left_triangles, exact_value)
    rel_error_left = relative_error(integral_left_triangles, exact_value)
    abs_error_simpson = absolute_error(integral_3_8, exact_value)
    rel_error_simpson = relative_error(integral_3_8, exact_value)

    print(f"Абсолютная погрешность метода левых прямоугольников: {abs_error_left:.7g}")
    print(f"Относительная погрешность метода левых прямоугольников: {rel_error_left:.7g}")
    print(f"Абсолютная погрешность метода 3/8: {abs_error_simpson:.7g}")
    print(f"Относительная погрешность метода 3/8: {rel_error_simpson:.7g}")

    print_results_table(a, b, n1, n2, integral_left_triangles, integral_3_8, exact_value)

    if abs_error_left < abs_error_simpson:
        print("Метод левых прямоугольников более точный.")
        epsilon = float_input("Введите требуемую точность для метода 3/8: ")
        n_for_accuracy = find_segments_for_accuracy(method_3_8, a, b, epsilon)
        print(f"Для достижения заданной точности методом 3/8 требуется {n_for_accuracy} участков разбиения.")
    else:
        print("Метод 3/8 более точный.")
        epsilon = float_input("Введите требуемую точность для метода левых прямугольноков: ")
        n_for_accuracy = find_segments_for_accuracy(left_triangles, a, b, epsilon)
        print(f"Для достижения заданной точности методом левых прямоугольников требуется {n_for_accuracy} участков разбиения.")

if __name__ == "__main__":
    main()