# ## part 1 ##

# file = open("input4.txt", "r")

# total = 0

# for line in file:

#     cards = line.split(": ")[1]
#     winning = cards.split("| ")[0]
#     yours = cards.split("| ")[1][:-1]

#     winning_best = winning.split(" ")
#     yours_best = yours.split(" ")

#     num_win = 0

#     for num in winning_best:
#         if num in yours_best and num != '':
#             num_win += 1
            
#     if num_win != 0:
#         num_win -= 1
#         total += 2**num_win

# print(total)


## part 2 ##

file = open("input4.txt", "r")

MATCHES_AND_CARD_NUMS = {}


for line in file:
    card_number = line.split(":")[0].split(" ")[1]
    cards = line.split(": ")[1]
    winning = cards.split("| ")[0]
    yours = cards.split("| ")[1][:-1]

    winning_best = winning.split(" ")
    yours_best = yours.split(" ")

    num_win = 0

    for num in winning_best:
        if num in yours_best and num != '':
            num_win += 1

    # 1 is the number of copies at this time
    MATCHES_AND_CARD_NUMS[int(card_number)] = [num_win, 1]

print(MATCHES_AND_CARD_NUMS)

WITH_DUPLICATES = MATCHES_AND_CARD_NUMS

for card_num, le_arr in MATCHES_AND_CARD_NUMS.items():
    num_matches = le_arr[0]
    copies = le_arr[1]

    while card_num + num_matches + 1 <= 6: # 6 is the number of cards
        for perf_num in range(card_num+1, card_num + num_matches+1):
            if num_matches != 0:
                current_arr = WITH_DUPLICATES[perf_num]
                MATCHES_AND_CARD_NUMS[perf_num] = [current_arr[0], current_arr[1]+1]
                print(current_arr)
        break
print(WITH_DUPLICATES)


# for card_num, le_arr in MATCHES_AND_CARD_NUMS.items():
#     num_matches = le_arr[0]
#     copies = le_arr[1]

#     for i in range(card_num+1, card_num+num_matches+2):
#         try:
#             current_arr = MATCHES_AND_CARD_NUMS[i]
#             print(current_arr)
#             MATCHES_AND_CARD_NUMS[i] = [current_arr[0], current_arr[1]+1]
#         except:
#             break

# print(MATCHES_AND_CARD_NUMS)
    


