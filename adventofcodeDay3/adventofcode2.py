from collections import defaultdict

if __name__ == '__main__':
    lines = open("./adventofcodeDay3/input.txt").read().strip().split("\n")
    motor = [[y for y in line] for line in lines]
    
    x = -1
    connected = 0
    dim_x = len(motor)
    dim_y = len(motor[0])
    gears = []
    multiplied_numbers = defaultdict(list)

    for line in motor:
        y = -1
        x += 1
        check = False
        number = ""
        for element in line:
            y += 1
            if element.isdigit():
                number += element
                for check_x in [-1, 0, 1]:
                    for check_y in [-1, 0, 1]:
                        if 0 <= x + check_x < dim_x and 0 <= y + check_y < dim_y:
                            element_checked = motor[x + check_x][y + check_y]
                            if not element_checked.isdigit() and element_checked != "." and element_checked != "*":
                                check = True
                            if element_checked == "*":
                                if not (x + check_x, y + check_y) in gears:
                                    gears.append((x + check_x, y + check_y))                           
            
            if not element.isdigit() and gears != [] or gears != [] and dim_y - 1 == y:
                for gear in gears:
                    multiplied_numbers[gear].append(int(number))
                gears = []
                number = ""
                check = False
                
            elif not element.isdigit() and check or check and dim_y - 1 == y:
                
                connected += int(number)
                check = False
                number = ""

            elif not element.isdigit() and not check or not check and dim_y - 1 == y:
                number = ""
                
    connected = 0
    for key, value in multiplied_numbers.items():
        if len(value) == 2:
            add = value[0] * value[1]
            print(key)
            print(value)
            print(add)
            connected += value[0] * value[1]
    
    print(connected)