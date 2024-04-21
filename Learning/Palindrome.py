def palindrome(n: int) -> int:
    reversedNumber = 0
    number = n
    while number > 0:
        lastDigit = number % 10
        number = number // 10
        reversedNumber = (reversedNumber * 10) + lastDigit
    return reversedNumber == n


print(palindrome(1001))
