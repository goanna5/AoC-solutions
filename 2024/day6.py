import time

startT = time.time()
file = open("input6.txt", "r")

grid = []

for i, line in enumerate(file):
    temp = []
    for j, char in enumerate(line[:-1]):
        temp.append(char)
        if char == "^":
            start = (i, j)

    grid.append(temp)

w = len(grid[0])
h = len(grid)

pos = start
dir = "u"
acceptable = ["X", "."]


# part 1
def can_move_to_next(pos, dir, g):
    # can move if next char in direction is X or . or going off grid
    if (pos[0] - 1) < 0 or (pos[0] + 1) >= h or (pos[1] - 1) < 0 or (pos[1] + 1) >= w:
        return True
    elif dir == "u" and (g[pos[0] - 1][pos[1]] in acceptable):
        return True
    elif dir == "d" and (g[pos[0] + 1][pos[1]] in acceptable):
        return True
    elif dir == "l" and (g[pos[0]][pos[1] - 1] in acceptable):
        return True
    elif dir == "r" and (g[pos[0]][pos[1] + 1] in acceptable):
        return True
    return False


def move(pos, dir, g):
    g[pos[0]][pos[1]] = "X"
    if dir == "u":
        new_pos = (pos[0] - 1, pos[1])
    elif dir == "d":
        new_pos = (pos[0] + 1, pos[1])
    elif dir == "l":
        new_pos = (pos[0], pos[1] - 1)
    elif dir == "r":
        new_pos = (pos[0], pos[1] + 1)
    return new_pos


def rotate(dir, g):
    g[pos[0]][pos[1]] = "X"
    if dir == "u":
        new_dir = "r"
    elif dir == "d":
        new_dir = "l"
    elif dir == "l":
        new_dir = "u"
    elif dir == "r":
        new_dir = "d"
    return new_dir


while (-1 < pos[0] < h) and (-1 < pos[1] < w):
    if can_move_to_next(pos, dir, grid):
        pos = move(pos, dir, grid)
    else:
        dir = rotate(dir, grid)


num_xs = 0
for row in grid:
    for col in row:
        if col == "X":
            num_xs += 1

print(num_xs)
endT = time.time()
print("Total time taken for part 1:", (endT - startT), "s")


# part 2
def check_loop(g):
    pos = start
    dir = "u"
    i = 0
    while (-1 < pos[0] < h) and (-1 < pos[1] < w) and i < 10000:
        i += 1
        if can_move_to_next(pos, dir, g):
            pos = move(pos, dir, g)
        else:
            dir = rotate(dir, g)

    if i >= 10000:
        return True
    else:
        return False


p2 = 0

for i in range(h):
    for j in range(w):
        g = [row[:] for row in grid]  # deepcopy array
        if g[i][j] != "#":
            g[i][j] = "#"
            if check_loop(g):
                p2 += 1

print(p2)
endT = time.time()

print("Total time taken for part 2:", (endT - startT), "s")
