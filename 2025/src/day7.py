import copy

def parse(data):
    data = [[l for l in line] for line in data]

    # insert the inital beam
    for c in range(len(data[0])):
        if data[0][c] == 'S':
            data[1][c] = '|'

    return data

#====================================================================


# initial thought is to count the number of splitters,
# but there maybe splitters that aren't reached
def part1(data):
    data = parse(data)

    # simulate the splits
    num_splits = 0
    row = 1
    while row < len(data) - 1:
        for col in range(len(data[row])):
            if data[row][col] == '|':
                if data[row+1][col] == '^':
                    num_splits += 1
                    data[row+1][col-1] = '|'
                    data[row+1][col+1] = '|'
                else:
                    data[row+1][col] = '|'
        row += 1

    return num_splits

#--------------------------------------------------------------------

# use a BFS
# always pass in a list such that the first line of the list
# is the current line that the beam is on
MEM = {}
def solve(time:list, line:int, beam:int) -> int:
    #---- already solved
    if (line,beam) in MEM:
        return MEM[(line,beam)]

    #---- base case: the bottom is reached
    if line == len(time) - 2:
        return 1

    #--- recursive case:
    next = line+1

    # split
    if time[next][beam] == '^':
        # split time and extend the beam
        time1                   = copy.deepcopy(time)
        time2                   = copy.deepcopy(time)
        time1[next][beam-1]     = '|'
        time2[next][beam+1]     = '|'

        ans = solve(time1, next, beam-1) + solve(time2, next, beam+1)

    # no split
    else:
        time[next][beam] = '|'
        ans = solve(time, next, beam)

    MEM[(line,beam)] = ans
    return ans


def part2(data):
    data = parse(data)
    
    # find the beam
    for col in range(len(data[1])):
        if data[1][col] == '|':
            beam = col
            break

    return solve(data[1:], 0, beam)



