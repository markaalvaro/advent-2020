def find_product():
    nums = set(int(line.strip()) for line in open('day1_input.txt'))
    for number in nums:
        if (2020-number) in nums:
            return number * (2020-number)

print(find_product())