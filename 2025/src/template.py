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
    pass


#---- Part 2 ------------------------------------

def part2(data):
    pass


#================================================
#       MAIN
#================================================
if __name__=='__main__':
    data = load_input()
    print(f'Part 1:', part1(data))
    print(f'Part 2:', part2(data))


