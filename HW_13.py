# task 1
def even_numbers(iterable):
    for item in iterable:
        if item % 2 ==0:
            yield item

print(list(even_numbers([1, 2, 3, 4, 5, 6])))

# task 2
# def read_lines(path):
#     with open(path, 'r', encoding='utf-8') as p:
#         for line in p:
#             yield line
#
# def filter_lines(path, keyword):
#     for line in read_lines(path):
#         if keyword in line:
#             yield line
#
# for line in filter_lines("log.txt", "ERROR"):
#     print(line)

# task 3
# def chain(iter1, iter2):
#     for x in iter1:
#         yield x
#     for i in iter2:
#         yield i
#
# print(list(chain([1, 2], [3, 4])))


# task 4
# def counter(start=0):
#     while True:
#         yield start
#         start+=1
#
# c = counter(10)
# print(next(c))
# print(next(c))
# print(next(c))

# task 5
# Option 1
# def take(n, iterable):
#     for i in range(n):
#         number = next(iterable)
#         yield number

# Option 2
# def take(n, iterable):
#     count = 0
#     for x in iterable:
#         yield x
#         count += 1
#         if count == n:
#             break

# Option 3
# def take(n, iterable):
#     count = 0
#     for x in iterable:
#         if count == n:
#             break
#         yield x
#         count +=1
#
# c = counter(100)
# print(list(take(5, c)))


import re
from tokenize import group

# task 6
# text = "one two three\tfour"
# res = re.sub(r'\s+', ',', text)
#
# print(res)

# task 7

# emails = ["a@test.com", "b@mail.ru", "user@sub.example.org"]
# domains = []
# for i in emails:
#     j = re.search(r'@(\w+(?:\.\w+)+)', i)
#     do = j.group(1)
#     domains.append(do)
#
# print(domains)

#task 8

# def is_valid_date(date):
#     pattern = r'\d{4}-\d{2}-\d{2}'
#     if re.fullmatch(pattern, date):
#         return True
#     else:
#         return False
#
# print(is_valid_date("2025-12-23"))
# print(is_valid_date("25-12-23"))

# task 9
# log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
#
# response_code = re.search(r'(\S\s)(\d{3})', log)
#
# print(response_code.group(2))

# task 10

# def is_strong_password(password):
#     if len(password) >=8:
#         if re.search(r'[A-Z]', password):
#
#             if re.search(r'\d', password):
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False
#
# print(is_strong_password("Abcdef12"))
# print(is_strong_password("abcdef12"))
# print(is_strong_password("Abcdefgh"))

# task 11

# hi = "<p>Hello <b>world</b>!</p>"
#
# hi_with_del_tags = re.sub(r'<[^>]*>', '', hi)
# print(hi_with_del_tags)

# task 12

# s = "name=John; age=30; city=London;"
#
# s_without_semicolon = re.sub(';', '', s)
#
# s_list = re.split(' ', s_without_semicolon)
#
# result = {}
# for item in s_list:
#     j = re.split('=', item)
#     result.update({j[0]: j[1]})
#
# print(result)

# task 13
# text = "Мой телефон: +7-999-123-45-67, офис: 8 (812) 555-66-77."
#
# def find_phones(t):
#     phones = re.findall(r'\+\d-\d{3}-\d{3}-\d{2}-\d{2}|\d\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}', t)
#     return phones
#
# print(find_phones(text))

# task 14
# text = "one,two;three four"
#
# result = re.split(r'[,;\s]+', text)
# print(result)

# task 15

# url = '/api/v1/users/123/orders/456'
#
# user_id = re.search(r'users/(\d+)', url)
# user_id = int(user_id.group(1))
#
# order_id = re.search(r'orders/(\d+)', url)
# order_id = int(order_id.group(1))
#
# print((user_id, order_id))