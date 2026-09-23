def calculator_main (a, b, func):
    return func(a, b)

def calculator_power (num):
    return num * num

def float_conversion (x):
    while True:
        try:
            return float(input(x))
        except:
            print("Вы ввели не число")

num1 = float_conversion("Введите число")
operation = input("Выберите операцию (Введите +, -, *, / или ^2)")
if operation == '^2':
    print(calculator_power(num1))
elif operation == '+':
    num2 = float_conversion("Введите число")
    print(calculator_main(num1, num2, lambda num1, num2: num1 + num2))
elif operation == '-':
    num2 = float_conversion("Введите число")
    print(calculator_main(num1, num2, lambda num1, num2: num1-num2))
elif operation == '*':
    num2 = float_conversion("Введите число")
    print(calculator_main(num1, num2, lambda num1, num2: num1*num2))
elif operation == '/':
    num2 = float_conversion("Введите число")
    print('Ошибка деления: деление на ноль') if num2==0 else print(calculator_main(num1, num2, lambda num1, num2: num1/num2))
else:
    print("Ошибка ввода. Введите +, -, *, / или ^2")


