import math


def gdc(n1: int, n2: int):
    factors = []
    if n1 > n2:
        for i in range(1, n1 + 1):
            if n1 % i == 0:
                factors.append(i)
        for i in reversed(range(1, n2 + 1)):
            if n2 % i == 0 and i in factors:
                print(i)
                return
    else:
        for i in range(1, n2 + 1):
            if n2 % i == 0:
                factors.append(i)
        for i in reversed((range(1, n1 + 1))):
            if n1 % i == 0 and i in factors:
                print(i)
                return
    return -1


def hcf(n1: int, n2: int):
    for i in reversed(range(1, min(n1, n2) + 1)):
        if n1 % i == 0 and n2 % i == 0:
            print(i)
            return
    return -1


def euclidean(n1: int, n2: int):
    number1 = n1
    number2 = n2
    temp = 0
    while number1 and number2 > -1:
        if number1 > number2:
            temp = number2
            number2 = number1 - number2
            number1 = temp
        else:
            temp = number1
            number1 = number2 - number1
            number2 = temp
    print(max(number1, number2))


def euclidean2(n1: int, n2: int):
    number1 = n1
    number2 = n2

    while number1 and number2 > 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    print(max(number1, number2))


gdc(99, 66)
hcf(9, 12)
euclidean(20, 15)
euclidean2(20, 15)
