def count_occurences(password, character):
    count = 0
    for i in range(0, len(password)):
        if password[i] == character:
            count += 1
    return count

def find_num_valid_passwords():
    numValid = 0
    for line in open('day2_input.txt'):
        fragments = line.split(' ')
        expectedRange = fragments[0].split('-')

        minExpected = int(expectedRange[0])
        maxExpected = int(expectedRange[1])
        letter = fragments[1][0]
        password = fragments[2]

        occurences = count_occurences(password, letter)
        if occurences >= minExpected and occurences <= maxExpected:
            numValid += 1
    
    return numValid

print(find_num_valid_passwords())