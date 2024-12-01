## part 1 ##

file = open("input7.txt", "r")
CARD_STRENGTH = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
card_strengths_unordered = {}
ordered_hands_one = []
ordered_hands_two = []
ordered_hands_three = []
ordered_hands_four = []
ordered_hands_five = []
ordered_hands_six = []
ordered_hands_seven = []

def strLeftGreatEqThanRight(str_left, str_right):
    left_smaller = False
    for letter_idx in range(0, 5):
        if CARD_STRENGTH[str_left[letter_idx]] > CARD_STRENGTH[str_right[letter_idx]]:
            left_smaller = True
        elif CARD_STRENGTH[str_left[letter_idx]] < CARD_STRENGTH[str_right[letter_idx]]:
            break
    return left_smaller

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_side = arr[:mid]
        right_side = arr[mid:]
        mergeSort(left_side)
        mergeSort(right_side)
 
        i = j = k = 0
 
        while i < len(left_side) and j < len(right_side):
            if strLeftGreatEqThanRight(left_side[i], right_side[j]):   
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1
 
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1
 
        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1


for line in file:
    hand, bid = line[:-1].split()
    types_of_cards = {}

    for card in hand:
        if card in types_of_cards:
            types_of_cards[card] += 1
        else:
            types_of_cards[card] = 1

    if len(types_of_cards) == 1:
        strength = 1 # 5 of a kind

    elif len(types_of_cards) == 2:
        if 4 in types_of_cards.values():
            strength = 2 # four of a kind
        else:
            strength = 3 # full house

    elif len(types_of_cards) == 3:
        if 3 in types_of_cards.values():
            strength = 4 # 3 of a kind
        else:
            strength = 5 # two pair

    elif len(types_of_cards) == 4:
        strength = 6 # one pair

    else:
        strength = 7 # all different

    card_strengths_unordered[hand] = [strength, int(bid)]

for key, value in card_strengths_unordered.items():
    if value[0] == 1:
        ordered_hands_one.append(key)
    elif value[0] == 2:
        ordered_hands_two.append(key)
    elif value[0] == 3:
        ordered_hands_three.append(key)
    elif value[0] == 4:
        ordered_hands_four.append(key)
    elif value[0] == 5:
        ordered_hands_five.append(key)
    elif value[0] == 6:
        ordered_hands_six.append(key)
    elif value[0] == 7:
        ordered_hands_seven.append(key)

ordered_lists = [ordered_hands_one, ordered_hands_two, ordered_hands_three, ordered_hands_four, ordered_hands_five,
                 ordered_hands_six, ordered_hands_seven]
all_lists  = []
total = 0

for le_list in ordered_lists:
    mergeSort(le_list)
    all_lists.extend(le_list)

all_lists.reverse()

for idx, hand in enumerate(all_lists):
    total += (card_strengths_unordered[hand][1] * (idx + 1))

print(total)


## part 2 ##

file = open("input7.txt", "r")
CARD_STRENGTH = {'A':12, 'K':11, 'Q':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1, 'J':0}
card_strengths_unordered = {}
ordered_hands_one = []
ordered_hands_two = []
ordered_hands_three = []
ordered_hands_four = []
ordered_hands_five = []
ordered_hands_six = []
ordered_hands_seven = []

for line in file:
    hand, bid = line[:-1].split()
    types_of_cards = {}

    for card in hand:
        if card in types_of_cards:
            types_of_cards[card] += 1
        else:
            types_of_cards[card] = 1

    # handling J
    if 'J' in types_of_cards:
        # finding how many Js
        num_js = types_of_cards['J']
        types_of_cards.pop('J')

        if types_of_cards != {}:
            card_with_max = max(types_of_cards, key=types_of_cards.get)
            num_highest = types_of_cards[card_with_max]

            # adjusting the new highest
            types_of_cards[card_with_max] = num_highest + num_js

    if len(types_of_cards) == 1 or len(types_of_cards) == 0:
        strength = 1 # 5 of a kind

    elif len(types_of_cards) == 2:
        if 4 in types_of_cards.values():
            strength = 2 # four of a kind
        else:
            strength = 3 # full house

    elif len(types_of_cards) == 3:
            if 3 in types_of_cards.values():
                strength = 4 # 3 of a kind
            else:
                strength = 5 # two pair

    elif len(types_of_cards) == 4:
        strength = 6 # one pair

    else:
        strength = 7 # all different

    card_strengths_unordered[hand] = [strength, int(bid)]


for key, value in card_strengths_unordered.items():
    if value[0] == 1:
        ordered_hands_one.append(key)
    elif value[0] == 2:
        ordered_hands_two.append(key)
    elif value[0] == 3:
        ordered_hands_three.append(key)
    elif value[0] == 4:
        ordered_hands_four.append(key)
    elif value[0] == 5:
        ordered_hands_five.append(key)
    elif value[0] == 6:
        ordered_hands_six.append(key)
    elif value[0] == 7:
        ordered_hands_seven.append(key)

ordered_lists = [ordered_hands_one, ordered_hands_two, ordered_hands_three, ordered_hands_four, ordered_hands_five,
                ordered_hands_six, ordered_hands_seven]
all_lists  = []
total = 0

for le_list in ordered_lists:
    mergeSort(le_list)
    all_lists.extend(le_list)

all_lists.reverse()

for idx, hand in enumerate(all_lists):
    total += (card_strengths_unordered[hand][1] * (idx+1))

print(total)