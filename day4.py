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

def find_num_valid_passports_correct():
    numValidPassports = 0

    with open('day4_input.txt', 'r') as file:
        passports = file.read().split('\n\n')
        for passport in passports:
            fields = re.split(r'\s+', passport)
            keys = set(map(get_key, fields))
            if len(keys) == 8 or len(keys) == 7 and 'cid' not in keys:
                allValid = True
                for field in fields:
                    if validate(field) == False:
                        allValid = False

                if allValid:
                    numValidPassports += 1
    
    return numValidPassports

valid_eye_colors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
def validate(field):
    fragments = field.split(':')
    key = fragments[0]
    value = fragments[1]

    if key == "byr":
        return int(value) >= 1920 and int(value) <= 2002
    elif key == "iyr":
        return int(value) >= 2010 and int(value) <= 2020
    elif key == "eyr":
        return int(value) >= 2020 and int(value) <= 2030
    elif key == "hgt":
        if re.match(r'^[0-9]+(cm|in)$', value) == None:
            return False
        height = value[0:len(value)-2]
        unit = value[len(value)-2:len(value)]
        if unit == "cm":
            return int(height) >= 150 and int(height) <= 193
        else:
            return int(height) >= 59 and int(height) <= 76
    elif key == "hcl":
        return re.match(r'^#[a-f0-9]{6}$', value) != None
    elif key == "ecl":
        return value in valid_eye_colors
    elif key == "pid":
        return re.match(r'^[0-9]{9}$', value) != None
    elif key == "cid":
        return True

    return False # catch unexpected keys if there were any

print(find_num_valid_passports())
print(find_num_valid_passports_correct())