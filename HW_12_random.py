import random

# task 1
x = random.randint(1, 6)
print(x)

# task 2
my_string = 'abcdefghijklmnopqrstuvwxyz'
a = random.choices(my_string, k=8)
b = "".join(a)
print(b)

# task 3
http = ["GET", "POST", "PUT", "DELETE"]

def http_choice(method):
    q = random.choice(method)
    return q

m = http_choice(http)
print(m)

# task 4
tests = ["test_login", "test_logout", "test_add_to_cart", "test_checkout"]
random.shuffle(tests)
print(tests)

# task 5
users = ["alice", "bob", "carol", "dave", "erin"]
d = random.sample(users, k=2)
print(d)

# task 6
def run_flaky_test():
    w = random.random()
    if w < 0.3:
        return 'FAILED'
    else:
        return 'PASSED'

print(run_flaky_test())

# task 7
# option 1

lottery_ticket = random.sample(range(1, 50), k=6)
print(lottery_ticket)

# option 2
lottery_ticket = []

while len(lottery_ticket) < 6:
    number_candidate = random.randint(1,49)
    if number_candidate not in lottery_ticket:
        lottery_ticket.append(number_candidate)

print(lottery_ticket)

# task 8
def generate_test_data(n):
    test_suite = []
    for i in range(1, n+1):
        test_suite.append(random.randint(0,100))
    return test_suite

print(generate_test_data(5))
