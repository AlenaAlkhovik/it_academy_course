# task 2.1
test_results = [
    {"name": "login_test", "status": "passed", "duration": 2.1},
    {"name": "payment_test", "status": "failed", "duration": 3.5},
    {"name": "logout_test", "status": "passed", "duration": 1.2}
]
success_tests = filter(lambda x: x["status"] == "passed", test_results)
print([x["name"] for x in success_tests])

#task 2.2
tests = [
    {"name": "complex_test", "duration": 5.2},
    {"name": "simple_test", "duration": 1.1},
    {"name": "medium_test", "duration": 3.4}
]
sorted_tests = lambda x: sorted(x, key=lambda t:t["duration"])

print([sorted_tests(tests)])

#task 2.3
emails = ["test@gmail.com", "invalid-email", "user@company.ru", "no@domain"]

valid_emails = filter(lambda x: "@" in x and (x.endswith(".com") or x.endswith(".ru")),emails)

print(list(valid_emails))