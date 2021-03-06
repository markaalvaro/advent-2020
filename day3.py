def find_num_trees(rightSteps, downSteps):
    position = [0, 0]
    numTrees = 0

    levels = [line.strip() for line in open('day3_input.txt')]
    while True:
        position[0] += rightSteps
        position[0] %= len(levels[0])
        position[1] += downSteps

        if position[1] == len(levels) or (position[1] == len(levels)-1 and downSteps == 2):
            return numTrees
        if levels[position[1]][position[0]] == '#':
            numTrees += 1
    
    return numTrees

case1 = find_num_trees(1, 1)
case2 = find_num_trees(3, 1)
case3 = find_num_trees(5, 1)
case4 = find_num_trees(7, 1)
case5 = find_num_trees(1, 2)

print(case2)
print(case1 * case2 * case3 * case4 * case5)