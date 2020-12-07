def find_num_trees(rightSteps, downSteps):
    position = [0, 0]
    numTrees = 0

    levels = [line.strip() for line in open('day3_input.txt')]
    while True:
        position[0] += rightSteps
        position[0] %= len(levels[0])
        position[1] += downSteps

        if position[1] == len(levels):
            return numTrees
        if levels[position[1]][position[0]] == '#':
            numTrees += 1
    
    return numTrees

print(find_num_trees(3, 1))