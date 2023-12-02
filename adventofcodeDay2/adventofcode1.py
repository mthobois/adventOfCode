if __name__ == '__main__':
    text = open("./adventofcodeDay2/input.txt", "r")
    dict = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0
    wrong_id = []
    for line in text:
        line = line.replace("\n", "")
        game_id, set  = line.split(": ")
        game_id = int(game_id.split(" ")[1])
        for game in set.split("; "):
            if game_id in wrong_id:
                break
            for draw in game.split(", "):
                number, color = draw.split(" ")
                if int(number) > dict[color]:
                    wrong_id.append(game_id)
                    break
        if game_id not in wrong_id:
            sum += game_id
    print(sum)


    
    
