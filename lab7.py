import random
import math

class Calc:
    def help(self):
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

    def plus(self, num1, num2):
        rsum = num1 + num2
        return rsum

    def minus(self, num1, num2):
        result_minus = num1 - num2
        return result_minus

    def umn(self, num1, num2):
        result_multiply = num1 * num2
        return result_multiply

    def delenie(self, num1, num2):
        result_division = num1 / num2
        return result_division

    def step(self, num1, num2):
        result_pow = pow(num1, num2)
        return result_pow

    def modul(self, num):
        result_mod = abs(num)
        return result_mod

    def factorial(self, num):
        result_fac = math.factorial(num)
        return result_fac

    def arccos(self, num):
        result_arc = math.acos(num)
        return result_arc

    def random(self):
        rand = (random.randint(0, 9999))
        return rand

    def calculate(self):
        self.help()
        operation = input("Введите операцию:")

        if operation == '+':
            number1 = float(input('Ведите первое число '))
            number2 = float(input('Введите второе число:'))
            result = self.plus(number1, number2)

        elif operation == '-':
            number1 = float(input('Ведите первое число '))
            number2 = float(input('Введите второе число:'))
            result = self.minus(number1, number2)

        elif operation == '*':
            number1 = float(input('Ведите первое число '))
            number2 = float(input('Введите второе число:'))
            result = self.umn(number1, number2)

        elif operation == '/':
            number1 = float(input('Ведите первое число '))
            number2 = float(input('Введите второе число:'))
            result = self.delenie(number1, number2)

        elif operation == 'pow':
            number1 = float(input('Ведите первое число '))
            number2 = float(input('Введите второе число:'))
            result = self.step(number1, number2)

        elif operation == 'random':
            result = self.random()

        elif operation == 'module':
            number = float(input('Введите число: '))
            result = self.modul(number)

        elif operation == 'f':
            number = float(input('Введите число: '))
            result = self.factorial(number)

        elif operation == 'arccos':
            number = float(input('Введите число: '))
            result = self.arccos(number)
        return result




calculator = Calc() # создание экземпляра класса Calc()
result = calculator.calculate() # обращение к функции calculate внутри экземпляра calculator класса Calc() 
print('Ответ: ', result)
