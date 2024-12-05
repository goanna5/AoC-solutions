file = open("input5.txt", "r")
rulebook = []
seqs = []

for line in file:
    if "|" in line:
        x, y = line[:-1].split("|")
        rulebook.append((int(x), int(y)))

    elif "," in line:
        a = line[:-1].split(",")
        b = []
        for thing in a:
            b.append(int(thing))
        seqs.append(b)


# part 1
def check(s):
    for rule in rulebook:
        x, y = rule
        if x in s and y in s:
            if s.index(x) > s.index(y):
                return False
    return True


mid_sum = 0
for sequence in seqs:
    if check(sequence):
        mid_sum += sequence[len(sequence) // 2]

print(mid_sum)


# part 2
wrong = []


def check2(s):
    for rule in rulebook:
        x, y = rule
        if x in s and y in s:
            if s.index(x) > s.index(y):
                wrong.append(s)
                break


def fix_order(old_s):
    while not check(w):
        for rule in rulebook:
            x, y = rule
            if x in old_s and y in old_s:
                if old_s.index(x) > old_s.index(y):
                    old_s[old_s.index(x)] = y
                    old_s[old_s.index(y)] = x
    return old_s


for sequence in seqs:
    check2(sequence)

mid_sum = 0
for w in wrong:
    aaa = fix_order(w)
    if check(w):
        mid_sum += w[len(w) // 2]

print(mid_sum)
