import os
import shutil
from contextlib import contextmanager

# # task 1
with open('hello.txt', 'w') as h:
    h.write('Hello, file!')

with open('hello.txt', 'r') as h:
    hello = h.read()
    print(hello)
#
# # task 2
# lines = ['text\n', '1\n', '2\n', '3\n', '4\n', '5\n']
# with open('numbers.txt', 'w') as n:
#     n.writelines(lines)
#
# with open('numbers.txt', 'r') as n:
#     numbers = n.read()
#     print(numbers)
#
# # task 3
# def count_lines(path):
#     with open(path, 'r') as c:
#         c_lines = c.readlines()
#         return len(c_lines)
#
# print(count_lines('numbers.txt'))
#
# # task 4
# with open('source.txt', 'r') as so, open('copy.txt', 'w') as co:
#     for line in so:
#         co.write(line)
#
# # task 5
# def log_message(path, message):
#     with open(path, 'a', encoding='utf-8') as p:
#         p.write(message+'\n')
#
# log_message("app.log", "Test started")
# log_message("app.log", "Test finished")

# # task 6
# def read_first_chars(path, n):
#     with open(path, 'r', encoding='utf-8') as p:
#         chars = p.read(n)
#     return chars
#
# print(read_first_chars('app.log', 20))

# # task 7
# def filter_file(src, dst, keyword):
#     with open(src, 'r', encoding='utf-8') as s, open(dst, 'w', encoding='utf-8') as d:
#         for line in s:
#             if keyword in line:
#                 d.write(line)
#
#
# filter_file("app.log", "errors.log", "ERROR")

# # task 8
# def sum_file(path):
#     total = 0
#     with open(path, 'r', encoding='utf-8') as p:
#         for line in p:
#             try:
#                 number = int(line)
#                 total += number
#             except ValueError as v:
#                 print(v)
#     return total
#
# print(sum_file('numbers.txt'))
# print(sum_file('copy.txt'))

# # task 9
# def copy_binary(src, dst):
#     with open(src, 'rb') as s, open(dst, 'wb') as d:
#         data = s.read()
#         d.write(data)
#
# copy_binary("image.png", "image_copy.png")

# # task 10
# def read_config(path):
#     config = {}
#     with open(path, 'r', encoding='utf-8') as p:
#         for line in p:
#             line = line.strip()
#             if line and not line.startswith('#'):
#                 key, value = line.split('=')
#                 config[key] = value
#     return config
#
# print(read_config("config.txt"))

# # Task 2 - Временный файл
# # with class
# class TempFile:
#     def __enter__(self):
#         self.f = open('temp.txt', 'w', encoding='utf-8')
#         return self.f
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.f.close()
#         os.remove('temp.txt')
#         return False
#
# # with TempFile() as f:
#     f.write('временные данные')
#     print(os.path.exists('temp.txt'))
#
# print(os.path.exists('temp.txt'))

# with @contextmanager
# @contextmanager
# def temp_file():
#     f = open('temp.txt', 'w', encoding='utf-8')
#     try:
#         yield f
#     finally:
#         f.close()
#         os.remove('temp.txt')
#
# with temp_file() as f:
#     f.write('временные данные')
#     print(os.path.exists('temp.txt'))
#
# print(os.path.exists('temp.txt'))