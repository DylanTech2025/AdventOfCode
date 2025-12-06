import sys

def load_input():
    day = sys.argv[0].replace('day','')[:-3]
    with open(f'{day}.in', 'r') as infile:
        data = [line.rstrip() for line in infile.readlines()]
    return data

#------------------------------------------------

def parse(data):
    data = [d.split() for d in data]
    nums = [[int(i) for i in d] for d in data[:-1]]
    nums = [[line[i] for line in nums] for i in range(len(data[0]))]
    
    return nums, data[-1]

#---- Part 1 ------------------------------------

def calculate(nums, sign):
    if sign == '+':
        return sum(nums)
    else:
        total = 1
        for num in nums:
            total *= num
        return total

def part1(data):
    data, signs = parse(data)

    grand_total = 0
    for i in range(len(signs)):
        grand_total += calculate(data[i], signs[i])

    return grand_total




#---- Part 2 ------------------------------------

def parse2(data):
    longest = max(len(line) for line in data)
    for i in range(len(data)):
        while (len(data[i]) < longest):
            data[i] += ' '

    return data[:-1], data[-1]

def part2(data):
    data, signs = parse2(data)

    # find the columns containing an operator,
    # signifying the end of a block of numbers
    sign_cols = []
    for i in range(len(signs)):
        if signs[i] in ['+', '*']:
            sign_cols.append(i)

    # read the input right to left, finding all the numbers read vertically
    # when the end of a block is reached, calcuate the sum or product
    grand_total = 0
    col = len(data[0]) - 1 
    while col >= 0:
        nums = []
        while not col+1 in sign_cols:
            num = [row[col] for row in data]
            nums.append(int(''.join(num)))
            col -= 1

        grand_total += calculate(nums, signs[col+1])
        col -= 1

    return grand_total




#================================================
#       MAIN
#================================================
if __name__=='__main__':
    data = load_input()
    print(f'Part 1:', part1(data))
    print(f'Part 2:', part2(data))


