#task #1
# решение#1
fullname = input("Введите ФИО полностью")
parts = fullname.split()
last_name = parts[0]
first_name = parts[1]
surname = parts[2]
name_output = first_name[0]+'.'
surname_output = surname[0]+'.'
print(last_name, name_output, surname_output)

# решение#2
fullname = input("Введите ФИО полностью")
last_name, first_name, patronymic = fullname.split()
print(f"{last_name} {first_name[0]}. {patronymic[0]}.")

#task #2
words = input("Введите строку в несколько слов")
list_words = words.split()
print(len(list_words))

#task #3
text = input("Введите строку")
print(text[::-1])

#task #4
text = input("Введите строку")
my_list = text.split()
text_without_spaces = ''.join(my_list)
print(text_without_spaces)

#task #5
text_1 = input("Введите первую строку")
text_2 = input("Введите вторую строку")
if text_2 in text_1:
    print("Строка найдена - True")
else:
    print("Строка не найдена - False")

#task #6
text = input("Введите строку")
symbol_search = input("Введите символ для поиска")
symbol_exchange= input("Введите символ для замены")

text_2 = text.replace(symbol_search, symbol_exchange)
print(text_2)

#task #7
text = input("Введите строку")
if text.isdigit():
    print("Строка является числом - True")
else:
    print("Строка является числом - False")