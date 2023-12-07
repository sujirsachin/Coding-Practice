def find_valid_games(games):
    game_number = 0
    final_sum = 0
    for game in games:
        red = 0
        blue = 0
        green = 0
        for i in reversed(range(len(game))):
            if game[i] in "blue":
                blue = int(game[i - 1])
                if blue > 14:
                    break
                i -= 1
            if game[i] in "green":
                green = int(game[i - 1])
                if green > 13:
                    break
                i -= 1
            if game[i] in "red":
                red = int(game[i - 1])
                if red > 12:
                    break
                i -= 1
        game_number += 1
        if red <= 12 and green <= 13 and blue <= 14:
            final_sum += game_number

    print(final_sum)


with open("day2Input2.txt", "r") as f:
    data = f.readlines()

data = [line.replace("\n", "") for line in data]
games = []
for line in data:
    line = line.replace(":", "")
    line = line.replace(";", "")
    line = line.replace(",", "")
    games.append(line.split(" "))

find_valid_games(games)
