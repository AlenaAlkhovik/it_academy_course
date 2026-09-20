# task # 1
user_name = input("Введите свое имя")
print(type(user_name))

# task # 2
num = input("Введите целое число")
result = int(num)
print(result)
print(type(result))

# task # 3
num = input("Введите число с точкой")
result = float(num)
print(result)
print(type(result))

# task # 4
num_1 = int(input('Введите первое число'))
num_2 = int(input('Введите второе число'))
summa = num_1 + num_2
print(summa)

# task # 5
user_input = input('введите строку из нескольких слов, разделённых пробелами')
my_list = user_input.split(' ')
print(my_list)
print(type(my_list))

# task # 6
text = input('Введите любую строку')
print(len(text))

# task # 7
text = input('Введите что-нибудь')
result = bool(text)
print(result)

# task # 8
text = input('Введите любую строку')
text_2 = input('Введите вторую любую строку')

result = text + text_2
print(result)

# task # 9
text = list(input('Введите любую строку'))
my_index = int(input('Введите число(индекс)'))
print(text[my_index])

# task # 10
text = input('Введите строку')
if text.isdigit():
     print("True")
else:
    print("False")

