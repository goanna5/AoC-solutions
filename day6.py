## part 1 ##

file = open("input6.txt", "r")
times = []
distances = []
final = 1

for line in file:
    values = line[:-1].split(":")[1].split(" ")
    if times == []:
        for val in values:
            if val != "":
                times.append(int(val))
    else:
        for val in values:
            if val != "":
                distances.append(int(val))

for time_idx, time in enumerate(times):
    that_tot = 0
    # not including 0 or full time of race
    for held_time in range(1, time):
        distance_travelled = (time - held_time) * held_time
        if distance_travelled > distances[time_idx]:
            that_tot += 1

    final *= that_tot
    
print(final)

## part 2 ##

file = open("input6.txt", "r")
times = ""
distances = ""
number_beats = 0

for line in file:
    values = line[:-1].split(":")[1].split(" ")
    if times == "":
        for val in values:
            times += val
    else:
        for val in values:
            distances += val

times = int(times)
distances = int(distances)   

# not including 0 or full time of race
for held_time in range(1, times):
    distance_travelled = (times - held_time) * held_time
    if distance_travelled > distances:
        number_beats += 1

print(number_beats)