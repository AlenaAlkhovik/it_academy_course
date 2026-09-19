# task 1
x = input("Введите строку")

for i in x:
    print(i)


# task 2
x = input("Введите строку")
count = 0

for i in x:
    if i  in 'aeiouAEIOU':
        count +=1
print(count)

#task 3
x = input("Введите несколько названий (через пробел)")

for i in x.split():
    print("Test Case " + i)

#task 4
password = 'admin'
user_password = input("Введите пароль")

while password != user_password:
    user_password = input("Введите пароль еще раз")
else:
    print("Пароль верный")


# task 5
for i in range (1,11):
    if i % 3 == 0:
        continue
    print(i)

#task 6
count = 0

for i in range(1,101):
    count +=i
print(count)

#task 7
browsers = ['Chrome', 'Firefox']
os = ["Windows", "Linux"]

for i in browsers:
    for o in os:
        print(i +'-'+ o)


#task 8
symbols = input("Введите строку")

for i, symbols in enumerate(symbols):
    print (i, symbols)

# task 9
email = input("Введите email")

for i in email:
    if i == '@':
        print("есть @")
        break
else:
    print("нет @")

#task 10
i=10
print(i)
while i >0:
    i -= 1
    print(i)

#task 11
x = input("Введите строку")

for i in x:
    i = i.upper()
    print(i, end="")

#task 12
x = int(input("Введите число"))

while x <=10:
    x = int(input("Введите число"))

#task 13
text = input("Введите строку в несколько слов (разделенных пробелами)")
words = text.split()
count = 0

for i in words:
    count += 1
print(count)


#task 14
for i in range(1,21):
    if i >15 :
        break
    print(i)

