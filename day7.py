import re

def can_contain_gold(current_bag, bags, memo):
    if current_bag in memo:
        return True
    if "shiny gold bag" in bags[current_bag]:
        return True
    for sub_bag in bags[current_bag]:
        if can_contain_gold(sub_bag, bags, memo):
            return True
    return False

def count_gold_bag_containers(rules):
    bags = {}
    for rule in rules:
        rule_fragments = re.findall(r'\w+ \w+ bag', rule)
        if rule_fragments[1] == "no other bag":
            bags[rule_fragments[0]] = []
        else:
            bags[rule_fragments[0]] = rule_fragments[1:len(rule_fragments)]
    
    count = 0
    memo = set()
    for bag in bags:
        if can_contain_gold(bag, bags, memo):
            memo.add(bag)
            count += 1
    return count


with open('day7_input.txt', 'r') as file:
    rules = file.read().split('\n')
    print(count_potential_bag_containers(rules))
