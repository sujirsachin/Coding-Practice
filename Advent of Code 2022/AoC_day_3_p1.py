import string

print("Advent of Code 2022, Link to Problem: {}".format('https://adventofcode.com/2022/day/3'))


def findItems(data):
    error_list = []
    for container in data:
        container = container.replace("\n", "")
        first_compartment = container[:len(container) // 2]
        second_compartment = container[len(container) // 2:]
        temp_list = list(set(first_compartment) & set(second_compartment))
        if temp_list:
            error_list.append(temp_list[0])
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 27
    sum = 0
    for character in error_list:
        sum += values[character]
    return sum


data2 = ["vJrwpWtwJgWrhcsFMMfFFhFp",
         "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
         "PmmdzqPrVvPwwTWBwg",
         "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
         "ttgJtRGJQctTZtZT",
         "CrZsJsPPZsGzwwsLwLmpwMDw"]

with open("day3Input1.txt", "r") as f:
    read_data = f.readlines()
print(findItems(read_data))
