from email.policy import default
from enum import Enum
from dataclasses import dataclass, field

# task 1
def test_info(author, component):
    def decorator(cls):
        cls.author = author
        cls.component = component
        return cls
    return decorator

@test_info(author="Иван", component="Auth")
class TestLogin:
    pass

print(TestLogin.author)
print(TestLogin.component)

#task 2
# PAGES = []

# def register_page(cls):
#     PAGES.append(cls)
#     return cls
#
# @register_page
# class LoginPage:
#     pass
#
# @register_page
# class DashboardPage:
#     pass
#
# print(PAGES)
# print([cls.__name__ for cls in PAGES])

# task 3
# class Tag:
#     def __init__(self, tag_name):
#         self.tag_name = tag_name
#
#     def __call__(self, cls):
#         cls.tag = self.tag_name
#         return cls
#
# @Tag('smoke')
# class SmokeTests:
#     pass
#
# @Tag('regression')
# class RegressionTests:
#     pass
#
# print(SmokeTests.tag)
# print(RegressionTests.tag)

# task 4
# class Environment(Enum):
#     DEV = "https://dev.example.com"
#     STAGE = "https://stage.example.com"
#     PROD = "https://example.com"
#
# def get_base_url(env):
#     if env == Environment.DEV:
#         return Environment.DEV.value
#     elif env == Environment.STAGE:
#         return Environment.STAGE.value
#     elif env == Environment.PROD:
#         return Environment.PROD.value
#     else:
#         return 'Your environment is invalid'
#
# print(get_base_url(Environment.DEV))
# print(get_base_url(Environment.PROD))

# task 5
# class Priority(Enum):
#     LOW = 1
#     MEDIUM = 2
#     HIGH = 3
#
# tasks = [
#     ("Починить тест логина", Priority.HIGH),
#     ("Обновить документацию", Priority.LOW),
#     ("Настроить CI", Priority.MEDIUM),
# ]
#
# # Сортировка по значению enum
#
# tasks_sorted = sorted(tasks, key=lambda t: t[1].value)
#
# for name, prio in tasks_sorted:
#     print(prio.name, "-", name)

# task 6
# class TestType(Enum):
#     API = 1
#     UI = 2
#     UNIT = 3
#
# tests = [
#     ("test_login_api", TestType.API),
#     ("test_login_ui", TestType.UI),
#     ("test_sum", TestType.UNIT),
#     ("test_profile_api", TestType.API),
# ]
#
# def filter_tests_by_type(tests, test_type):
#     filtered_tests = [t for t in tests if t[1] == test_type]
#     return filtered_tests
#
# print(filter_tests_by_type(tests, TestType.API))
# print(filter_tests_by_type(tests, TestType.UI))

# task 7
# def parse_int_list(strings):
#     new_list = []
#     for i in strings:
#         try:
#             int(i)
#             new_list.append(int(i))
#         except ValueError:
#             print(f'the value {i} cannot be converted to int')
#     return new_list
#
# raw = ["10", "20", "abc", "30", "4.5", "40"]
# nums = parse_int_list(raw)
# print(nums)

# task 8
# def calculator_main(a, b, func):
#     return func(a, b)
#
# def calculator_power(num):
#     return num * num
#
# def float_conversion(x):
#     while True:
#         try:
#             return float(input(x))
#         except ValueError:
#             print("Вы ввели не число")
#
# def check_operation(operation):
#     if operation not in ['+', '-', '*', '/', '^2']:
#         raise ValueError('Ошибка ввода. Введите +, -, *, / или ^2')
#
#
# num1 = float_conversion("Введите число: ")
#
# while True:
#     try:
#         operation = input("Выберите операцию (Введите +, -, *, / или ^2): ")
#         check_operation(operation)
#         break
#     except ValueError as e:
#         print(e)
#
# if operation == '^2':
#     print(calculator_power(num1))
# elif operation == '+':
#     num2 = float_conversion("Введите число: ")
#     print(calculator_main(num1, num2, lambda num1, num2: num1 + num2))
# elif operation == '-':
#     num2 = float_conversion("Введите число: ")
#     print(calculator_main(num1, num2, lambda num1, num2: num1-num2))
# elif operation == '*':
#     num2 = float_conversion("Введите число: ")
#     print(calculator_main(num1, num2, lambda num1, num2: num1*num2))
# elif operation == '/':
#     num2 = float_conversion("Введите число: ")
#     try:
#         print(calculator_main(num1, num2, lambda num1, num2: num1 / num2))
#     except ZeroDivisionError:
#         print('Ошибка деления: деление на ноль')

# task 9
# @dataclass
# class Point:
#     x: float
#     y: float
#
# p1 = Point(1, 2)
# p2 = Point(-3.5, 4.2)
#
# print(p1)
# print(p2)

# task 10
# @dataclass
# class Product:
#     name: str
#     price: float
#     quantity: int = 1
#
#     def total(self):
#         total_cost = self.price * self.quantity
#         return total_cost
#
#
# p1 = Product("Keyboard", 50.0, 2)
# p2 = Product("Mouse", 25.0)
#
# print(p1, "total:", p1.total())
# print(p2, "total:", p2.total())

# task 11
# from typing import List, Optional

# @dataclass
# class Book:
#     title: str
#     authors: List[str] = field(default_factory=list)
#     year: int | None = None
#
#     def formatted(self):
#         authors = ', '.join(self.authors) if self.authors else 'автор неизвестен'
#         year = self.year if self.year else 'год неизвестен'
#         return f'{self.title} ({year}) - {authors}'
#
# b1 = Book("Python 101", ["John Doe"], 2020)
# b2 = Book("Безымянная книга")
# b3 = Book("Совместный труд", ["Alice", "Bob"])
#
# for b in (b1, b2, b3):
#     print(b.formatted())
