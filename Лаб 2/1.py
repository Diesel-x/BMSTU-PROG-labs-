# Баянов Дияз Гайсаевич; ИУ7-14Б
# Лаб работа №2; Часть 2; Задание 1; Вариант 4

# Имрорт библиотек
import math as m

# Ввод данных
x = float(input("Введите x: " ))

# Решение и вывод
print(f"Результат выполнения 1-го уравнения, где x <= 5: {-x - 5}" 
      if x <= -5 else "x не подходит условию x <= -5")
print(f"Результат выполнения 2-го уравнения, где -5 < x <= 0: {x + 5}" 
      if -5 < x and x <= 0 else "x не подходит условию, где -5 < x <= 0")
print(f"Результат выполнения 3-го уравнения, где x >= 5: {m.sqrt(25 - x ** 2)}" 
      if 0 <= x and x <= 5 else "x не подходит условию, где x >= 5")
print(f"Результат выполнения 4-го уравнения, где 0 <= x <= 5: {m.log(x - 4)}" 
      if x >= 5 else "x не подходит условию, где x >= 5")
