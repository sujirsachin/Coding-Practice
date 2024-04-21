import math


def countDigits(n: int) -> int:
    count = 0
    while (n > 0):
        n = n // 10
        count += 1
    return count

def countDigits2(n: int) -> int:
    return int(math.log10(n)+1)


print(countDigits2(2222))
