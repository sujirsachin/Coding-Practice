def reverseNumber(n: int) -> int:
    reversedNumber = 0
    number = n
    while (number > 0):
        lastDigit = n % 10
        number = number // 10
        reversedNumber = (reversedNumber * 10) + lastDigit
    return int(reversedNumber)


print(reverseNumber(1002))
