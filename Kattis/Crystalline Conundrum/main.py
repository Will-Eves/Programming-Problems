# O(n^2) solution

# basic input
r, c = map(int, input().split())

# grid input
grid = []

for y in range(r):
    grid.append([])

    s = input()
    for x in range(c):
        si = s[x]
        if si == '*':
            grid[y].append([True, True, True, True, True])
        else:
            grid[y].append([False, False, False, False, False])

# grid values are [could_be_from_right, could_be_from_down, could_be_root, could_grow_left, could_grow_up]

# define some helper functions

def exists(cell):
    if cell[0] or cell[1] or cell[2]:
        return True
    
    return False

def root(cell):
    if not cell[0] and not cell[1] and cell[2]:
        return True
    
    return False

def left_root(cell):
    if exists(cell):
        if cell[3]:
            return True
    
    return False

def up_root(cell):
    if exists(cell):
        if cell[4]:
            return True
    
    return False

# Go Down (Testing if can't come from down, if not, all things downstream also can't come from down):

for x in range(c):
    could_be_from_down = True

    for y in range(r):
        if not exists(grid[y][x]):
            continue

        if y == r-1:
            grid[y][x][1] = False
        elif not exists(grid[y+1][x]):
            could_be_from_down = False
            grid[y][x][1] = False

# Go Right (Testing if can't come from right, if not, all things downstram also can't come from down):

for y in range(r):
    could_be_from_right = True

    for x in range(c):
        if not exists(grid[y][x]):
            continue
        
        if x == c-1:
            grid[y][x][0] = False
        elif not exists(grid[y][x+1]):
            could_be_from_right = False
            grid[y][x][0] = False

# Backpropagation must be repeated multiple times to ensure a correct answer (literally just guessed the number)
BACKPROP_COUNT = 4
for iterations in range(BACKPROP_COUNT):
    # Go Down Definite Root:
    for x in range(c):
        root_above = False

        for y in range(r):
            if not exists(grid[y][x]):
                continue

            if root_above:
                grid[y][x][4] = False

            if root(grid[y][x]):
                root_above = True

    # Backpropagate Definite Root:

    for x in range(c):
        from_below = False

        for y in reversed(range(r)):
            if not exists(grid[y][x]):
                from_below = False
                continue

            if not from_below:
                grid[y][x][1] = False

            if up_root(grid[y][x]):
                from_below = True

    # Go Right Definite Root:

    for y in range(r):
        root_left = False

        for x in range(c):
            if grid[y][x] == [False, False, False, False]:
                continue

            if root_left:
                grid[y][x][3] = False

            if root(grid[y][x]):
                root_left = True

    # Backpropogate Definite Root:

    for y in range(r):
        from_right = False

        for x in reversed(range(c)):
            if not exists(grid[y][x]):
                from_right = False
                continue

            if not from_right:
                grid[y][x][0] = False

            if left_root(grid[y][x]):
                from_right = True

# Final (Count Roots):

count = 0

PRINT_GRID = False

for y in range(r):
    o = ''
    for x in range(c):
        if grid[y][x][0:3] == [True, True, True]:
            o += '?'
        elif grid[y][x][0:3] == [True, False, True]:
            o += '-'
        elif grid[y][x][0:3] == [False, True, True]:
            o += '|'
        elif grid[y][x][0:3] == [False, False, True]:
            if grid[y][x][3] and grid[y][x][4]:
                o += 'R'
            elif grid[y][x][3]:
                o += 'L'
            elif grid[y][x][4]:
                o += 'T'
            else:
                o += 'r'
        else:
            o += ' '

        if root(grid[y][x]):
            count += 1
    
    if PRINT_GRID:
        print(o+'|')

if PRINT_GRID:
    print('-'*(r+1))

print(count)