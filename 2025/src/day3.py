import sys

def load_input():
    day = sys.argv[0].replace('src/day','')[:-3]
    with open(f'src/{day}.in', 'r') as infile:
        data = [line.rstrip() for line in infile.readlines()]
    return data

#------------------------------------------------

def parse(data):
    pass

#---- Part 1 ------------------------------------

def part1(data):
    total = 0

    for bank in data:
        # find the largest digit, for tens
        left = 0
        for i in range(len(bank)-1):
            if bank[i] > bank[left]:
                left = i

        # find the largest digit after left, for ones
        right = left + 1
        for i in range(left+1, len(bank)):
            if bank[i] > bank[right]:
                right = i

        # convert to a number
        num = int( bank[left] + bank[right] )
        total += num

    return total
    


#---- Part 1 ------------------------------------

def get_joltage(bank:str, num_batteries:int) -> int:
    batteries = [-1]

    for b in range(1, num_batteries+1):
        batteries.append(batteries[b-1]+1)

        for i in range(batteries[b], len(bank) - num_batteries + b):
            if bank[i] > bank[batteries[b]]:
                batteries[b] = i

    on_batteries = [bank[i] for i in batteries[1:]]

    return int(''.join(on_batteries))


def part2(data):
    total = 0 

    for bank in data:
        total += get_joltage(bank, 12)

    return total


#================================================
#       MAIN
#================================================
if __name__=='__main__':
    data = load_input()
    print(f'Part 1:', part1(data))
    print(f'Part 2:', part2(data))


