file = open("input3.txt", "r")

same_letter = []
line_array = []
badges = []

for line in file:
    
    mid_point = len(line) // 2
    first = line[0:mid_point]
    second = line[mid_point:]

    for letter in first:
        if letter in second:
            same_letter.append(letter)
            break
    
    # finding the thing common to all 3 elves
    line_array.append(line)
    if len(line_array) == 3:
        for letter in line_array[0]:
            if (letter in line_array[1]) and (letter in line_array[2]) and (letter != '\n'):
                badges.append(letter)

        line_array = []
    


print(len(badges))


value = 0

# working out score based on ascii
for chara in same_letter:
    # if uppercase
    if ord(chara) < 91:
        value += ord(chara) - 38
    # lowercase
    else:
        value += ord(chara) - 96

print(value)
        




