import re


def calibrate(data):
    total = 0
    for string in data:
        digits = [int(char) for char in string if char.isdigit()]
        print(digits)
        if len(digits) == 1:
            number = str(digits[0]) + str(digits[0])
            total += int(number)
        else:
            number = str(digits[0]) + str(digits[-1])
            total += int(number)
    print(total)

with open("day1Input2.txt", "r") as f:
    data = f.readlines()

data = [line.replace("\n", "") for line in data]
print(data)
calibrate(data)
