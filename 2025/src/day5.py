import sys

def load_input():
    day = sys.argv[0].replace('src/day','')[:-3]
    with open(f'src/{day}.in', 'r') as infile:
        data = [line.rstrip() for line in infile.readlines()]
    return data

#------------------------------------------------

def combine_regions(data):
    lows,highs = [], []
    for low, high in data:
        lows.append(low)
        highs.append(high)
    lows.sort()
    highs.sort()

    ranges = []
    l,r = 0,0

    while l < len(lows):
        if r+1 < len(lows) and highs[r] >= lows[r+1]:
            r+=1

        else:
            ranges.append((lows[l], highs[r]))
            r +=1
            l = r

    return ranges

def parse(data):
    for i in range(len(data)):
        if data[i] == '':
            break

    ranges = [r.split('-') for r in data[:i]]
    ranges = [(int(l), int(r)) for l,r in ranges]

    ingredients = data[i+1:]
    ingredients = [int(i) for i in ingredients]

    return ranges, ingredients

#---- Part 1 ------------------------------------

def part1(data):
    ranges, ingredients = parse(data)

    ranges = combine_regions(ranges)
    ingredients.sort()

    i = 0
    total = 0

    for l, r in ranges:

        # skip everything below the range that we're checking
        while ingredients[i] < l:
            i += 1

        # count everything that's in the region
        while i < len(ingredients) and ingredients[i] <= r:
            total += 1
            i += 1
    
    return total


def part1_slow(data):
    ranges, ingredients = parse(data)

    checked = set()
    total = 0

    for l,r in ranges:
        for i in ingredients:
            if i in checked:
                continue

            if l <= i <= r:
                total += 1
                checked.add(i)

    return total


#---- Part 2 ------------------------------------



def part2(data):
    ranges, _ = parse(data)
    ranges = combine_regions(ranges)

    total = 0
    for low, high in ranges:
        total += high - low + 1

    return total

#================================================
#       MAIN
#================================================
if __name__=='__main__':
    data = load_input()
    print(f'Part 1:', part1(data))
    print(f'Part 2:', part2(data))


