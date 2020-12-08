import re

def count_affirmatives_per_group(groups):
    count = 0

    for group in groups:
        count += len(set(re.sub(r'\s+', '', group)))
    
    return count

def to_set(str):
    return set(str)

def count_full_group_affirmatives(groups):
    count = 0

    for group in groups:
        answers = re.split(r'\s+', group)
        affirmatives = set(answers[0])
        for i in range(1, len(answers)):
            affirmatives = affirmatives.intersection(answers[i])
        count += len(affirmatives)
    
    return count


with open('day6_input.txt', 'r') as file:
    groups = file.read().split('\n\n')
    print(count_affirmatives_per_group(groups))
    print(count_full_group_affirmatives(groups))