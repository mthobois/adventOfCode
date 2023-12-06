if __name__ == '__main__':
    cards = open("./adventofcodeDay4/input.txt").read().strip().split("\n")

    global_score = 0

    for card in cards:
        card = card.split(": ")[1]
        score = 0
        winner, numbers = card.split(" | ")
        
        for i in range(0, len(winner), 3):
            winning_number = int(winner[i] + winner[i+1])
            for i in range (0, len(numbers), 3):
                if winning_number == int(numbers[i] + numbers[i+1]):
                    print(int(numbers[i] + numbers[i+1]))
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
        global_score += score
    print(global_score)