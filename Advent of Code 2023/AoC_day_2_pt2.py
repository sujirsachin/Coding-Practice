print("Advent of Code 2022, Link to Problem: {}".format('https://adventofcode.com/2022/day/2'))


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
    win = {"A": "Y",
           "B": "Z",
           "C": "X"}
    lose = {"A": "Z",
            "B": "X",
            "C": "Y"}
    draw = {"A": "X",
            "B": "Y",
            "C": "Z"}
    for currentRound in data:
        if currentRound[1] == "Z":
            currentRound[1] = win[currentRound[0]]
        elif currentRound[1] == "X":
            currentRound[1] = lose[currentRound[0]]
        else:
            currentRound[1] = draw[currentRound[0]]
        finalScore += score[currentRound[1]] + roundScore[tuple(currentRound)]
    return finalScore


def readAndTransformData():
    data = []
    with open("day2Input.txt", "r") as f:
        readData = f.readlines()
    for line in readData:
        temp2 = line.split(" ")
        temp2[1] = temp2[1][0:-1]
        data.append(temp2)
    return data


data = readAndTransformData()

data2 = [["A", "Y"], ["B", "X"], ["C", "Z"]]
# TODO: Last element is not getting parsed- check later
data[-1][1] = "X"
print(findMaxScore(data))
