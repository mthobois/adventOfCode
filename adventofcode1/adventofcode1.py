
if __name__ == '__main__':
    text = open("./adventofcode1/input.txt", "r")
    values = []
    for word in text:
        for letter in word:
            if letter.isdigit():
                first = letter
                break
        for letter in word[::-1]:
            if letter.isdigit():
                second = letter
                break
        print(first+second)
        values.append(int(first + second))
    print(sum(values))
    