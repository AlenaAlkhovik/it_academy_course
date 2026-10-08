# task 1
# class Vehicle:
#     def __init__(self, speed):
#         self.speed = speed
#
#     def move(self):
#         print(f'Двигаюсь со скоростью {self.speed}')
#
# class Car(Vehicle):
#     def __init__(self, speed, honk_type = 'beep-beep'):
#         Vehicle.__init__(self, speed)
#         self.honk_type = honk_type
#
#     def honk(self):
#         print(self.honk_type)
#
# car = Car(100)
# car.move()
# car.honk()

# task 2
# class Employee:
#     def __init__(self, name):
#         self.name = name
#         self.salary = ''
#
# class Manager(Employee):
#     def __init__(self, name, salary = 80000):
#         self.name = name
#         self.salary = salary
#
# class Developer(Employee):
#     def __init__(self, name, salary = 70000):
#         self.name = name
#         self.salary = salary
#
# ivan = Manager("Иван")
# petya = Developer("Петр")
# print(ivan.salary)
# print(petya.salary)

#task 3
# class Shape:
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         s = self.length * self.width
#         return s
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         s = 3.14*(self.radius**2)
#         return s
#
# rect = Rectangle(5, 3)
# cir = Circle(10)
# print(rect.area())
# print(cir.area())

#task 4
# class Account:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self, dep):
#         with_added_deposit = self.balance + dep
#         self.balance = with_added_deposit
#         return self.balance
#
#     def withdraw(self, wit):
#         without_withdraw = self.balance - wit
#         self.balance = without_withdraw
#         return self.balance
#
#
# class SavingsAccount(Account):
#     def __init__(self, balance, percent):
#         Account.__init__(self, balance)
#         self.percent = percent
#
#     def add_interest(self):
#         with_added_percent = self.balance + (self.balance * self.percent)/100
#         self.balance = with_added_percent
#         return self.balance
# 
# account = SavingsAccount(5000, 15)
# account.deposit(1000)
# account.withdraw(20)
# print(account.add_interest())