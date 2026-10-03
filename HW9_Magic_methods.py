# task 1

class TestCase:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f'name = {self.name}, status = {self.status}'

    def __repr__(self):
        return f'TestCase(name = {self.name!r}, status = {self.status!r})'

t = TestCase("test_login", "passed")
print(t)
print([t])

# task 2

# class TestSuite:
#     def __init__(self, tests):
#         self.tests = tests
#
#     def __len__(self):
#         return len(self.tests)
#
#     def __bool__(self):
#         return len(self.tests) > 0
#
#
# suite = TestSuite(["test_login", "test_signup"])
# print(len(suite))
# if suite:
#     print("Suite не пустой")

# task 3

# class Results:
#     def __init__(self):
#         self._data = {}
#
#     def __setitem__(self, test_name, status):
#         self._data[test_name] = status
#
#     def __getitem__(self, test_name):
#         return self._data[test_name]
#
# results = Results()
#
# results["test_login"] = "passed"
# print(results["test_login"])

#task 4

# class TestSuite:
#     def __init__(self, tests):
#         self.tests = tests
#
#     def __iter__(self):
#         return iter(self.tests)
#
# suite = TestSuite(["test_login", "test_signup"])
# for test in suite:
#     print(test)

#task 5

# class Duration:
#     def __init__(self, seconds):
#         self.seconds = seconds
#
#     def __add__(self, other):
#         return Duration(self.seconds + other.seconds)
#
#     def __str__(self):
#         return f'{self.seconds} sec'
#
# t1 = Duration(1.5)
# t2 = Duration(2.3)
# print(t1 + t2)

#task 6

# class TestRunner:
#     def __init__(self, tests):
#         self.tests = tests
#
#     def __call__(self):
#         for i in self.tests:
#             print(i)
#
# runner = TestRunner(["test_login", "test_signup"])
# runner()

# task 7

# class Version:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __lt__(self, other):
#         return (self.a, self.b) < (other.a, other.b)
#
#     def __eq__(self, other):
#         return (self.a, self.b) == (other.a, other.b)
#
#
# v1 = Version(1, 2)
# v2 = Version(1, 3)
# print(v1 < v2)
# print(v1 == v2)

