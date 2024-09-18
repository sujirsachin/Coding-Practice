import math
from typing import List


def prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime", n)
            return
    print("Prime", n)


def prime2(numbers: List):
    for n in numbers:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                print("Not Prime", n)
                break
            elif i == int(math.sqrt(n)):
                print("Prime", n)


prime(13)

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
composite_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39,
                     40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72,
                     74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]
prime2(numbers)
prime2(composite_numbers)
