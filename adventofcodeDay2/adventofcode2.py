if __name__ == '__main__':
    text = open("./adventofcodeDay2/input.txt", "r")
    dict = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0
    wrong_id = []
    for line in text:
        min = {'red': 0, 'green': 0, 'blue': 0}
        line = line.replace("\n", "")
        game_id, set  = line.split(": ")
        game_id = int(game_id.split(" ")[1])
        for game in set.split("; "):
            for draw in game.split(", "):
                number, color = draw.split(" ")
                if int(number) > min[color]:
                    min[color] = int(number)
        sum += min['red'] * min['green'] * min['blue']
    print(sum)
