## part 1 ##
file = open("input2.txt", "r")
valid = True
total_sum = 0

for line in file:
    game_split = line.split(": ")
    game_num = game_split[0].split()[1]
    cubes = game_split[1]
    sets = cubes[:-1].split("; ")
    for set in sets:
        individual_cubes = set.split(", ")
        for individual_cube in individual_cubes:
            parts = individual_cube.split()
            number = int(parts[0])
            colour = parts[1]
            if ((number > 12) and (colour == 'red')) or ((number > 13) and (colour == 'green')) \
                or (number > 14 and colour == 'blue'):
                valid = False
                break
    
    if valid:
        total_sum += int(game_num)
    else: 
        valid = True

print(total_sum)

## part 2 ##
file = open("input2.txt", "r")
total_power = 0

for line in file:
    red_game_cubes = green_game_cubes = blue_game_cubes = []
    cubes = line.split(": ")[1]
    sets = cubes[:-1].split("; ")
    for set in sets:
        individual_cubes = set.split(", ")
        for individual_cube in individual_cubes:
            parts = individual_cube.split()
            number = int(parts[0])
            colour = parts[1]

            if colour == 'red':
                red_game_cubes.append(number)
            elif colour == 'green':
                green_game_cubes.append(number)
            elif colour == 'blue':
                blue_game_cubes.append(number)
    
    power = max(red_game_cubes) * max(green_game_cubes) * max(blue_game_cubes)
    total_power += power

print(total_power)