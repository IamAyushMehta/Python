import math


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def add(*numbers):
    sum(numbers)


def subtract(*numbers):
    res = numbers[0]
    for i in range(1, len(numbers)):
        res -= numbers[i]
    return res


def square(x):
    return x**2


def cube(x):
    return x**3

