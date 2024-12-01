# sum up the numbers until *just* a new line character appears
# then add the total to an array
# then at end of loop

## Works!! yay

file = open("input1.txt", "r")

elf_total = 0

elves = []

for line in file:
    
    if line == "\n":
        elves.append(elf_total)
        elf_total = 0
    else:
        elf_total += int(line[:-1])


print(max(elves))


# top 3 elves
max_elf = max(elves)
elves.remove(max_elf)

# 2nd max elf
second_max = max(elves)
elves.remove(second_max)

# 3rd max elf
third_max = max(elves)

top_3 = max_elf + second_max + third_max
print(top_3)
