## part 1 ##

file = open("input8.txt", "r")
NODES = {}
found = False

for line_idx, line in enumerate(file):
    if line_idx == 0:
        sequence = line[:-1]
    
    elif line_idx > 1:
        split_line = line[:-1].split(" = ")
        res = tuple(map(str, split_line[1][1:-1].split(', ')))
        NODES[split_line[0]] = res

steps = 0
current_key = 'PNM'

while not found:
    for dir in sequence:
        if current_key == 'ZZZ':
            found = True
            break
        steps += 1
        if dir == 'L':
            current_key = NODES[current_key][0]
        else:
            current_key = NODES[current_key][1]

print(steps)