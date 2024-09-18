import math


def divisors(n: int):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


def divisors2(n: int):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if n // i != i:
                print(i, " ", n // i)
            else:
                print(i)


divisors2(36)
