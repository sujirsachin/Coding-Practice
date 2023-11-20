print("Advent of Code 2022, Link to Problem: {}".format('https://adventofcode.com/2022/day/4'))

def find_count_of_duplicates(assignment_pairs) -> int:
    count = 0
    j = 0
    for pair in assignment_pairs:
        sections = [list(map(int, section.split('-'))) for section in pair.split(',')]
        if is_subset_section(list(range(sections[j][0], sections[j][1] + 1)),
                             list(range(sections[j + 1][0], sections[j + 1][1] + 1))):
            count += 1
    return count


def is_subset_section(elf1, elf2):
    return set(elf1).issubset(set(elf2)) or set(elf2).issubset(set(elf1))


with open("day4Input1.txt", "r") as f:
    assignment_pairs = f.readlines()

assignment_pairs = [assignment.replace("\n", "") for assignment in assignment_pairs]
assignment_pairs2 = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
print(find_count_of_duplicates(assignment_pairs))
