import random
import math

print("Операции:\n"
      "'+' - Сложение\n"
      "'-' - Вычитание\n"
      "'*' - Умножение\n"
      "'/' - Деление\n"
      "'pow' - Возведение в степень\n"
      "'module' - Модуль\n"
      "'0' - Рандомное число\n"
      "'f' - Факториал\n"
      "'arccos' - Арккосинус\n")
operation = input("Введите операцию:")
if operation in ('+', '-', '*', '/'):
    a = float(input("Введите первое число:"))
    b = float(input("Введите второе число:"))
    if operation == '+':
        print(a+b)
    elif operation == '-':
        print(a-b)
    elif operation == '*':
        print(a*b)
    elif operation == '/':
        if b != 0:
            print(a / b)
        else:
            print("Делить на 0 нельзя))")
if operation in ('pow'):
    a = float(input("Введите число:"))
    b = float(input("Введите степень:"))
    print(pow(a,b))
if operation in ('module'):
    a = float(input("Введите число:"))
    print(abs(a))
if operation in ('0'):
    print("Рандомное число:", random.randint(0, 9999))
if operation in ('f'):
    a = int(input("Введите число:"))
    print(math.factorial(a))
if operation in ('arccos'):
    a = float(input("Введите число:"))
    print(math.acos(a))
