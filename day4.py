import re

def get_key(field):
    return field.split(':')[0]

def find_num_valid_passports():
    numValidPassports = 0

    with open('day4_input.txt', 'r') as file:
        passports = file.read().split('\n\n')
        for passport in passports:
            fields = re.split(r'\s+', passport)
            keys = set(map(get_key, fields))
            if len(keys) == 8 or len(keys) == 7 and 'cid' not in keys:
                numValidPassports += 1
    
    return numValidPassports

print(find_num_valid_passports())