import string


def palindrome(n: int) -> int:
    reversedNumber = 0
    number = n
    while number > 0:
        lastDigit = number % 10
        number = number // 10
        reversedNumber = (reversedNumber * 10) + lastDigit
    return reversedNumber == n


def palindrome_string(word: string) -> string:
    left = 0
    right = len(word) - 1
    while left <= right:
        if word[left] != word[right]:
            return "Not a Palindrome"
        left += 1
        right -= 1
    return "Palindrome"


print(palindrome_string("madam"))      # Palindrome
print(palindrome_string("hello"))      # Not a Palindrome
print(palindrome_string("Able was I ere I saw Elba"))
print(palindrome_string("able was I ere I saw elba")) # Palindrome

print(palindrome(1001))
