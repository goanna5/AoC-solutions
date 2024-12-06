file = open("input4.txt", "r")

grid = []

for line in file:
    temp = []
    for char in line[:-1]:
        temp.append(char)
    grid.append(temp)
count = 0
w = len(grid[0])
h = len(grid)

for r_ix in range(h):
    for c_ix in range(w):
        # horizontal
        if (
            ((c_ix + 3) < w)
            and grid[r_ix][c_ix] == "X"
            and grid[r_ix][c_ix + 1] == "M"
            and grid[r_ix][c_ix + 2] == "A"
            and grid[r_ix][c_ix + 3] == "S"
        ):
            count += 1

        if (
            ((c_ix + 3) < w)
            and grid[r_ix][c_ix] == "S"
            and grid[r_ix][c_ix + 1] == "A"
            and grid[r_ix][c_ix + 2] == "M"
            and grid[r_ix][c_ix + 3] == "X"
        ):
            count += 1

        # vertical
        if (
            ((r_ix + 3) < h)
            and grid[r_ix][c_ix] == "X"
            and grid[r_ix + 1][c_ix] == "M"
            and grid[r_ix + 2][c_ix] == "A"
            and grid[r_ix + 3][c_ix] == "S"
        ):
            count += 1

        if (
            ((r_ix + 3) < h)
            and grid[r_ix][c_ix] == "S"
            and grid[r_ix + 1][c_ix] == "A"
            and grid[r_ix + 2][c_ix] == "M"
            and grid[r_ix + 3][c_ix] == "X"
        ):
            count += 1
        # diagonal
        if (
            ((r_ix + 3) < h)
            and ((c_ix + 3) < w)
            and grid[r_ix][c_ix] == "X"
            and grid[r_ix + 1][c_ix + 1] == "M"
            and grid[r_ix + 2][c_ix + 2] == "A"
            and grid[r_ix + 3][c_ix + 3] == "S"
        ):
            count += 1

        if (
            ((r_ix - 3) > -1)
            and ((c_ix + 3) < w)
            and grid[r_ix][c_ix] == "X"
            and grid[r_ix - 1][c_ix + 1] == "M"
            and grid[r_ix - 2][c_ix + 2] == "A"
            and grid[r_ix - 3][c_ix + 3] == "S"
        ):
            count += 1

        if (
            ((r_ix + 3) < h)
            and ((c_ix - 3) > -1)
            and grid[r_ix][c_ix] == "X"
            and grid[r_ix + 1][c_ix - 1] == "M"
            and grid[r_ix + 2][c_ix - 2] == "A"
            and grid[r_ix + 3][c_ix - 3] == "S"
        ):
            count += 1

        if (
            ((r_ix - 3) > -1)
            and ((c_ix - 3) > -1)
            and grid[r_ix][c_ix] == "X"
            and grid[r_ix - 1][c_ix - 1] == "M"
            and grid[r_ix - 2][c_ix - 2] == "A"
            and grid[r_ix - 3][c_ix - 3] == "S"
        ):
            count += 1
print(count)

# part 2
count2 = 0
for r_ix in range(h):
    for c_ix in range(w):
        if (
            grid[r_ix][c_ix] == "A"
            and (r_ix - 1 > -1)
            and (c_ix - 1 > -1)
            and (r_ix + 1 < h)
            and (c_ix + 1 < w)
        ):
            if (
                grid[r_ix - 1][c_ix - 1] == "S" and grid[r_ix + 1][c_ix + 1] == "M"
            ) and (grid[r_ix - 1][c_ix + 1] == "M" and grid[r_ix + 1][c_ix - 1] == "S"):
                count2 += 1
            if (
                grid[r_ix - 1][c_ix + 1] == "S" and grid[r_ix + 1][c_ix - 1] == "M"
            ) and (grid[r_ix - 1][c_ix - 1] == "M" and grid[r_ix + 1][c_ix + 1] == "S"):
                count2 += 1
            if (
                grid[r_ix - 1][c_ix + 1] == "S" and grid[r_ix + 1][c_ix - 1] == "M"
            ) and (grid[r_ix - 1][c_ix - 1] == "S" and grid[r_ix + 1][c_ix + 1] == "M"):
                count2 += 1
            if (
                grid[r_ix - 1][c_ix - 1] == "M" and grid[r_ix + 1][c_ix + 1] == "S"
            ) and (grid[r_ix - 1][c_ix + 1] == "M" and grid[r_ix + 1][c_ix - 1] == "S"):
                count2 += 1
print(count2)
