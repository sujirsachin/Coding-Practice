def part_number(engine):
    number=""
    for line in engine:
        for i in range(0, len(line)):
            if line[i] == '.':
                print(number)
                number = ""
            if line[i].isdigit():
                if line[i+1] != len(line) and line[i+1].isdigit():
                    number += line[i]
                    pass
                elif line[i+1] != len(line) and line[i+1] != '.' and not line[i+1].isalnum():
                    number += line[i]
        print(number)
with open("day3Input1.txt", "r") as f:
    data = f.readlines()
data = [line.replace("\n","") for line in data]
engine = []
for line in data:
    engine.append(list(line))
print(data)
print(engine)
part_number(engine)