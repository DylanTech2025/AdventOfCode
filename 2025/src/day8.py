import sys
from collections import defaultdict

def load_input():
    day = sys.argv[0].replace('src/day','')[:-3]
    with open(f'src/{day}.in', 'r') as infile:
        data = [line.rstrip() for line in infile.readlines()]
    return data

#------------------------------------------------

def parse(data):
    data = [line.split(',') for line in data]
    data = [(int(x), int(y), int(z)) for x,y,z in data]
    return data

#---- Part 1 ------------------------------------

def getDistances(nodes):
    distances = []
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            x1,y1,z1 = nodes[i]
            x2,y2,z2 = nodes[j]
            distance = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
            distances.append((distance, i,j))
    return distances


# return the parent node of i's circuit
def find(parents, i):
    #---- base case: found root node
    if parents[i] == i:
        return i

    #---- recursive case
    parents[i] = find(parents, parents[i])
    return parents[i]

# merge i's and j's circuits
def union(parents, i,j):
    # i's parent node
    pi = find(parents, i)

    # j's parent node
    pj = find(parents, j)

    # join the cicuits by changing j's
    # parent to i's parent
    parents[pj] = pi


def part1(data):
    nodes = parse(data)
    parents = {i:i for i in range(len(nodes))}

    # find the distances that every is away from eachother
    distances = getDistances(nodes)

    # use Union Find to combine nodes into circuits
    distances.sort()
    for pair in range(1000):
        _, i, j = distances[pair]

        # skip the items that are in the same circuit
        if find(parents, i) == find(parents, j):
            continue

        # combine the circuits
        union(parents, i, j)

    # calcuate the answer
    # keys: root node number, values: how many nodes belong to that root
    sizes = defaultdict(int)
    for node in parents.values():
        root = find(parents, node)
        sizes[root] += 1

    ans = 1
    for s in sorted(sizes.values())[-3:]:
        ans *= s

    return ans

#---- Part 2 ------------------------------------

def part2(data):
    nodes = parse(data)
    parents = {i:i for i in range(len(nodes))}

    # find the distances that every is away from eachother
    distances = getDistances(nodes)

    # use Union Find to combine nodes into circuits
    distances.sort()
    for _,i,j in distances:
        
        # skip the items that are in the same circuit
        if find(parents, i) == find(parents, j):
            continue

        # combine the circuits
        union(parents, i, j)

        if all(find(parents, 0) == find(parents, i) for i in range(len(nodes))):
            break

    x1,_,_ = nodes[i]
    x2,_,_ = nodes[j]

    return x1 * x2


#================================================
#       MAIN
#================================================
if __name__=='__main__':
    data = load_input()
    print(f'Part 1:', part1(data))
    print(f'Part 2:', part2(data))


