import sys

def load_input():
    day = sys.argv[0].replace('src/day','')[:-3]
    with open(f'src/{day}.in', 'r') as infile:
        data = [line.rstrip() for line in infile.readlines()]
    return data

#------------------------------------------------

def parse(data):
    data = data[0].split(",")
    data = [item.split('-') for item in data]
    return [(int(a), int(b)) for a,b in data]

#---- Part 1 ------------------------------------

def part1(data):
    ranges = parse(data)

    total = 0
    for a,b in ranges:
        for i in range(a,b+1):
            numstr = str(i)

            if len(numstr) % 2 == 1:
                continue

            half = len(numstr) // 2
            if numstr[half:] == numstr[:half]:
                total += i

    return total


#---- Part 1 ------------------------------------

def is_invalid(numstr) -> bool:
    # try different chunk sizes
    for c in range(1, len(numstr)//2 + 1):
        if not len(numstr) % c == 0:
            continue

        # split the number into equal size chunks
        # max chunk size is half the length of numstr
        chunks = [numstr[i:i+c] for i in range(0, len(numstr), c)]

        if all(chunks[0] == chunks[i] for i in range(1,len(chunks))):
            return True

    return False


def part2(data):
    ranges = parse(data)

    total = 0
    for a,b in ranges:
        for i in range(a,b+1):
            if is_invalid(str(i)):
                total += i

    return total

#================================================
#       MAIN
#================================================
if __name__=='__main__':
    data = load_input()
    print(f'Part 1:', part1(data))
    print(f'Part 2:', part2(data))


