import math

# task 1
radius = 7

s = math.pi*(math.pow(radius, 2))

print(s)

# task 2
print(math.floor(9.8))

# task 3
in_radians = math.radians(45)
print(math.sin(in_radians))

# task 4
print(math.sqrt(144))

# task 5
print(math.gcd(270, 192))

# task 6
print(math.exp(3))

# task 7
print(math.factorial(8))

# task 8
print(math.log(256, 2))

# task 9
print(math.ceil(3.14159))

# task 10
def tn (x):
    a = math.radians(x)
    return math.tan(a)

x = float(input('Введите угол в градусах: '))
print(tn(x))