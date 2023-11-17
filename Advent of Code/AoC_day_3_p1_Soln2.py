def calculate_priority(item_type):
    if 'a' <= item_type <= 'z':
        return ord(item_type) - ord('a') + 1
    elif 'A' <= item_type <= 'Z':
        return ord(item_type) - ord('A') + 27
    else:
        return 0

def find_sum_of_priorities(rucksack_contents):
    first_compartment = rucksack_contents[:len(rucksack_contents)//2]
    second_compartment = rucksack_contents[len(rucksack_contents)//2:]

    common_items = set(first_compartment) & set(second_compartment)

    priority_sum = sum(calculate_priority(item) for item in common_items)

    return priority_sum

def main():
    rucksack_contents_list = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
    with open("day3Input1.txt", "r") as f:
        read_data = f.readlines()

    total_priority_sum = sum(find_sum_of_priorities(contents) for contents in read_data)

    print("The sum of priorities is:", total_priority_sum)

if __name__ == "__main__":
    main()