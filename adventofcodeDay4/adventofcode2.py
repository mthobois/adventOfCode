from collections import defaultdict

if __name__ == '__main__':
    cards = open("./adventofcodeDay4/input.txt").read().strip().split("\n")

    dict = defaultdict(int)

    for card in cards:
        game_id, card = card.split(": ")
        game_id = int(game_id.split(" ", 1)[1])
        if dict[game_id] == 0:
            dict[game_id] = 1
            card_number = 1
        elif dict[game_id] == 1:
            dict[game_id] += 1
            card_number = dict[game_id]
        else:
            dict[game_id] += 1
            card_number = dict[game_id]
            print(f"{game_id} : {card_number}")

        score = 0
        winner, numbers = card.split(" | ")
        
        for i in range(0, len(winner), 3):
            winning_number = int(winner[i] + winner[i+1])
            for i in range (0, len(numbers), 3):
                if winning_number == int(numbers[i] + numbers[i+1]):
                    #print(int(numbers[i] + numbers[i+1]))
                    score += 1
        for i in range (score):
            dict[game_id + i + 1] += card_number

    for k, v in dict.items():
        print(f"id: {k}, value: {v}")
    print(sum(dict.values()))