import re

def get_accumulator_value_pre_loop(instructions):
    accumulator = 0

    visited = set()
    current_index = 0
    while current_index not in visited:
        visited.add(current_index)

        match = re.search(r'(\w+) \+?(-?\d+)', instructions[current_index])
        operation = match.group(1)
        argument = match.group(2)

        if operation == "acc":
            accumulator += int(argument)
            current_index += 1
        elif operation == "nop":
            current_index += 1
        else:
            current_index += int(argument)
    
    return accumulator


with open('day8_input.txt', 'r') as file:
    instructions = file.read().split('\n')
    print(get_accumulator_value_pre_loop(instructions))
