## part 1 ##
file = open("input15.txt", "r")

le_list = file.readline()[:-1].split(",")
final_sum = 0

for val in le_list:
    current_val = 0
    for chara in val:
        current_val += ord(chara)
        current_val *= 17
        current_val %= 256
    final_sum += current_val

print(final_sum)


## part 2
boxes = {}

for val in le_list:
    current_val = 0
    for chara in val:
        current_val += ord(chara)
        current_val *= 17
        current_val %= 256
    #current_val = which box to add to
    lens_list = boxes.get(current_val)

    # add to dictionary
    if "=" in val:
        lab, _, no = val.partition("=")
        if lens_list is None:
            lens_list = []
        
        # if something with same lab is in list
        in_list = False
        for lens in lens_list:
            if lens[0] == lab:
                in_list = True
                lens[1] = no
                break
        if not in_list:
            lens_list.append([lab, no])
        boxes[current_val] = lens_list

    # remove from dictionary
    else:
        label = val.split("-")
        if lens_list is not None:
            for lez in lens_list:
                if lez[0] == label:
                    lens_list.remove(lez)
        
        if lens_list == []:
            boxes.pop(current_val)
        else:
            boxes[current_val] = lens_list

print(boxes)

# total = 0   
# # find focusing power
# for k, v in boxes.items():
#     for idx, li in enumerate(v):
#         total += (k + 1) * (idx + 1) * int(li[1])
# print(total)

        



    
    



