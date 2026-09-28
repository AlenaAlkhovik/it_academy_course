import time
import functools

# task 1

def retry(times):
    def dec(func):
        def wrapper():
            for attempt in range(1,times+1):
                result = func()
                if result == 'PASSED':
                    print(f'Успешно! попытка номер: {attempt}')
                    return result
                else:
                    print(f'Не успешно! попытка номер: {attempt}')
            if attempt == times:
                print('Попыток больше нет')
            return ""
        return wrapper
    return dec


@retry(3)
def flaky_test():
    if time.time() % 2 < 1:
        return "FAILURE"
    return "PASSED"

print(flaky_test())

# task 2
def require_role(func):
    def wrapper(*args):
        if args[0] == 'admin':
            return func(*args)
        else:
            print(f'Ошибка: Требуется роль admin, текущая: {args[0]}')
    return wrapper


@require_role
def admin_test(*args):
    print("Выполняется админский тест")
    return "Success"

admin_test(input('Введите свою роль'))

#task 3

def timer(func):
    @functools.wraps(func)
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f'{func.__name__} выполнился за {end_time-start_time:.2f} сек')
        return result
    return wrapper

@timer
def slow_test():
    time.sleep(1)
    return "OK"

print(slow_test())

# task 4
def wait_with_retry_until(timeout, interval):
    def dec(func):
        def wrapper():
            start_test = time.time()
            attempt = 1
            while time.time() - start_test < timeout:
                res = func()
                if res:
                    print('Элемент найден')
                    return res
                else:
                    print(f'Попытка {attempt}: неуспешно')
                    time.sleep(interval)
                    attempt += 1
            else:
                print('Элемент не найден. Таймаут вышел')
            return res
        return wrapper
    return dec

@wait_with_retry_until(timeout=3, interval=0.5)
def element_visible():
    return time.time() % 3 > 2  # имитация появления элемента

element_visible()

# task 5
def cache_results(func):
    my_dict = {}
    @functools.wraps(func)
    def wrapper(n):
        if n in my_dict:
            return my_dict[n]
        res = func(n)
        my_dict[n] = res
        return res
    return wrapper

def count_exec_time(func):
    @functools.wraps(func)
    def wrapper(n):
        print(f"Выполняю {func.__name__} с аргументом {n}")
        start_time = time.time()
        res = func(n)
        print(res)
        end_time = time.time()
        func_duration = end_time - start_time
        return func_duration
    return wrapper

@count_exec_time
@cache_results
def expensive_calculation(n):
    print(f"Вычисляем для {n}")
    time.sleep(1)
    return n * n

print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(6))
print(expensive_calculation(6))

# task 6
def validate_params(func):
    def wrapper(**kwargs):
        errors = []
        if not isinstance(kwargs.get('age'), int):
            errors.append('age должен быть int')
        if not isinstance(kwargs.get('username'), str):
            errors.append('username должен быть str')

        if errors:
            return ', '.join(errors)
        return func(**kwargs)
    return wrapper


@validate_params
def create_user(**kwargs):
    return f"Пользователь {kwargs['username']} создан"

print(create_user(username="test", age=25))
print(create_user(username="test2", age='25'))
print(create_user(username=True, age='25'))
print(create_user(username=True, age=25))

# task 7
LOG_LEVEL = "ERROR"

levels = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50,
}

def conditional_log(min_level):
    def decor(func):
        @functools.wraps(func)
        def wrapper():
            result = func()
            if levels[min_level] >= levels[LOG_LEVEL]:
                print(f'функция {func.__name__} вернула {result}')
            return result
        return wrapper
    return decor


@conditional_log("WARNING")
def debug_test():
    return "debug_result"

@conditional_log("ERROR")
def error_test():
    return "error_result"

debug_test()
error_test()