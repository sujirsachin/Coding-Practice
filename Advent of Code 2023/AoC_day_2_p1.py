def findMaxScore(data) -> int:
    finalScore = 0
    score = {"X": 1,
             "Y": 2,
             "Z": 3}
    roundScore = {("A", "X"): 3,
                  ("A", "Y"): 6,
                  ("A", "Z"): 0,
                  ("B", "X"): 0,
                  ("B", "Y"): 3,
                  ("B", "Z"): 6,
                  ("C", "X"): 6,
                  ("C", "Y"): 0,
                  ("C", "Z"): 3, }
    for currentRound in data:
        finalScore += score[currentRound[1]] + roundScore[tuple(currentRound)]
    return finalScore


def read_and_transform_data() -> list:
    data =[]
    with open("day2Input.txt", "r") as f:
        read_data = f.readlines()
    for line in read_data:
        temp2 = line.split(" ")
        temp2[1] = temp2[1][0:-1]
        data.append(temp2)
    return data

data = read_and_transform_data()
data2 = [["A", "Y"], ["B", "X"], ["C", "Z"]]
#TODO: Last element is not getting parsed- check later
data[-1][1] = "X"
print(data)
print(findMaxScore(data))
