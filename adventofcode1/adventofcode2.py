
if __name__ == '__main__':
    text = open("./adventofcode1/input.txt", "r")
    values = []
    dict = {
        'one': "1", 'two': "2", 'three': "3", 'four': "4", 'five': "5",
        'six': "6", 'seven': "7", 'eight': "8", 'nine': "9",
    }
    
    
    for word in text:
        first = ""
        second = ""
        check = ""
        for letter in word:
            if first != "":
                break
            check += letter
            if letter.isdigit():
                first = letter
                break
            for key in dict.keys():
                if key in check:
                    first = dict[key]
                    break
                    
        check = ""
        for letter in word[::-1]:
            if second != "":
                break
            check = letter + check
            if letter.isdigit():
                second = letter
                break
            for key in dict.keys():
                if key in check:
                    second = dict[key]
                    break 
            
        values.append(int(first + second))
    print(sum(values))