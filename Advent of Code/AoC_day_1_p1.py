
def getMaxCalories(data):
    maxCalories = 0
    for elf in data:
        maxCalories = max(maxCalories, sum(elf[0:]))
    return maxCalories

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
print(mainList)
print(getMaxCalories(mainList))