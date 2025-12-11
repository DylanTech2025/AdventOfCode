import sys

def load_input():
    day = sys.argv[0].replace('day','')[:-3]
    with open(f'{day}.in', 'r') as infile:
        data = [line.rstrip() for line in infile.readlines()]
    return data

#------------------------------------------------

def parse(data):
    data = [line.split(',') for line in data]
    return [(int(a), int(b)) for a,b in data]

#---- Part 1 ------------------------------------

def part1(data):
    corners = parse(data)

    largest = 0
    for a in range(len(corners)-1):
        for b in range(1,len(corners)):
            x1,y1 = corners[a]
            x2,y2 = corners[b]
            area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
            if area > largest:
                largest = area

    return largest


#---- Part 2 ------------------------------------
corners = []

#---- Shape -------------------------------------

def getGridDimensions(points):
    maxX,maxY = 0, 0
    for x,y in points:
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y
    return maxX+1, maxY+1


def genGrid(points):
    maxX,maxY = getGridDimensions(points)
    
    grid = []
    for row in range(maxY,-1,-1):
        line = []
        for col in range(maxX+1):
            line.append( '0' if (col, row) in points else '.')        
        grid.append(line)
    grid.append([str(i) for i in range(maxX+1)])
    return grid

def getBorder(corners) -> set:
    corners.append(corners[0])
    border = set()

    for i in range(len(corners)-1):
        x1,y1 = corners[i]
        x2,y2 = corners[i+1]

        # vertical
        if x1 == x2:
            y1,y2 = sorted([y1,y2])
            for y in range(y1, y2+1):
                border.add((x1,y))
        # horizontal 
        if y1 == y2:
            x1,x2 = sorted([x1,x2])
            for x in range(x1,x2+1):
                border.add((x,y1))

    return border
    

def fillShape(border:set) -> set:
    shape = border.copy()

    #---- find a point inside the shape
    # find the min x
    minx = 100000
    miny = 100000
    for x,_ in border:
        minx = x if x < minx else minx
    for y in [y for x,y in border if x == minx]:
        miny = y if y < miny else miny

    x,y = minx+1,miny+1
    
    # queue of points to check
    dirs  = [(-1,0), (1,0),(0,1),(0,-1)]
    check = [(x+dx, y+dy) for dx,dy in dirs]

    while len(check) > 0:
        x,y = check.pop()

        if (x,y) in shape:
            continue
        shape.add((x,y))

        for dx,dy in dirs:
            check.append((x+dx, y+dy))

    return shape


def check(shape:set, x1,y1,x2,y2) -> bool:
    x1,x2 = sorted([x1,x2])
    y1,y2 = sorted([y1,y2])

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if not (x,y) in shape:
                return False

    return True


#---- coord compression -------------------------
compCorners = []

compX,compY = {}, {}
revX, revY = {},{}

def compress(points) -> None:
    X, Y = set(), set()
    for x,y in points:
        X.add(x)
        Y.add(y)

    for i,x in enumerate(sorted(X)):
        compX[x] = i*2
        revX[i*2]  = x
    for i,y in enumerate(sorted(Y)):
        compY[y] = i*2
        revY[i*2]  = y

def find(i) -> (int,int):
    x = compX[ corners[i][0] ]
    y = compY[ corners[i][1] ]
    return x,y

#------------------------------------------------

def part2(data):
    global corners, compCorners
    corners = parse(data)
    
    # find the compressed corners, border, and shape
    compress(corners)
    compCorners = [find(i) for i in range(len(corners))]
    compBorder  = getBorder(compCorners)
    shape       = fillShape(compBorder)

    # find the largest area
    largest = 0
    for a in range(len(compCorners)-1):
        for b in range(1, len(compCorners)):
            x1,y1 = compCorners[a]
            x2,y2 = compCorners[b]

            # find the uncompressed coords to calculate area
            xa,ya = revX[x1], revY[y1]
            xb,yb = revX[x2], revY[y2]
            area  = (abs(xa-xb)+1) * (abs(ya-yb)+1)
            if area > largest:
                if check(shape, x1,y1,x2,y2):
                    largest = area

    return largest

#================================================
#       MAIN
#================================================
if __name__=='__main__':
    data = load_input()
    print(f'Part 1:', part1(data))
    print(f'Part 2:', part2(data))


