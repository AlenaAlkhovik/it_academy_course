def generate_report (title, *args, format='PDF', **kwargs):
    print(f'Отчет: {title}')
    print(f'Формат: {format}')
    print("Тесты:")
    for i in args:
        print(i)
    for i, j in kwargs.items():
        print(f'{i}: {j}')

title = input('Input report tile')
tests = input('Input test titles separated by 1 comma and 1 space')
tests_list = tests.split(', ')
format = input('Input format')
other_params = {}
while True:
    key = input("Введите ключ (или пустую строку для завершения): ")
    if key == "":
        break
    value = input(f"Введите значение для '{key}': ")
    other_params[key] = value

generate_report(title, tests_list, format=format, **other_params)