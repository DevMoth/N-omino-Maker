import copy
def rt(d, x, y):
    grid = copy.deepcopy(d)
    if x+1 >= len(grid[0]):
        grid = [a+[0] for a in grid]
    grid[y][x+1] = 1
    x += 1
    return grid
def lt(d, x, y):
    grid = copy.deepcopy(d)
    if x-1 < 0:
        grid = [[0]+a for a in grid]
        grid[y][x] = 1
    else:
        grid[y][x-1] = 1
        x -= 1
    return grid
def down(d, x, y):
    grid = copy.deepcopy(d)
    if y+1 >= len(grid):
        grid = grid + [[0 for i in range(len(grid[0]))]]
    grid[y+1][x] = 1
    y += 1
    return grid
def up(d, x, y):
    grid = copy.deepcopy(d)
    if y - 1 < 0:
        grid = [[0 for i in range(len(grid[0]))]] + grid
        grid[y][x] = 1
    else:
        grid[y-1][x] = 1
        y -= 1
    return grid

def rotate(d, n):
    od = copy.deepcopy(d)
    for rep in range(n):
        rd = [[0 for j in range(len(od))] for i in range(len(od[0]))]
        for y in range(len(od)):
            for x in range(len(od[0])):
                rd[x][y] = od[len(od)-1-y][x]
        od = rd
    return od
def draw(d):
    for i in d:
        for j in i:
            print("0*"[j],sep = "", end = "")
        print()
    print()
def drawList(blocks):
    for a in blocks:
        draw(a)

def canPlace(d, x, y):
    try:
        return d[y][x] != 1 or x < 0 or y < 0
    except:
        return True
def findMoves(d):
    moves = []
    for y in range(len(d)):
        for x in range(len(d[0])):
            if d[y][x] == 1:
                dirs = ""
                dirs += "1" if canPlace(d, x,y-1) else "0"
                dirs += "1" if canPlace(d, x+1,y) else "0"
                dirs += "1" if canPlace(d, x,y+1) else "0"
                dirs += "1" if canPlace(d, x-1,y) else "0"
                moves.append([x,y, dirs])
    return moves

def pieceCount(d):
    return sum([sum(a) for a in d])

cache = [ [[[1]]],[[[1]]] ]
def isUnique(d, blocks):
    ind = pieceCount(d)
    if (d in blocks[ind]) or (rotate(d,1) in blocks[ind]) or (rotate(d,2) in blocks[ind]) or (rotate(d,3) in blocks[ind]):
        return 0
    return 1
def f(n, d = [[1]]):
    if n <= 0:
        if isUnique(d, cache):
            cache[pieceCount(d)].append(d)
            return [d]
        else:
            return []
    else:
        moves = findMoves(d)
        output = []
        for move in moves:
            if move[2][0] == "1":
                output += f(n-1,up(d, move[0], move[1]))
            if move[2][1] == "1":
                output += f(n-1,rt(d, move[0], move[1]))
            if move[2][2] == "1":
                output += f(n-1,down(d, move[0], move[1]))
            if move[2][3] == "1":
                output += f(n-1,lt(d, move[0], move[1]))
        return output

def cacheStep():
    cache.append([])
    for d in cache[-2]:
        f(1, d)
while 1:
    segCount = int(input("Input segment count: "))
    while segCount > len(cache)-1:
        cacheStep()
    print(len(cache[segCount]))
    #drawList(cache[segCount])
    #drawList(f(int(input("Input segment count: "))-1))
    

