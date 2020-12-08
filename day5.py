def find_max_seat_id(boardingPasses):
    max = 0
    for boardingPass in boardingPasses:
        row = int(boardingPass[0:7].replace('F', '0').replace('B', '1'), 2)
        column = int(boardingPass[7:10].replace('L', '0').replace('R', '1'), 2)
        seatId = row  * 8 + column
        if seatId > max:
            max = seatId
    
    return max

def find_missing_id(boardingPasses):
    ids = []
    for boardingPass in boardingPasses:
        row = int(boardingPass[0:7].replace('F', '0').replace('B', '1'), 2)
        column = int(boardingPass[7:10].replace('L', '0').replace('R', '1'), 2)
        seatId = row  * 8 + column
        ids.append(seatId)    

    sortedIds = sorted(ids)
    for i in range(1, len(sortedIds)):
        if sortedIds[i-1] + 2 == sortedIds[i]:
            return sortedIds[i-1] + 1

with open('day5_input.txt', 'r') as file:
    boardingPasses = file.read().split('\n')
    print(find_max_seat_id(boardingPasses))
    print(find_missing_id(boardingPasses))