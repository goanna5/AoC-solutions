## part 1 ##

file = open("input5.txt", "r")
seeds_to_be_planted = []

# just for debugging
seed1 = [79]
seed2 = [14]
seed3 = [55]
seed4 = [13]

def map(line: str):
    dest_strt, src_strt, range_len = line[:-1].split(" ")
    for idx, seed in enumerate(seeds_to_be_planted):
        if seed in range(int(src_strt), int(src_strt)+int(range_len)):
            seed += int(dest_strt) - int(src_strt)
            seeds_to_be_planted[idx] = seed
 
            # this is just for debugging
            if idx == 0:
                seed1.append(seed)
            elif idx == 1:
                seed2.append(seed)
                
            elif idx == 2:
                seed3.append(seed)
            else:
                seed4.append(seed)


for line_number, line in enumerate(file):
    # getting seeds
    if line_number == 0:
        str_seeds = line.split(": ")[1][:-1].split(" ")
        for seed in str_seeds:
            seeds_to_be_planted.append(int(seed))

    # mapping
    if line_number not in [0, 1, 2, 5, 6, 10, 11, 16, 17, 20, 21, 25, 26, 29, 30]:
        map(line)
        
print(f"seed 1 progression: {seed1}")
print(f"seed 2 progression: {seed2}")
print(f"seed 3 progression: {seed3}")
print(f"seed 4 progression: {seed4}")
print(f"final: {seeds_to_be_planted}")
