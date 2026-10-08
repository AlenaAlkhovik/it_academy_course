# task 1.1

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print('Отрицательную цену задать нельзя')
        else:
            self._price = value

p = Product(100)
print(p.price)
p.price = 250
print(p.price)
p.price = -10
print(p.price)

#task 1.2
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# rect = Rectangle(3, 4)
# print(rect.area)
# rect.width = 10
# print(rect.area)

#task 1.3
# class TestStats:
#     def __init__(self, passed, total):
#         self.passed = passed
#         self.total = total
#
#     @property
#     def success_rate(self):
#         return (self.passed*100)/self.total
#
#
# stats = TestStats(8, 10)
# print(stats.success_rate)
# stats.passed = 9
# print(stats.success_rate)
#
# stats2 = TestStats(5, 12)
# print(stats2.success_rate)

# task 2.1
# class PermissionMixin:
#     def has_permission(self, user_role):
#         return user_role == 'admin'
#
# class SecureAction(PermissionMixin):
#     def execute(self, role):
#         a = self.has_permission(role)
#         if a:
#             print('Админ. Метод запущен')
#         else:
#             print('Нет прав.')
#
# action = SecureAction()
# action.execute("user")
# action.execute("admin")

# task 2.2
# class Logger:
#     def log(self, message):
#         print(f'[Log] {message}.')
#
# class Service:
#     def __init__(self):
#         self.logger= Logger()
#
#     def process(self):
#         self.logger.log('Начало обработки')
#         print('Обработка данных')
#         self.logger.log('Конец обработки')
#
# s = Service()
# s.process()

#task 2.3
# class Admin:
#     def create_user(self, name):
#         print(f'User "{name}" is created')
#
# class Support:
#     def create_ticket(self, ticket_name):
#         print(f'Ticket "{ticket_name}" is created')
#
# class SuperUser(Admin, Support):
#     pass
#
# su = SuperUser()
# su.create_user("Ivan")
# su.create_ticket("Падает сервис")

# task 2.4
# class A:
#     def who_am_i(self):
#         print('A')
#
# class B(A):
#     def who_am_i(self):
#         print('B')
#
# class C(A):
#     def who_am_i(self):
#         print('C')
#
# class D(B, C):
#     pass
#
# d = D()
# d.who_am_i()
# print(D.mro())
# print(D.__mro__)

# task 2.5
# class LoggingMixin:
#     def log(self, message):
#         print(f'[LOG] {message}')
#
# class RetryMixin:
#     def retry(self, number_of_runs):
#         if number_of_runs >= 3:
#             i = [1, 2, 3]
#             for x in i:
#                 print(f'Попытка {x}')
#                 self.run()
#         elif number_of_runs == 2:
#             i = [1, 2]
#             for x in i:
#                 print(f'Попытка {x}')
#                 self.run()
#         elif number_of_runs == 1:
#             print(f'Попытка {number_of_runs}')
#             self.run()
#         else:
#             print('Некорректное число попыток')
#
# class Job(LoggingMixin, RetryMixin):
#     def run(self):
#         self.log('Выполняем задачу')
#         print('Job что-то делает...')
#
# j = Job()
# j.retry(2)

# task 3.1
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return f'Прямоугольник. Площадь: {self.length * self.width}'
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return f'Круг. Площадь: {math.pi*(self.radius**2):.2f}'
#
# shapes = [Rectangle(3, 4), Circle(2)]
# for s in shapes:
#     print(s.area())

# task 3.2
# from abc import ABC, abstractmethod
#
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
#     def go(self):
#         print('Начинаем движение')
#         self.move()
#
# class Car(Transport):
#     def move(self):
#         print('Едем по дороге на машине')
#
# class Bike(Transport):
#     def move(self):
#         print('Едем на велосипеде')
#
# for t in (Car(), Bike()):
#     t.go()

# task 3.3
# from abc import ABC, abstractmethod
#
# class BaseTestCase(ABC):
#     @abstractmethod
#     def prepare_data(self):
#         pass
#
#     @abstractmethod
#     def run_test(self):
#         pass
#
#     def run(self):
#         print(f'=={type(self).__name__}==')
#         self.prepare_data()
#         self.run_test()
#
# class LoginTest(BaseTestCase):
#     def prepare_data(self):
#         print('Готовим пользователя для логина')
#
#     def run_test(self):
#         print('Проверяем успешный логин')
#
# class PaymentTest(BaseTestCase):
#     def prepare_data(self):
#         print('Готовим данные карты и баланс')
#
#     def run_test(self):
#         print('Проверяем успешный платеж')
#
#
# tests = [LoginTest(), PaymentTest()]
# for t in tests:
#     t.run()

# task 4.1
# from abc import ABC, abstractmethod
#
# class BaseTest(ABC):
#     @abstractmethod
#     def run(self):
#         pass
#
# class APITest(BaseTest):
#     def __init__(self, message):
#         self.message = message
#
#     def run(self):
#         print(f'API тест: проверяем эндпоинт {self.message}')
#
# class UITest(BaseTest):
#     def __init__(self, message):
#         self.message = message
#
#     def run(self):
#         print(f'UI тест: проверяем страницу {self.message}')
#
# def run_all(tests):
#     for i in tests:
#         i.run()
#
# tests = [
#     APITest("/login"),
#     UITest("LoginPage"),
#     APITest("/users"),
# ]
# run_all(tests)

# task 4.2
# class TestCollection:
#     def __init__(self, collection):
#         self.collection = collection
#
#     def __len__(self):
#         return len(self.collection)
#
# def print_length(obj):
#     print(len(obj))
#
#
# print_length("Python")
# print_length([1, 2, 3])
# print_length({"a": 1, "b": 2})
# print_length(TestCollection([10, 20, 30, 40]))
