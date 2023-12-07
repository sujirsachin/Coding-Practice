import re


def find_files(data):
    depth = 0
    sum = 0
    temp_sum = 0
    directory_sum = 0
    for line in data:
        if depth == 0:
            if temp_sum <= 100000:
                sum = max(sum, temp_sum)
            temp_sum = 0
            directory_sum = 0
        if "cd .." in line:
            if directory_sum + temp_sum < 100000:
                directory_sum = directory_sum + temp_sum
            if directory_sum <= 100000:
                sum = max(sum, directory_sum)
            depth -= 1
        elif "cd" in line and not "cd /" in line:
            if directory_sum + temp_sum < 100000:
                directory_sum = directory_sum + temp_sum
            if directory_sum <= 100000:
                sum = max(sum, directory_sum)
            depth += 1
        elif depth > 0 and bool(re.search(r'\d', line)):
            if depth > 1:
                list = re.findall(r'\b\d+\b', line)
                if(temp_sum <= 100000 and int(list[0]) <= 100000):
                    temp_sum += (int(list[0]))
                    temp_sum += (int(list[0]))
                    directory_sum = (int(list[0]))
            else:
                list = re.findall(r'\b\d+\b', line)
                if (temp_sum <= 100000 and int(list[0]) <= 100000):
                    temp_sum += (int(list[0]))
                    directory_sum = (int(list[0]))
    for line in data:
        if bool(re.search(r'\d', line)):
            list = re.findall(r'\b\d+\b', line)
            temp_sum += (int(list[0]))
    if temp_sum <= 100000:
        print(max(sum,temp_sum))
    else:
        print(sum)



with open("day7Input1.txt", "r") as f:
    data = f.readlines()
data = [line.replace("\n", "") for line in data]
print(data)
find_files(data)
