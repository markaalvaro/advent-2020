import re

def count_affirmatives_per_group(groups):
    count = 0

    for group in groups:
        count += len(set(re.sub(r'\s+', '', group)))
    
    return count

with open('day6_input.txt', 'r') as file:
    groups = file.read().split('\n\n')
    print(count_affirmatives_per_group(groups))