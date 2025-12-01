import sys


def load_input():
    day = sys.argv[0].replace('solns/day','')[:-3]
    with open(f'solns/{day}.in', 'r') as infile:
        data = [line.rstrip() for line in infile.readlines()]
    return data


data = load_input()
print(data)


