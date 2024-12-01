## part 1 ##

file = open("input9.txt", "r")

def findNextRow(line_arr):
    all_zero = True
    first_element = line_arr[0]
    for word in line_arr:
        if first_element != word:
            all_zero = False
            break
        else:
            all_zero = True
        


    next_arr = []
    for idx, num in enumerate(line_arr):
        if idx < len(line_arr):
            diff = line_arr[idx + 1] - num
            next_arr.append(diff)

    findNextRow(next_arr)




for line in file:
    findNextRow(map(int, line[:-1].split(" ")))
