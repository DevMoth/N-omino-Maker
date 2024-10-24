def rt(grid, x, y):
    #grid, x, y = d
    if x+1 >= len(grid[0]):
        grid = [a+[0] for a in grid]
    grid[y][x+1] = 1
    x += 1
    return [grid, x, y]
def lt(grid, x, y):
    #grid, x, y = d
    if x-1 < 0:
        grid = [[0]+a for a in grid]
        grid[y][x] = 1
    else:
        grid[y][x-1] = 1
        x -= 1
    return [grid, x, y]
def down(grid, x, y):
    #grid, x, y = d
    if y+1 >= len(grid):
        grid = grid + [[0 for i in range(len(grid[0]))]]
    grid[y+1][x] = 1
    y += 1
    return [grid, x, y]
def up(grid, x, y):
    #grid, x, y = d
    if y - 1 < 0:
        grid = [[0 for i in range(len(grid[0]))]] + grid
        grid[y][x] = 1
    else:
        grid[y-1][x] = 1
        y -= 1
    return [grid, x, y]
h = []
def f(n, d = [ [[1]], 0, 0 ]):
    if n > 0:
        moves = [f(n-1,move(d)) for move in [up,down,lt,rt]]
    else:
        h.append(d[0])
f(3)
for a in h:
    for b in a:
        print(*b)
    print()

