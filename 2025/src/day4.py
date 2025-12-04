import sys

def load_input():
    day = sys.argv[0].replace('src/day','')[:-3]
    with open(f'src/{day}.in', 'r') as infile:
        data = [line.rstrip() for line in infile.readlines()]
    return data

#------------------------------------------------

def parse(data):
    return [[a for a in row] for row in data]

#---- Part 1 ------------------------------------

def get_num_adj(grid, r, c):
    num_adj = 0

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            row,col = r+dr, c+dc

            if row < 0 or row >= len(grid):
                continue
            if col < 0 or col >= len(grid[r]):
                continue
            if dr == 0 and dc == 0:
                continue
            
            if grid[row][col] == '@':
                num_adj += 1

    return num_adj

def part1(data):
    total = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '@' and get_num_adj(data, row, col) < 4:
                total += 1

    return total

#---- Part 2 ------------------------------------

def find_removable(grid) -> set:
    removable = set()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@' and get_num_adj(grid, row, col) < 4:
                removable.add((row,col))

    return removable


def part2(data):
    grid        = parse(data)
    total       = 0
    removable   = find_removable(grid)

    while len(removable) > 0:
        total += len(removable)

        # remove rolls
        for row, col in removable:
            grid[row][col] = '.'
        
        # find points that can now be removed
        removable = find_removable(grid)
    
    return total


#================================================
#       MAIN
#================================================
if __name__=='__main__':
    data = load_input()
    print(f'Part 1:', part1(data))
    print(f'Part 2:', part2(data))


