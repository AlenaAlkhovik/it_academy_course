# task #1
number = int(input('Введите число'))

if number > 0:
     print('число положительное')
elif number == 0:
     print('число = 0')
else:
    print('число отрицатеьное')


# task #2
test_info = input('Введите строку')

if test_info.endswith("test"):
    print('заканчивается на test')
else:
    print('не заканчивается на test')


# task #3
age = int(input('Введите ваш возраст'))

if age >=18:
     print('Доступ разрешен')
else: print('Доступ запрещен')

# task #4
test_info = input('Введите строку')

if test_info == (''):
    print('вы ввели пустую строку')

# task 5
Password = 'Puppy'
user_password = input('Введите пароль')

if user_password == Password:
    print('Success')
else:
    print('Fail')


# task #6
test_info = input('Введите строку')

if 'error' in test_info:
    print('Ошибка найдена')


# task #7
num = int(input('Введите число'))

if num == 0:
    print('число = 0')
elif num % 2 == 0:
    print('число четное')
else:
    print('число нечетное')


# task #8
text = input('Введите строку')

if text.istitle():
    print('Верно')
else:
    print('Неверно')

# task #9

text_length = input('Введите строку')

if len(text_length) >10:
    print('Строка длинная')
else:
    print('Строка короткая')


# task #10
letter = input('Введите букву')

match letter:
     case 'a'| 'e'| 'i'| 'o'| 'u'| 'A'| 'E'| 'I'| 'O'| 'U':
          print('буква гласная')
     case _:
         print('буква согласная')

#task #11
name = input('Введите имя')

if name == 'Иван':
    print('Привет, студент')


#task #12

name = input('Введите имя')
surname = input('Введите фамилию')

if name == surname:
    print("Имя и вамиля одинаковые")
else:
    print('Имя и фамилия - разные')


#task #13
num = int(input("Введите число"))

if num >= 1 and num <= 100:
    print ("Число в диапазоне")
else:
    print("Число вне диапазона")


#task #14
text = input('Введите строку')

if text.isdigit():
    print("Строка состоит полностью из цифр")
else:
    print('В строке содержатся другие символы, кроме цифр')


#task #15
text = input("Введите строку")

if text.endswith("a"):
    print("Строка заканчивается на а")
else:
    print("Строка не заканчивается на а")
