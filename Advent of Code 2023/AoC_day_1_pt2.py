def mapLettersToNumbers(data):
    letters_to_number ={"one": 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "zero": 0,
                        "eleven": 11,
                        "twelve": 12,
                        "thirteen": 13,
                        "fourteen": 14,
                        "fifteen": 15,
                        "sixteen": 16,
                        "seventeen":17,
                        "eighteen": 18,
                        "nineteen": 19}
    list = ["one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "zero", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]
    #for string in data:
       # for number in list:
           # if number in string:

def convert(data):
    final_string = []
    number = ""
    letters_to_number = {"one": 1,
                         "two": 2,
                         "three": 3,
                         "four": 4,
                         "five": 5,
                         "six": 6,
                         "seven": 7,
                         "eight": 8,
                         "nine": 9,
                         "zero": 0,
                         "eleven": 11,
                         "twelve": 12,
                         "thirteen": 13,
                         "fourteen": 14,
                         "fifteen": 15,
                         "sixteen": 16,
                         "seventeen": 17,
                         "eighteen": 18,
                         "nineteen": 19}
    list = ["one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "zero", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]
    data = ["sachin"]
    for string in data:
        for char in string:
            if char.isdigit():
                number =""
                final_string.append(char)
            elif number+char in list:
                number += char
                final_string.append(letters_to_number[number])
                if len(number) >5:
                    number = number[1:]





data = []
with open("day1Input3.txt", "r") as f:
    data = f.readlines()

data = [line.replace("\n", "") for line in data]
print(data)
print()