import math


def prime(n):
    for i in range(int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
