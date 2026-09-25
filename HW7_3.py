# test 3.1
def apply_test_check(check_func, test_results):
    passed_count = 0
    for i in test_results:
        if check_func(i):
            passed_count += 1
    return passed_count

test_results = [
    {"status": "passed"}, {"status": "failed"}, {"status": "passed"}
]

result = apply_test_check(lambda x: x["status"] == "passed", test_results)
print(f"Прошло тестов: {result}")

# test 3.2
def filter_logs(any_name, filter_func):
    return [i for i in any_name if filter_func(i)]

logs = [
    {"level": "INFO", "message": "Test started"},
    {"level": "ERROR", "message": "Login failed"},
    {"level": "WARNING", "message": "Timeout occurred"}
]

error_logs = filter_logs(logs, lambda x: x["level"] == "ERROR")
print("Ошибки:", error_logs)

# решмла использовать эту же функцию с другими логами и лямбдой

logs = [
    {"level": "INFO", "message": "Test started"},
    {"level": "ERROR_1", "message": "Login failed"},
    {"level": "WARNING", "message": "Timeout occurred"},
    {"level": "INFO", "message": "Test started"},
    {"level": "ERROR_2", "message": "Login failed"},
    {"level": "WARNING", "message": "Timeout occurred"}
]

error_logs = filter_logs(logs, lambda x: x["message"] == "Login failed")
print("Ошибки:", error_logs)

# test 3.2
def transform_tests(tests, transform_func):
    return [transform_func(test) for test in tests]

tests = [{"name": "test1", "duration": 2.0}, {"name": "test2", "duration": 3.0}]
increased_tests = transform_tests(tests, lambda t: {**t, "duration": t["duration"] * 1.1})
print("Тесты с увеличенным временем:", increased_tests)




