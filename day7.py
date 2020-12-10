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

def count_nested_bags_recursive(current_bag, current_bag_count, bags, memo):
    if current_bag in memo:
        return current_bag_count * memo[current_bag]
    
    count = current_bag_count
    if len(bags[current_bag]) > 0:
        for sub_bag in bags[current_bag]:
            sub_bag_name = str(sub_bag[2:len(sub_bag)])
            sub_bag_count = int(str(sub_bag[0:1]))

            sub_bag_nested_count = count_nested_bags_recursive(sub_bag_name, sub_bag_count, bags, memo)

            memo[sub_bag_name] = int(sub_bag_nested_count / sub_bag_count)
            count += (current_bag_count * sub_bag_nested_count)

    return count


def count_nested_bags(rules):
    bags = {}
    for rule in rules:
        rule_fragments = re.findall(r'\d* ?\w+ \w+ bag', rule)
        if rule_fragments[1] == " no other bag":
            bags[rule_fragments[0]] = []
        else:
            bags[rule_fragments[0]] = rule_fragments[1:len(rule_fragments)]

    return count_nested_bags_recursive("shiny gold bag", 1, bags, {})


with open('day7_input.txt', 'r') as file:
    rules = file.read().split('\n')
    print(count_gold_bag_containers(rules))
    print(count_nested_bags(rules) - 1)
