def armstrongNumber(n: int) -> bool:
    armstrongNumber = 0
    number = n
    order = len(str(n))
    while number > 0:
        lastDigit = number % 10
        armstrongNumber += lastDigit ** order
        number //= 10
    return armstrongNumber == n

print(armstrongNumber(1634))