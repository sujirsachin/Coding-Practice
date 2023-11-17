import string


def findItems(data):
    error_list = []
    for container in data:
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


def get_priority_and_sum(data) -> int:
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 27
    sum = 0
    for character in data:
        sum += values[character]
    return sum


def find_common_items(data):
    i = 1
    error_list = []
    for container in data:
        container = container.replace("\n","")
        if i == 3:
            third_compartment = container
            temp_list = list(set(first_compartment) & set(second_compartment) & set(third_compartment))
            if temp_list:
                error_list.append(temp_list[0])
            i = 1
        elif i == 2:
            second_compartment = container
            i += 1
        else:
            first_compartment = container
            i += 1
    return get_priority_and_sum(error_list)


data2 = ["vJrwpWtwJgWrhcsFMMfFFhFp",
         "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
         "PmmdzqPrVvPwwTWBwg",
         "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
         "ttgJtRGJQctTZtZT",
         "CrZsJsPPZsGzwwsLwLmpwMDw"]

with open("day3Input1.txt", "r") as f:
    data = f.readlines()

print(find_common_items(data))
