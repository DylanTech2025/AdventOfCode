import sys

def load_input():
    day = sys.argv[0].replace('src/day','')[:-3]
    with open(f'src/{day}.in', 'r') as infile:
        data = [line.rstrip() for line in infile.readlines()]
    return data

#------------------------------------------------

def parse(data):
    return [(line[0], int(line[1:])) for line in data]

#---- Part 1 ------------------------------------

def part1(data):
    count = 0
    insts = parse(data)

    pos = 50
    for dir, val in insts:
        pos += val if dir == 'R' else -1*val
        pos %= 100

        if pos == 0:
            count += 1

    return count


#---- Part 1 ------------------------------------

def part2(data):
    count = 0
    insts = parse(data)

    pos = 50
    for dir, val in insts:
        for _ in range(val):
            if dir == 'R':
                pos += 1
            else:
                pos -= 1

            if pos == -1 or pos == 100:
                pos %= 100
            
            if pos == 0:
                count += 1

    return count


#================================================
#       MAIN
#================================================
if __name__=='__main__':
    data = load_input()
    print(f'Part 1:', part1(data))
    print(f'Part 2:', part2(data))


