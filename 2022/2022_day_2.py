# A = rock opponent (1)
# B = paper opponent (2)
# C = scissors opponent (3)

# X = rock me (1)
# Y = paper me (2)
# Z = scissors me (3)

# 0 if lost, 3 if draw, 6 if won

# win for me
# rock paper (A Y)
# scissors rock (C X)
# paper scissors (B Z)

# draw iff same

# otherwise opponent has won so 0 points

# doesnt work

total_score = 0
winning_combo = ['A Y\n', 'C X\n', 'B Z\n']

file = open("input.txt", "r")
for line in file:
    split_line = line.split(' ')
    # individual scores
    if split_line[1] == 'X':
        total_score += 1
    elif split_line[1] == 'Y':
        total_score += 2
    else:
        total_score += 3


    # score winning overall
    if split_line[0] == split_line[1]:
        total_score += 3
    elif line in winning_combo:
        total_score += 6


print(total_score)