def find_max_seat_id():
    max = 0
    with open('day5_input.txt', 'r') as file:
        boardingPasses = file.read().split('\n')
        for boardingPass in boardingPasses:
            row = int(boardingPass[0:7].replace('F', '0').replace('B', '1'), 2)
            column = int(boardingPass[7:10].replace('L', '0').replace('R', '1'), 2)
            seatId = row  * 8 + column
            if seatId > max:
                max = seatId
    
    return max

print(find_max_seat_id())