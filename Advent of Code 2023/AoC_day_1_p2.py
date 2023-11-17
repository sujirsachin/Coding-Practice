def SumOfCalories(data) -> list:
    calories = []
    for elf in data:
        calories.append(sum(elf[0:]))
    print(calories)
    return calories

def getTopThreeMaxCalories(data):
    calories = SumOfCalories(data)
    calories = sorted(calories)
    print(calories[-3:])
    return sum(calories[-3:])
data = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000,9000], [10000]]

with open('day1Input.txt') as f:
    data2 = f.readlines()
tempList = []
mainList = []
for line in data2:
    if line == '\n':
        mainList.append(tempList)
        tempList = []
        continue
    else:
        tempList.append(int(line[:-1]))
print(getTopThreeMaxCalories(mainList))