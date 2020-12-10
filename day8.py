import re

def get_accumulator_value(instructions):
    accumulator = 0
    cycle_detected = False

    visited = set()
    current_index = 0
    while cycle_detected == False and current_index != len(instructions):
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
        
        if current_index in visited:
            cycle_detected = True
    
    return [accumulator, cycle_detected]

def get_correct_accumulator(instructions):
    for current_index in range(0, len(instructions)):
        old_instruction = instructions[current_index]
        operation = old_instruction[0:3]
        if operation == "jmp" or operation == "nop":
            instructions[current_index] = flip_operation(operation) + old_instruction[3:len(old_instruction)]
            result = get_accumulator_value(instructions)
            if result[1] == False:
                return result[0]
            instructions[current_index] = old_instruction

def flip_operation(operation):
    if operation == "jmp":
        return "nop"
    else:
        return "jmp"

with open('day8_input.txt', 'r') as file:
    instructions = file.read().split('\n')
    print(get_accumulator_value(instructions)[0])
    print(get_correct_accumulator(instructions))

