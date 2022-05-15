import random
import math

print("Операции:\n"
      "'+' - Сложение\n"
      "'-' - Вычитание\n"
      "'*' - Умножение\n"
      "'/' - Деление\n"
      "'pow' - Возведение в степень\n"
      "'module' - Модуль\n"
      "'random' - Рандомное число\n"
      "'f' - Факториал\n"
      "'arccos' - Арккосинус\n")

operation = input("Введите операцию:")

def plus(num1, num2):
    rsum = num1 + num2
    return rsum

def minus(num1, num2):
    result_minus = num1 - num2
    return result_minus

def umn(num1, num2):
    result_multiply = num1 * num2
    return result_multiply

def delenie(num1, num2):
    result_division = num1 / num2
    return result_division

def step(num1, num2):
    result_pow = pow(num1, num2)
    return result_pow

def modul(num):
    result_mod = abs(num)
    return result_mod

def factorial(num):
    result_fac = math.factorial(num)
    return result_fac

def arccos(num):
    result_arc = math.acos(num)
    return result_arc

if operation == '+':
    number1 = float(input('Ведите первое число '))
    number2 = float(input('Введите второе число:'))
    result = plus(number1, number2)
    print('Ответ: ', result)

elif operation == '-':
    number1 = float(input('Ведите первое число '))
    number2 = float(input('Введите второе число:'))
    result = minus(number1, number2)
    print('Ответ: ', result)

elif operation == '*':
    number1 = float(input('Ведите первое число '))
    number2 = float(input('Введите второе число:'))
    result = umn(number1, number2)
    print('Ответ: ', result)

elif operation == '/':
    number1 = float(input('Ведите первое число '))
    number2 = float(input('Введите второе число:'))
    result = delenie(number1, number2)
    print('Ответ: ', result)

elif operation == 'pow':
    number1 = float(input('Ведите первое число '))
    number2 = float(input('Введите второе число:'))
    result = step(number1, number2)
    print('Ответ: ', result)

if operation == 'random':
    rand = (random.randint(0, 9999))
    print('Ответ: ', rand)
    quit()

if operation == 'module':
    number = float(input('Введите число: '))
    result = modul(number)
    print('Ответ: ', result)
    quit()
if operation == 'f':
    number = float(input('Введите число: '))
    result = factorial(number)
    print('Ответ: ', result)
    quit()
if operation == 'arccos':
    number = float(input('Введите число: '))
    result = arccos(number)
    print('Ответ: ', result)
    quit()
