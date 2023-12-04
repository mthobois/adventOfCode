if __name__ == '__main__':
    lines = open("./adventofcodeDay3/input.txt").read().strip().split("\n")
    motor = [[y for y in line] for line in lines]
    
    x = -1
    connected = 0
    dim_x = len(motor)
    dim_y = len(motor[0])

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
                            if not motor[x + check_x][y + check_y].isdigit() and motor[x + check_x][y + check_y] != ".":
                                check = True
                                print(motor[x + check_x][y + check_y])
                            
       
            if not element.isdigit() and check or check and dim_y - 1 == y:
                
                connected += int(number)
                check = False
                number = ""
            elif not element.isdigit() and not check or not check and dim_y - 1 == y:
                number = ""
    print(connected)
     