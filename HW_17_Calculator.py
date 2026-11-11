import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculator with operations: add, sub, mul, div, pow')
    parser.add_argument('--a', '-a', help='Enter any first number', type=float, required=True)
    parser.add_argument('--b', '-b', help='Enter any second number', type=float, required=True)
    parser.add_argument('--operation', '-op', choices=['add', 'sub', 'mul', 'div', 'pow'], help='Enter any of the operations: add, sub, mul, div, pow', required=True)
    args = parser.parse_args()

    if args.operation == 'add':
        print(add(args.a, args.b))
    elif args.operation == 'sub':
        print(subtract(args.a, args.b))
    elif args.operation == 'mul':
        print(multiply(args.a, args.b))
    elif args.operation == 'div':
        try:
            print(divide(args.a, args.b))
        except ZeroDivisionError:
            print('Ошибка деления: деление на ноль')
    elif args.operation == 'pow':
        print(power(args.a, args.b))
