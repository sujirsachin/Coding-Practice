def find_valid_games(games):
    final_sum = 0
    for game in games:
        red = 0
        blue = 0
        green = 0
        for i in reversed(range(len(game))):
            if game[i] in "blue":
                blue = max(int(game[i - 1]), blue)
                i -= 1
            if game[i] in "green":
                green = max(int(game[i - 1]),green)
                i -= 1
            if game[i] in "red":
                red = max(int(game[i - 1]), red)
                i -= 1
        final_sum += red * green * blue

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
